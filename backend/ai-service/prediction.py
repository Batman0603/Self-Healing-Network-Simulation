def predict_failure(node_data):
    try:
        health = node_data.get("health", 1)

        if health < 0.3:
            return "high_risk"
        elif health < 0.6:
            return "medium_risk"
        return "low_risk"

    except Exception as e:
        print("[PREDICTION ERROR]", e)
        return "unknown"