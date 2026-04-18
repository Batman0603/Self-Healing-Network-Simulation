import asyncio
import random
import time

# Each node has its own state + version
node_state = {}

def initialize_nodes():
    for i in range(5):
        node_state[f"N{i}"] = {
            "health": round(random.uniform(0.7, 1.0), 2),
            "status": "alive",
            "version": 0,
            "last_updated": time.time()
        }

def merge_state(local, incoming):
    # keep latest version
    if incoming["version"] > local["version"]:
        return incoming
    return local

async def gossip_exchange(node_a, node_b):
    try:
        state_a = node_state[node_a]
        state_b = node_state[node_b]

        # exchange states
        merged_a = merge_state(state_a, state_b)
        merged_b = merge_state(state_b, state_a)

        node_state[node_a] = merged_a
        node_state[node_b] = merged_b

    except Exception as e:
        print("[GOSSIP ERROR]", e)

async def run_gossip():
    initialize_nodes()

    while True:
        try:
            nodes = list(node_state.keys())

            if len(nodes) < 2:
                await asyncio.sleep(2)
                continue

            # pick two random nodes (peer selection)
            node_a, node_b = random.sample(nodes, 2)

            await gossip_exchange(node_a, node_b)

            print(f"[GOSSIP] {node_a} <-> {node_b}")

        except Exception as e:
            print("[GOSSIP LOOP ERROR]", e)

        await asyncio.sleep(2)