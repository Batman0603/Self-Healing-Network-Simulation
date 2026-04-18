import sys
from pathlib import Path
import httpx
from config import PROTOCOL_URL

# Add parent directory to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from shared.schemas import NodeData

async def send_data(client, data):
    try:
        # Convert data to list of NodeData
        node_updates = []
        for node, info in data.items():
            node_updates.append(NodeData(node=node, health=info["health"], status=info["status"]))
        
        # Send as list
        resp = await client.post(PROTOCOL_URL, json=[node.dict() for node in node_updates], timeout=2.0)
        if resp.status_code != 200:
            print(f"[PUBLISH WARNING] Protocol service returned {resp.status_code}")
            
    except Exception as e:
        print(f"[PUBLISH ERROR] Could not reach {PROTOCOL_URL}: {e}")