import os

# Redis Configuration
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# Service URLs (Using Docker Compose service names or localhost for development)
# Updated to match actual docker-compose.yml ports
NETWORK_SERVICE_URL = os.getenv("NETWORK_SERVICE_URL", "http://localhost:8001")
PROTOCOL_SERVICE_URL = os.getenv("PROTOCOL_SERVICE_URL", "http://localhost:8011")
METRICS_SERVICE_URL = os.getenv("METRICS_SERVICE_URL", "http://localhost:8012")
SIMULATION_SERVICE_URL = os.getenv("SIMULATION_SERVICE_URL", "http://localhost:8010")
AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://localhost:8013")
WEBSOCKET_SERVICE_URL = os.getenv("WEBSOCKET_SERVICE_URL", "http://localhost:8002")
API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://localhost:8000")

# Service Names
SERVICE_NAME = os.getenv("SERVICE_NAME", "service")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", "8000"))

# Timeouts & Retries
REQUEST_TIMEOUT = 5
MAX_RETRIES = 3
RETRY_DELAY = 1

# Health Thresholds
HIGH_RISK_THRESHOLD = 0.3
MEDIUM_RISK_THRESHOLD = 0.6

# Simulation Settings
SIMULATION_INTERVAL = 2  # seconds
BATCH_SIZE = 10

# Message Queue Settings
REDIS_ttl_messages = 3600  # 1 hour
REDIS_POLL_TIMEOUT = 0  # Non-blocking
