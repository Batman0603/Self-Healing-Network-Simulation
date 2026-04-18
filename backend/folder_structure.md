backend/
│
├── api-gateway/
│   ├── main.py
│   ├── routes.py
│   ├── service_calls.py
│   ├── health.py              # 🔥 health check
│   ├── .env
│
├── network-service/
│   ├── main.py
│   ├── graph.py
│   ├── routing.py             # shortest + backup + failover
│   ├── health.py
│   ├── .env
│
├── simulation-service/
│   ├── main.py
│   ├── packet.py
│   ├── simulator.py
│   ├── publisher.py
│   ├── health.py
│   ├── .env
│
├── protocol-service/
│   ├── main.py
│   ├── gossip.py
│   ├── heartbeat.py
│   ├── publisher.py
│   ├── health.py
│   ├── .env
│
├── ai-service/
│   ├── main.py
│   ├── anomaly.py
│   ├── prediction.py
│   ├── scoring.py
│   ├── decision.py
│   ├── publisher.py
│   ├── health.py
│   ├── .env
│
├── websocket-service/
│   ├── main.py
│   ├── socket_handler.py
│   ├── manager.py
│   ├── health.py
│   ├── .env
│
├── metrics-service/            # 🔥 NEW
│   ├── main.py
│   ├── collector.py           # collects from services
│   ├── aggregator.py          # latency avg, drop rate
│   ├── health.py
│   ├── .env
│
├── shared/
│   ├── schemas.py
│   ├── utils.py
│   ├── state.py
│   ├── constants.py
│   ├── logger.py              # 🔥 centralized logging
│
├── config/
│   ├── settings.py
│   ├── service_urls.py
│
├── docker-compose.yml
└── README.md