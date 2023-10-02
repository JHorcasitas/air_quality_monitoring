from typing import List
from pydantic import BaseModel


class Location(BaseModel):
    type: str
    coordinates: List[float]  # [longitude, latitude]


class Pollution(BaseModel):
    ts: str  # Timestamp
    aqius: int
    mainus: str
    aqicn: int
    maincn: str


class Weather(BaseModel):
    ts: str  # Timestamp
    tp: int  # Temperature
    pr: int  # Pressure
    hu: int  # Humidity
    ws: float  # Wind Speed
    wd: int  # Wind Direction
    ic: str  # Weather Icon


class Current(BaseModel):
    pollution: Pollution
    weather: Weather


class AirQualityInfo(BaseModel):
    city: str
    state: str
    country: str
    location: Location
    current: Current
