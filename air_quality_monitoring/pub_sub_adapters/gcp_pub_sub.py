from typing import Dict
from concurrent.futures import Future

from loguru import logger
from google.cloud import pubsub_v1


class GCPPubSub:
    def __init__(self) -> None:
        self._client = pubsub_v1.PublisherClient()

    def publish_message(
        self,
        data: str,
        metadata: Dict[str, str] | None,
        project_id: str,
        topic_id: str,
    ) -> int:
        """Publish a message to the given topic.

        :param data: Message data to publish.
        :param metadata: Message metadata to publish.
        :param project_id: Project id where the topic exists.
        :param topic_id: Topic to publish the message.
        :return: The message id of the message published.
        """
        metadata = metadata or {}
        topic_path = self._client.topic_path(project_id, topic_id)
        future: Future = self._client.publish(
            topic_path, data.encode("utf-8"), **metadata
        )
        try:
            return future.result(timeout=5)
        except Exception as e:
            logger.exception(e)
            raise e
