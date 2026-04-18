def make_decision(node_data, prediction, score):
    try:
        status = node_data.get("status")

        if status == "down":
            return "reroute"

        if prediction == "high_risk":
            return "reroute"

        if score < 40:
            return "alert"

        if prediction == "medium_risk":
            return "monitor"

        return "normal"

    except Exception as e:
        print("[DECISION ERROR]", e)
        return "unknown"