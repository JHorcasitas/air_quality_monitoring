# Air Quality Monitoring

## Setup
    python -m pip install -r requirements.txt

Define the following variables in a `.env` file inside the `air_quality_monitoring` directory. This should follow the [python-dotenv](https://pypi.org/project/python-dotenv/) syntax.

- `SENTRY_DSN`: Sentry DSN to use for error reporting.
- `LOG_DIR`: Directory to create log file.
- `IQAIR_API_KEY`: API key of the IQAir air quality API.
- `GCP_PROJECT_ID`: GCP project where the pub/sub service to be used lives.
- `GCP_TOPIC_ID`: Pub/sub topic to publish messages to.

## Cron job configuration
