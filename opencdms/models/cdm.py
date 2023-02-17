# =============================================================================
# MIT License
#
# Copyright (c) 2023, OpenCDMS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================
from abc import ABC as AbstractBase
from dataclasses import dataclass
from datetime import datetime
from typing import NewType, Optional

Geography = NewType("Geography", str)

class DomainModelBase(AbstractBase):
    """
    Base class for OpenCDMS domain models.
    """

    def table_info(self) -> str:
        """Return table comment"""
        return self._comment

    def column_info(self, column: str) -> str:
        """Return column information"""
        return self._comments.get(column)


@dataclass
class ObservationType(DomainModelBase):
    id: int
    name: str
    description: str
    links: Optional[dict]
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for observation type",
        "description": "Description of observation type",
        "links": "Link(s) to definition of observation type"
    }
    _comment = "placeholder"


@dataclass
class FeatureType(DomainModelBase):
    id: int
    name: str
    description: str
    links: Optional[dict]
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for feature type",
        "description": "Description of feature type",
        "links": "Link(s) to definition of feature type"
    }
    _comment = "placeholder"


@dataclass
class User(DomainModelBase):
    id: str
    name: str
    _comments = {
        "id": "ID / primary key",
        "name": "Name of user"
    }
    _comment = "placeholder"


@dataclass
class ObservedProperty(DomainModelBase):
    id: int
    short_name: str
    standard_name: Optional[str]
    units: str
    description: str
    links: Optional[dict]
    _comments = {
        "id": "ID / primary key",
        "short_name": "Short name representation of observed property, e.g. 'at'",
        "standard_name": "CF standard name (if applicable), e.g. 'air_temperature'",
        "units": "Canonical units, e.g. 'Kelvin'",
        "description": "Description of observed property",
        "links": "Link(s) to definition / source of observed property"
    }
    _comment = "placeholder"


@dataclass
class ObservingProcedure(DomainModelBase):
    id: int
    name: str
    description: str
    links: Optional[dict]
    _comments = {
        "id": "ID / primary key",
        "name": "Name of observing procedure",
        "description": "Description of observing procedure",
        "links": "Link(s) to further information"
    }
    _comment = "placeholder"


@dataclass
class RecordStatus(DomainModelBase):
    id: int
    name: str
    description: str
    _comments = {
        "id": "ID / primary key",
        "name": "Short name for status",
        "description": "Description of the status"
    }
    _comment = "placeholder"


@dataclass
class TimeZone(DomainModelBase):
    id: int
    abbreviation: str
    name: str
    offset: str
    _comments = {
        "id": "ID / primary key",
        "abbreviation": "Abbreviation for time zone",
        "name": "Name / description of timezone",
        "offset": "Offset from UTC"
    }
    _comment = "placeholder"


@dataclass
class Host(DomainModelBase):
    id: str
    name: str
    description: Optional[str]
    links: Optional[dict]
    location: Optional[Geography]
    elevation: Optional[float]
    wigos_station_identifier: Optional[str]
    facility_type: Optional[str]
    date_established: Optional[datetime]
    date_closed: Optional[datetime]
    wmo_region: Optional[str]
    territory: Optional[str]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    version: int
    change_date: datetime
    user_id: int
    status_id: int
    comments: str
    time_zone_id: Optional[int]
    _comments = {
        "id": "ID / primary key",
        "name": "Preferred name of host",
        "description": "Description of host",
        "links": "URI to host, e.g. to OSCAR/Surface",
        "location": "Location of station",
        "elevation": "Elevation of station above mean sea level",
        "wigos_station_identifier": "WIGOS station identifier",
        "facility_type": "Type of observing facility, fixed land, mobile sea, etc",
        "date_established": "Date host was first established",
        "date_closed": "Date host was first established",
        "wmo_region": "WMO region in which the host is located",
        "territory": "Territory the host is located in",
        "valid_from": "Date from which the details for this record are valid",
        "valid_to": "Date after which the details for this record are no longer valid",
        "version": "Version number of this record",
        "change_date": "Date this record was changed",
        "user_id": "Which user last modified this record",
        "status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc",
        "time_zone_id": "Time zone the host is located in"
    }
    _comment = "wmdr.observing_facility"


