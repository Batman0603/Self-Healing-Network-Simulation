import asyncio
import httpx
from datetime import datetime
from metrics import update_metrics
from config import API_GATEWAY_URL, COLLECT_INTERVAL

async def collect_metrics():
    async with httpx.AsyncClient() as client:
        while True:
            try:
                # Use async client to prevent blocking the event loop
                response = await client.get(f"{API_GATEWAY_URL}/protocol-state", timeout=2.0)

                if response.status_code == 200:
                    data = response.json()

                    total = len(data)
                    active = sum(1 for n in data.values() if n["status"] == "alive")
                    failed = total - active

                    update_metrics({
                        "total_nodes": total,
                        "active_nodes": active,
                        "failed_nodes": failed,
                        "last_updated": datetime.now().isoformat()
                    })

                    print("[METRICS UPDATED]", total, active, failed)
                else:
                    print(f"[COLLECTOR WARNING] Gateway returned {response.status_code} for /protocol-state")

            except Exception as e:
                print("[COLLECTOR ERROR]", e)

            await asyncio.sleep(COLLECT_INTERVAL)