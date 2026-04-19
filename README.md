# Self-Healing Network Simulation

A distributed system simulation demonstrating a resilient network architecture. The project features automated fault detection and recovery using a decentralized Gossip protocol and AI-driven health analysis.

## System Architecture

The simulation is composed of several specialized microservices:

- **API Gateway**: Orchestrates communication between the frontend and internal services.
- **Protocol Service**: Manages network state consensus using a Gossip protocol and Heartbeat monitoring.
- **AI Service**: Uses machine learning to detect anomalies and predict node failures before they occur.
- **Network Service**: Handles graph topology, pathfinding, and dynamic rerouting logic.
- **Simulation Service**: Generates synthetic node metrics and failure events to test system resilience.
- **Metrics Service**: Aggregates health data for real-time monitoring.
- **Websocket Service**: Provides live state updates to the dashboard.

## Key Features

- **Decentralized State**: Nodes share health information via Gossip, ensuring no single point of failure for network visibility.
- **AI-Driven Healing**: The AI service identifies "high-risk" nodes and triggers proactive rerouting to maintain uptime.
- **Real-Time Visualization**: A React-based dashboard to monitor network health and automated recovery actions.

## Project Structure

```text
backend/
├── api-gateway/       # FastAPI routing and orchestration
├── ai-service/        # Anomaly detection and failure prediction
├── protocol-service/  # Gossip protocol and health consensus
├── network-service/   # Graph management and routing
├── simulation-service/# Synthetic data generation
├── metrics-service/   # Data collection and aggregation
└── shared/            # Common schemas and models
frontend/              # React + Vite visualization dashboard
```

## Getting Started

### Backend Services
For each service in the `backend/` directory, install the required dependencies:
```bash
pip install -r requirements.txt
```

### Frontend Dashboard
Navigate to the frontend directory and start the development server:
```bash
cd frontend
npm install
npm run dev
```

## Requirements
- Python 3.9+
- Node.js 18+