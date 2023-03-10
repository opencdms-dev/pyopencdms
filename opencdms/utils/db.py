from opencdms.config import config
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Query


def get_connection_string(
    engine: str,
    driver: str,
    user: str,
    password: str,
    host: str,
    port: str,
    db_name: str,
) -> str:
    return f"{engine}+{driver}://{user}:{password}@{host}:{port}/{db_name}"


def get_cdm_connection_string() -> str:
    return get_connection_string(
        engine=config.CDM_DB_ENGINE,
        driver=config.CDM_DB_DRIVER,
        user=config.CDM_DB_USER,
        password=config.CDM_DB_PASS,
        host=config.CDM_DB_HOST,
        port=config.CDM_DB_PORT,
        db_name=config.CDM_DB_NAME,
    )


def cdm_session():
    DB_URL = get_cdm_connection_string()
    db_engine = create_engine(DB_URL)
    SessionLocal = sessionmaker(bind=db_engine)
    session = SessionLocal()
    return session


def get_count(q: Query):
    """
    Return the number of rows that matches a query
    """
    count_q = q.statement.with_only_columns(
        func.count(), maintain_column_froms=True
    ).order_by(None)
    count = q.session.execute(count_q).scalar()
    return count
