import httpx
import logging

logger = logging.getLogger(__name__)

class ServiceClient:
    @staticmethod
    async def get(url: str, params: dict = None):
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(url, params=params)
                return response.json()
        except Exception as e:
            logger.error(f"[ServiceClient] GET {url} failed: {e}")
            return None

    @staticmethod
    async def post(url: str, json: dict = None):
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.post(url, json=json)
                return response.json()
        except Exception as e:
            logger.error(f"[ServiceClient] POST {url} failed: {e}")
            return None

    @staticmethod
    async def health_check(url: str):
        try:
            async with httpx.AsyncClient(timeout=3.0) as client:
                response = await client.get(f"{url}/health")
                return response.status_code == 200
        except Exception:
            return False
