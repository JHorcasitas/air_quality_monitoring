import os

import sentry_sdk
from loguru import logger
from dotenv import load_dotenv

from information_sources.iqair import IQAirClient
from pub_sub_adapters import GCPPubSub


if __name__ == "__main__":
    # Load env variables
    load_dotenv()

    # Setup sentry-sdk
    sentry_sdk.init(dsn=os.environ["SENTRY_DSN"])

    # Setup logging
    logger.add(
        os.path.join(os.environ["LOG_DIR"], "air_quality_monitoring.log"),
        format="[{time}][{level}] {message}",
        level="DEBUG",
        mode="a",
        rotation="1 month",  # Rotate every month
        retention=4,  # Keep the last 4 log files
    )
    logger.info(f"Starting execution of iqair_poll_cron_job")

    # Poll IQAIR API
    responses = []
    cities = [
        "Alvaro Obregon",
        "Magdalena Contreras",
        "Mexico City",
        "Tlalpan",
    ]
    for city in cities:
        r = IQAirClient(
            api_key=os.environ["IQAIR_API_KEY"]
        ).get_specific_city_data(city)
        responses.append(r)

    # Publish message to pub/sub
    for r in responses:
        GCPPubSub().publish_message(
            data=r.model_dump_json(),
            metadata=None,
            project_id=os.environ["GCP_PROJECT_ID"],
            topic_id=os.environ["GCP_TOPIC_ID"],
        )

    # TODO: Trigger dataflow pipeline
