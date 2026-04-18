import httpx
from config import PROTOCOL_URL

async def send_data(client, data):
    try:
        # Reuse the existing client to benefit from connection pooling
        resp = await client.post(PROTOCOL_URL, json=data, timeout=2.0)
        if resp.status_code != 200:
            print(f"[PUBLISH WARNING] Protocol service returned {resp.status_code}")
            
    except Exception as e:
        print(f"[PUBLISH ERROR] Could not reach {PROTOCOL_URL}: {e}")