import asyncio
import sys
from pathlib import Path
import logging

sys.path.insert(0, str(Path(__file__).parent.parent))
from shared.redis_bus import RedisBus
from anomaly import detect_anomalies
from decision import make_decision
from publisher import publish_result

logger = logging.getLogger(__name__)

async def analyze_node_data(data):
    try:
        if not isinstance(data, dict) or 'nodes' not in data:
            logger.warning(f"[AI ANALYZER] Invalid data format: {data}")
            return
        nodes = data['nodes']
        anomalies = detect_anomalies(nodes)
        for anomaly in anomalies:
            decision = make_decision(anomaly, None, None)
            if decision:
                await publish_result({"node": anomaly.get("node"), "decision": decision})
    except Exception as e:
        logger.error(f"[AI ANALYZER] Error: {e}")

async def start_analyzer():
    bus = RedisBus()
    await bus.subscribe("node-data", analyze_node_data)
    logger.info("[AI ANALYZER] Started listening for node-data events")
    while True:
        await asyncio.sleep(1)