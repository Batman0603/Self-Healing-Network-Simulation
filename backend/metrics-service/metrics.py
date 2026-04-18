from threading import Lock

metrics_data = {
    "total_nodes": 0,
    "active_nodes": 0,
    "failed_nodes": 0,
    "last_updated": None
}

lock = Lock()

def update_metrics(data):
    try:
        with lock:
            metrics_data.update(data)
    except Exception as e:
        print("[METRICS UPDATE ERROR]", e)

def get_metrics():
    try:
        with lock:
            return metrics_data
    except Exception as e:
        print("[METRICS FETCH ERROR]", e)
        return {}