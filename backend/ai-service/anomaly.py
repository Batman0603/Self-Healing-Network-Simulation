from sklearn.ensemble import IsolationForest
import numpy as np

# 🔹 store history
history_store = {}

# 🔹 ML model (global)
model = IsolationForest(contamination=0.2)

# 🔹 initial training data (normal values)
initial_data = np.array([[0.9], [0.8], [0.85], [0.7], [0.75]])
model.fit(initial_data)


def detect_anomaly(node_data):
    try:
        node = node_data.get("node")
        health = node_data.get("health", 1)

        if node not in history_store:
            history_store[node] = []

        history = history_store[node]

        # store history
        history.append(health)
        if len(history) > 5:
            history.pop(0)

        # ✅ RULE 1: threshold
        if health < 0.3:
            return True

        # ✅ RULE 2: sudden drop
        if len(history) >= 2 and (history[-2] - health) > 0.3:
            return True

        # ✅ RULE 3: continuous drop
        if len(history) >= 3 and history[-1] < history[-2] < history[-3]:
            return True

        # 🔥 ML PART (Isolation Forest)
        prediction = model.predict([[health]])

        if prediction[0] == -1:
            return True

        return False

    except Exception as e:
        print("[ANOMALY ERROR]", e)
        return False