import asyncio
import random
import time
from gossip import node_views

async def run_heartbeat():
    while True:
        try:
            nodes = list(node_views.keys())

            if not nodes:
                await asyncio.sleep(2)
                continue

            # Pick a random node to simulate a state change on
            node_to_update = random.choice(nodes)

            # A node can only update its own state. We access it via its view of itself.
            current_self_state = node_views[node_to_update][node_to_update]

            # Simulate a failure event
            if random.random() < 0.2:
                current_self_state["status"] = "down"
                current_self_state["health"] = max(0.0, current_self_state["health"] - 0.4)
                current_self_state["version"] += 1
                current_self_state["last_updated"] = time.time()

                print(f"[FAILURE] {node_to_update} DOWN")

        except Exception as e:
            print("[HEARTBEAT ERROR]", e)

        await asyncio.sleep(5) # Wait 5 seconds before the next potential failure