@dataclass
class Observer(DomainModelBase):
    id: str
    name: str
    description: str
    links: Optional[dict]
    location: Optional[Geography]
    elevation: Optional[float]
    manufacturer: Optional[str]
    model: Optional[str]
    serial_number: Optional[str]
    firmware_version: Optional[str]
    uncertainty: Optional[str]
    observing_method: Optional[str]
    _comments = {
        "id": "ID / primary key",
        "name": "Name of sensor",
        "description": "Description of sensor",
        "links": "Link(s) to further information",
        "location": "Location of observer",
        "elevation": "Elevation of observer above mean sea level",
        "manufacturer": "Make, or manufacturer, of sensor",
        "model": "Model of sensor",
        "serial_number": "Serial number of sensor",
        "firmware_version": "Firmware version of software installed in sensor",
        "uncertainty": "Standard uncertainty in measurements from sensor",
        "observing_method": "Primary method/principles by which the sensor makes measurements"
    }
    _comment = "wmdr.equipment"


@dataclass
class Collection(DomainModelBase):
    id: str
    name: str
    links: Optional[dict]
    _comments = {
        "id": "ID / primary key",
        "name": "Name of collection",
        "links": "Link(s) to further information on collection"
    }
    _comment = "placeholder"


@dataclass
class Feature(DomainModelBase):
    id: str
    type_id: int
    geometry: Geography
    elevation: Optional[float]
    parent_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    links: Optional[dict]
    _comments = {
        "id": "ID / primary key",
        "type_id": "enumerated feature type",
        "geometry": "",
        "elevation": "Elevation of feature above mean sea level",
        "parent_id": "Parent feature for this feature if nested",
        "name": "Name of feature",
        "description": "Description of feature",
        "links": "Link(s) to further information on feature"
    }
    _comment = "table to contain definition of different geographic features"


@dataclass
class SourceType(DomainModelBase):
    id: str
    description: Optional[str]
    _comments = {
        "id": "ID / primary key",
        "description": "Description of source type, e.g. file etc"
    }
    _comment = "placeholder"


@dataclass
class Source(DomainModelBase):
    id: str
    source_type_id: int
    name: str
    links: Optional[dict]
    processor: Optional[str]
    _comments = {
        "id": "ID / primary key",
        "source_type_id": "The type of source",
        "name": "Name of source",
        "links": "Link(s) to further information on source",
        "processor": "Name of processor used to ingest the data"
    }
    _comment = "placeholder"


@dataclass
class Observation(DomainModelBase):
    id: str
    location: Geography
    elevation: Optional[float]
    observation_type_id: Optional[int]
    phenomenon_start: Optional[datetime]
    phenomenon_end: datetime
    result_value: float
    result_uom: Optional[str]
    result_description: Optional[str]
    result_quality: Optional[dict]
    result_time: Optional[datetime]
    valid_from: Optional[datetime]
    valid_to: Optional[datetime]
    host_id: str
    observer_id: Optional[str]
    observed_property_id: int
    observing_procedure_id: Optional[int]
    report_id: Optional[str]
    collection_id: Optional[str]
    parameter: Optional[dict]
    feature_of_interest_id: Optional[str]
    version: int
    change_date: datetime
    user_id: int
    status_id: int
    comments: str
    source_id: int
    _comments = {
        "id": "ID / primary key",
        "location": "Location of observation",
        "elevation": "Elevation of observation above mean sea level",
        "observation_type_id": "Type of observation",
        "phenomenon_start": "Start time of the phenomenon being observed or observing period, if missing assumed instantaneous with time given by phenomenon_end",
        "phenomenon_end": "End time of the phenomenon being observed or observing period",
        "result_value": "The value of the result in float representation",
        "result_uom": "Units used to represent the value being observed",
        "result_description": "str representation of the result if applicable",
        "result_quality": "JSON representation of the result quality, key / value pairs",
        "result_time": "Time that the result became available",
        "valid_from": "Time that the result starts to be valid",
        "valid_to": "Time after which the result is no longer valid",
        "host_id": "Host associated with making the observation, equivalent to OGC OMS 'host'",
        "observer_id": "Observer associated with making the observation, equivalent to OGC OMS 'observer'",
        "observed_property_id": "The phenomenon, or thing, being observed",
        "observing_procedure_id": "Procedure used to make the observation",
        "report_id": "Parent report ID, used to link coincident observations together",
        "collection_id": "Primary collection or dataset that this observation belongs to",
        "parameter": "List of key/ value pairs in dict",
        "feature_of_interest_id": "Feature that this observation is associated with",
        "version": "Version number of this record",
        "change_date": "Date this record was changed",
        "user_id": "Which user last modified this record",
        "status_id": "Whether this is the latest version or an archived version of the record",
        "comments": "Free text comments on this record, for example description of changes made etc",
        "source_id": "The source of this record"
    }
    _comment = "table to store observations"
