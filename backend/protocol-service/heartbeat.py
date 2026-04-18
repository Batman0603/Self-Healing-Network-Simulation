import asyncio
import random
import time
from gossip import node_state

async def run_heartbeat():
    while True:
        try:
            nodes = list(node_state.keys())

            if not nodes:
                await asyncio.sleep(2)
                continue

            node = random.choice(nodes)
            current = node_state[node]

            # simulate failure
            if random.random() < 0.2:
                current["status"] = "down"
                current["health"] = max(0.0, current["health"] - 0.4)
                current["version"] += 1
                current["last_updated"] = time.time()

                print(f"[FAILURE] {node} DOWN")

        except Exception as e:
            print("[HEARTBEAT ERROR]", e)

        await asyncio.sleep(5)