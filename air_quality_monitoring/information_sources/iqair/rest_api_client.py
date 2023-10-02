import os

import requests
import sentry_sdk
from loguru import logger

from information_sources.iqair import AirQualityInfo


class IQAirClient:
    BASE_URL = "https://api.airvisual.com"

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def get_specific_city_data(self, city: str) -> AirQualityInfo:
        url = (
            IQAirClient.BASE_URL
            + f"/v2/city?city={city}&state=Mexico "
            f"City&country=Mexico&key={self._api_key}"
        )

        try:
            response = requests.get(url, timeout=30)
        except Exception as e:
            logger.exception(e)
            raise e
        return AirQualityInfo(**response.json()["data"])
