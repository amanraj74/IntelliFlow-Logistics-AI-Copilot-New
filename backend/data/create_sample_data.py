import json
import os
from datetime import datetime

def create_perfect_sample_data():
    """Create perfect sample data for streaming"""
    
    os.makedirs('./data/streams', exist_ok=True)
    
    # Perfect driver data structure
    drivers_data = [
        {
            "driver_id": "D-001",
            "name": "John Smith", 
            "safety_score": 9.2,
            "timestamp": datetime.now().isoformat()
        },
        {
            "driver_id": "D-002",
            "name": "Maria Garcia",
            "safety_score": 7.1, 
            "timestamp": datetime.now().isoformat()
        },
        {
            "driver_id": "D-003",
            "name": "David Chen",
            "safety_score": 8.8,
            "timestamp": datetime.now().isoformat()
        }
    ]
    
    # Save to streams folder
    with open('./data/streams/drivers.json', 'w') as f:
        json.dump(drivers_data, f, indent=2)
    
    print("✅ Perfect sample data created!")

if __name__ == "__main__":
    create_perfect_sample_data()
