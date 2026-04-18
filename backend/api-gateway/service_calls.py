import requests

NETWORK_SERVICE_URL = "http://localhost:8001"

def fetch_route(src, dst):
    try:
        response = requests.get(
            f"{NETWORK_SERVICE_URL}/route",
            params={"src": src, "dst": dst},
            timeout=2
        )

        if response.status_code == 200:
            return response.json()

        return fallback_response("Network service returned error")

    except requests.exceptions.Timeout:
        return fallback_response("Network service timeout")

    except requests.exceptions.ConnectionError:
        return fallback_response("Network service unavailable")

    except Exception:
        return fallback_response("Unknown error")

def fallback_response(message):
    return {
        "success": False,
        "path": [],
        "message": message
    }