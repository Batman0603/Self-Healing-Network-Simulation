def calculate_score(node_data):
    try:
        health = node_data.get("health", 1)
        status = node_data.get("status", "alive")

        score = health * 100

        if status == "down":
            score -= 40

        return max(0, round(score, 2))

    except Exception as e:
        print("[SCORING ERROR]", e)
        return 0