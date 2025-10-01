import json
import os
import time
import random
from datetime import datetime

def generate_live_driver_data():
    """Generate live driver data for real-time demo"""
    
    os.makedirs('./data/streams/drivers', exist_ok=True)
    
    drivers = [
        {"driver_id": "D-001", "name": "John Smith", "safety_score": 9.2, "incidents": 0},
        {"driver_id": "D-002", "name": "Maria Garcia", "safety_score": 7.8, "incidents": 1},
        {"driver_id": "D-003", "name": "David Chen", "safety_score": 8.5, "incidents": 0},
    ]
    
    while True:
        # Simulate real-time updates
        for driver in drivers:
            # Random safety score changes
            driver["safety_score"] += random.uniform(-0.3, 0.2)
            driver["safety_score"] = max(1.0, min(10.0, driver["safety_score"]))
            driver["timestamp"] = datetime.now().isoformat()
            
            # Write individual files (triggers Pathway streaming)
            filename = f"./data/streams/drivers/driver_{driver['driver_id']}.json"
            with open(filename, 'w') as f:
                json.dump({
                    "content": f"Driver {driver['name']} safety analysis",
                    "driver_id": driver["driver_id"],
                    "safety_score": driver["safety_score"],
                    "timestamp": driver["timestamp"]
                }, f)
        
        print(f"✅ Live data updated at {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(10)  # Update every 10 seconds

if __name__ == "__main__":
    generate_live_driver_data()
