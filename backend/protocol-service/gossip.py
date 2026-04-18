import asyncio
import random
import time

# Each node maintains its own view of the entire network's state.
# node_views['N0'] is N0's knowledge of all other nodes.
node_views = {}

def initialize_nodes():
    # Each node starts only knowing about itself.
    for i in range(5):
        node_id = f"N{i}"
        node_views[node_id] = {
            node_id: {
                "health": round(random.uniform(0.7, 1.0), 2),
                "status": "alive",
                "version": 0,
                "last_updated": time.time()
            }
        }

def merge_views(local_view, remote_view):
    # Merge the remote view into the local view.
    new_view = local_view.copy()
    for node_id, remote_node_state in remote_view.items():
        local_node_state = new_view.get(node_id)

        # If we don't know about this node, or the remote state is newer, update our view.
        if not local_node_state or remote_node_state['version'] > local_node_state['version']:
            new_view[node_id] = remote_node_state
    return new_view

async def gossip_exchange(node_a, node_b):
    try:
        view_a = node_views.get(node_a, {})
        view_b = node_views.get(node_b, {})

        # Exchange and merge views
        new_view_for_a = merge_views(view_a, view_b)
        new_view_for_b = merge_views(view_b, view_a)

        node_views[node_a] = new_view_for_a
        node_views[node_b] = new_view_for_b

    except Exception as e:
        print(f"[GOSSIP ERROR] between {node_a} and {node_b}: {e}")

async def run_gossip():
    initialize_nodes()

    while True:
        try:
            nodes = list(node_views.keys())

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