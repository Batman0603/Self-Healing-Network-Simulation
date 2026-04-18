import random

nodes = {}

def sync_nodes(node_list):
    if not node_list:
        return

    # 1. Remove nodes that no longer exist in the network service
    nodes_to_remove = [node for node in nodes if node not in node_list]
    for node in nodes_to_remove:
        del nodes[node]

    # 2. Add new nodes that aren't in simulation yet
    for node in node_list:
        if node not in nodes:
            nodes[node] = {
                "health": round(random.uniform(0.7, 1.0), 2),
                "status": "alive"
            }

def update_nodes():
    try:
        if not nodes:
            return {}

        for node in nodes:
            # Balanced fluctuation (-0.05 to +0.05) to prevent immediate death
            change = random.uniform(-0.05, 0.05)
            nodes[node]["health"] = round(nodes[node]["health"] + change, 2)
            
            # Simple self-healing: if a node is down, give it a 20% chance to recover slightly
            if nodes[node]["status"] == "down" and random.random() > 0.8:
                nodes[node]["health"] = 0.25

            nodes[node]["health"] = max(0, min(1, nodes[node]["health"]))

            # failure condition
            if nodes[node]["health"] < 0.2:
                nodes[node]["status"] = "down"
            else:
                nodes[node]["status"] = "alive"

        return nodes

    except Exception as e:
        print("[NODE ERROR]", e)
        return nodes