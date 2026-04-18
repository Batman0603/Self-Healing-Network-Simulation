from state import graph

def add_node(node: str):
    if not graph.has_node(node):
        graph.add_node(node)

def add_edge(src: str, dst: str, weight: float):
    if not graph.has_node(src) or not graph.has_node(dst):
        raise ValueError(f"Cannot create edge: One or both nodes ('{src}', '{dst}') do not exist.")
    graph.add_edge(src, dst, weight=weight)

def get_graph():
    return graph