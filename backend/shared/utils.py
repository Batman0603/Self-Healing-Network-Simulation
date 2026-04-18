import httpx
from shared.constants import REQUEST_TIMEOUT
from shared.logger import get_logger

logger = get_logger("utils")

async def safe_post(client: httpx.AsyncClient, url: str, data: dict):
    try:
        response = await client.post(url, json=data, timeout=REQUEST_TIMEOUT)
        return response.json()
    except httpx.TimeoutException:
        logger.error(f"[TIMEOUT] {url}")
        return {"success": False, "error": "timeout"}
    except httpx.ConnectError:
        logger.error(f"[CONNECTION ERROR] {url}")
        return {"success": False, "error": "connection failed"}
    except Exception as e:
        logger.error(f"[HTTP ERROR] {url}: {e}")
        return {"success": False, "error": str(e)}