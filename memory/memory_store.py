import json
from datetime import datetime
import os

LOG_DIR = "memory/logs"
os.makedirs(LOG_DIR, exist_ok=True)

def store_memory(agent_name: str, input_text: str, output_text: str):
    filename = os.path.join(LOG_DIR, f"{agent_name}.json")
    
    default_data = [{
        "timestamp": datetime.now().isoformat(),
        "input": "Initial memory setup.",
        "response": "Hello Shraddha. I'm here to walk gently beside you."
    }]

    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            data = json.loads(content) if content else default_data
    except (FileNotFoundError, json.JSONDecodeError):
        data = default_data

    data.append({
        "timestamp": datetime.now().isoformat(),
        "input": input_text,
        "response": output_text
    })

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)