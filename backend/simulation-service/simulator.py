import asyncio
import httpx
from shared.models.network_event import NetworkEvent
from node_manager import sync_nodes, update_nodes
from publisher import send_data
from config import INTERVAL, NETWORK_NODES_URL

async def run_simulation():
    async with httpx.AsyncClient() as client:
        try:
            while True:
                # 1. Fetch current nodes from Network Service
                try:
                    resp = await client.get(NETWORK_NODES_URL, timeout=2.0)
                    if resp.status_code == 200:
                        node_list = resp.json().get("nodes", [])
                        sync_nodes(node_list)
                    else:
                        print(f"[SIMULATOR SYNC ERROR] Received status {resp.status_code} from {NETWORK_NODES_URL}")
                        
                except Exception as e:
                    print(f"[SIMULATOR SYNC ERROR] Failed to connect to {NETWORK_NODES_URL}: {e}")

                data = update_nodes()
                if not data:
                    print("[SIMULATION] Idle - No nodes found. Waiting for Network Service...")
                else:
                    # Check for failed nodes to trigger events
                    for node_id, node_info in data.items():
                        if node_info["status"] == "down":
                            event = NetworkEvent(node_id=node_id, status="DOWN")
                            # Logic to publish 'event' can be added here

                    print(f"[SIMULATION] Running - Active nodes: {len(data)}")
                    await send_data(client, data)

                await asyncio.sleep(INTERVAL)

        except Exception as e:
            print("[SIMULATOR ERROR]", e)