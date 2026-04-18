import asyncio
import json
import logging
import redis.asyncio as redis

logger = logging.getLogger(__name__)

class RedisBus:
    def __init__(self, url: str = "redis://redis:6379"):
        self.url = url
        self.client = None
        self.subscriptions = {}

    async def connect(self):
        self.client = redis.from_url(self.url)

    async def publish(self, channel: str, data: dict):
        try:
            if not self.client:
                await self.connect()
            await self.client.publish(channel, json.dumps(data))
        except Exception as e:
            logger.error(f"[RedisBus] Publish error on {channel}: {e}")

    async def subscribe(self, channel: str, handler):
        try:
            if not self.client:
                await self.connect()
            pubsub = self.client.pubsub()
            await pubsub.subscribe(channel)
            logger.info(f"[RedisBus] Subscribed to {channel}")
            asyncio.create_task(self._listen(pubsub, handler))
        except Exception as e:
            logger.error(f"[RedisBus] Subscribe error on {channel}: {e}")

    async def _listen(self, pubsub, handler):
        async for message in pubsub.listen():
            if message["type"] == "message":
                try:
                    data = json.loads(message["data"])
                    await handler(data)
                except Exception as e:
                    logger.error(f"[RedisBus] Handler error: {e}")