import pytest
from sqlalchemy import create_engine, schema
from sqlalchemy.orm import sessionmaker, close_all_sessions, Session, clear_mappers

from opencdms.utils.db import get_cdm_connection_string
from opencdms.provider.opencdmsdb import mapper_registry, start_mappers

from cdms_pygeoapi import CDMSProvider
from pygeoapi.provider.base import (
    ProviderItemNotFoundError
)
from opencdms.utils.seeder import seed_observations

DB_URL = get_cdm_connection_string()

db_engine = create_engine(DB_URL)
Base = mapper_registry.generate_base()

@pytest.fixture
def db_session():
    Session = sessionmaker(bind=db_engine)
    session = Session()
    yield session
    session.close()


def setup_module(module):
    schemas = {v.schema for k, v in Base.metadata.tables.items()}

    for _schema in schemas:
        if not db_engine.dialect.has_schema(db_engine, _schema):
            db_engine.execute(schema.CreateSchema(_schema))
    Base.metadata.create_all(bind=db_engine)
    start_mappers()


def teardown_module(module):
    close_all_sessions()
    Base.metadata.drop_all(bind=db_engine)
    clear_mappers()



def test_create_observations(db_session):
    created = seed_observations(db_session)
    assert created is True


@pytest.fixture()
def config():
    return {
        'name': 'PostgreSQL',
        'type': 'feature',
        'data': {'host': '127.0.0.1',
                 'dbname': 'postgres',
                 'user': 'postgres',
                 "port": 35432,
                 'password': "password",
                 'search_path': ['cdm', 'public']
                 },
        'id_field': 'id',
        'table': 'observation',
        'geom_field': 'location'
    }


def test_query_should_show_selected_fields(config):
    # pytest.set_trace()
    """Test query with select properties"""
    p = CDMSProvider(config)
    select_properties=['comments','host_id']
    feature_collection = p.query(select_properties=select_properties)
    assert feature_collection.get('type') == 'FeatureCollection'
    features = feature_collection.get('features')
    assert features is not None
    feature = features[0]
    properties = feature.get('properties')
    assert select_properties[0] in properties.keys()
    assert properties is not None
    geometry = feature.get('geometry')
    assert geometry is not None

def test_query_with_property_filter(config):
    """Test query valid features when filtering by property"""
    p = CDMSProvider(config)
    properties=[("result_description","A good result" )]
    select_properties = ["result_description"]
    feature_collection = p.query(properties=properties, select_properties=select_properties)
    assert feature_collection.get('type') == 'FeatureCollection'
    features = feature_collection.get('features')
    assert features is not None
    feature = features[0]
    properties = feature.get('properties')
    assert select_properties[0] in properties.keys()
    assert properties is not None
    geometry = feature.get('geometry')
    assert geometry is not None


def test_query_bbox(config):
    """Test query with a specified bounding box """
    p = CDMSProvider(config)
    properties=[("result_description","A good result" )]
    select_properties = ["result_description"]
    NG_bbox = [ 2.69170169436, 4.24059418377, 14.5771777686, 13.8659239771 ] # Nigeria https://gist.github.com/graydon/11198540
    feature_collection = p.query(bbox=NG_bbox)
    features = feature_collection.get('features')
    assert len(features) == 10

def test_instantiation(config):
    """Test attributes are correctly set during instantiation."""
    # Act
    provider =CDMSProvider(config)

    # Assert
    assert provider.name == "PostgreSQL"
    # assert provider.table == "observation"
    assert provider.id_field == "id"


def test_query_skip_geometry(config):
    """Test query without geometry"""
    p = CDMSProvider(config)
    result = p.query(skip_geometry=True)
    feature = result['features'][0]
    assert feature['geometry'] is None

def test_get_not_existing_item_raise_exception(config):
    """Testing query for a not existing object"""
    p = CDMSProvider(config)
    with pytest.raises(ProviderItemNotFoundError):
        p.get("2329039")