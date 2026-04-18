from shared.logger import get_logger

logger = get_logger("state")

# Global node state
node_state = {}

def update_node(node, data):
    try:
        node_state[node] = data
        logger.info(f"Updated state: {node} → {data}")
    except Exception as e:
        logger.error(f"[STATE UPDATE ERROR] {e}")

def get_node(node):
    return node_state.get(node, {})

def get_all_nodes():
    return node_state

def clear_state():
    global node_state
    node_state = {}