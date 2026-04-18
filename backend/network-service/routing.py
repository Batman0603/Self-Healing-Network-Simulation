import networkx as nx

def get_best_path(G, src, dst):
    if src not in G.nodes or dst not in G.nodes:
        raise ValueError("Invalid source or destination")

    try:
        return nx.shortest_path(G, source=src, target=dst, weight="weight")

    except nx.NetworkXNoPath:
        raise ValueError("No path available")

    except Exception:
        raise Exception("Routing failure")