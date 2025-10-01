import pandas as pd
import json
import os
import time
from datetime import datetime
import threading

class PathwaySimulator:
    """Simulates Pathway real-time data processing for the hackathon"""
    
    def __init__(self):
        self.data_streams = {
            'drivers': [],
            'invoices': [],
            'shipments': []
        }
        self.is_streaming = False
        self.setup_sample_data()
    
    def setup_sample_data(self):
        """Setup sample streaming data"""
        os.makedirs('data/streams', exist_ok=True)
        
        # Create sample CSV files that will be "updated" in real-time
        drivers_data = [
            {"driver_id": "D-001", "name": "John Smith", "safety_score": 9.2, "incidents": 0, "last_update": datetime.now().isoformat()},
            {"driver_id": "D-002", "name": "Maria Garcia", "safety_score": 7.1, "incidents": 3, "last_update": datetime.now().isoformat()},
            {"driver_id": "D-003", "name": "David Chen", "safety_score": 8.8, "incidents": 1, "last_update": datetime.now().isoformat()},
        ]
        
        invoices_data = [
            {"invoice_id": "INV-001", "amount": 12500, "due_date": "2025-10-05", "status": "Pending"},
            {"invoice_id": "INV-002", "amount": 8300, "due_date": "2025-09-28", "status": "Overdue"},
        ]
        
        shipments_data = [
            {"shipment_id": "SH-001", "route": "Delhi-Mumbai", "value": 125000, "status": "In Transit", "deviation": 0},
            {"shipment_id": "SH-002", "route": "Bangalore-Chennai", "value": 89000, "status": "Anomaly Detected", "deviation": 45},
        ]
        
        # Save to JSON files (simulating real-time data streams)
        with open('data/streams/drivers.json', 'w') as f:
            json.dump(drivers_data, f, indent=2)
        
        with open('data/streams/invoices.json', 'w') as f:
            json.dump(invoices_data, f, indent=2)
            
        with open('data/streams/shipments.json', 'w') as f:  
            json.dump(shipments_data, f, indent=2)
    
    def start_streaming(self):
        """Start simulated real-time data streaming"""
        self.is_streaming = True
        thread = threading.Thread(target=self._stream_updates)
        thread.daemon = True
        thread.start()
        return "✅ Real-time streaming started!"
    
    def _stream_updates(self):
        """Simulate real-time data updates"""
        import random
        
        while self.is_streaming:
            time.sleep(10)  # Update every 10 seconds
            
            # Update driver safety scores randomly
            drivers_file = 'data/streams/drivers.json'
            if os.path.exists(drivers_file):
                with open(drivers_file, 'r') as f:
                    drivers = json.load(f)
                
                for driver in drivers:
                    # Simulate small changes in safety scores
                    change = random.uniform(-0.1, 0.1)
                    driver['safety_score'] = max(0, min(10, driver['safety_score'] + change))
                    driver['last_update'] = datetime.now().isoformat()
                
                with open(drivers_file, 'w') as f:
                    json.dump(drivers, f, indent=2)
    
    def get_live_data(self, data_type):
        """Get live data from streams"""
        file_path = f'data/streams/{data_type}.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return []
    
    def update_data(self, data_type, new_data):
        """Update data stream (simulating real-time changes)"""
        file_path = f'data/streams/{data_type}.json'
        current_data = self.get_live_data(data_type)
        current_data.append(new_data)
        
        with open(file_path, 'w') as f:
            json.dump(current_data, f, indent=2)
        
        return f"✅ {data_type} data updated in real-time!"

# Global instance
pathway_simulator = PathwaySimulator()
