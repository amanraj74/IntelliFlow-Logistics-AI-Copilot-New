import pathway as pw
import json
from datetime import datetime

class RealTimeProcessor:
    def __init__(self):
        self.setup_streaming_pipeline()
    
    def setup_streaming_pipeline(self):
        """Setup real Pathway streaming ETL pipeline"""
        print("🔥 Real Pathway Streaming ETL Starting...")
        
        # Define logistics data schema
        class DriverDataSchema(pw.Schema):
            driver_id: str
            name: str
            safety_score: float
            incidents: int
            timestamp: str
        
        # Stream from JSON files
        self.driver_stream = pw.io.fs.read(
            "./data/streams/drivers",
            format="json", 
            mode="streaming",
            schema=DriverDataSchema
        )
        
        # Real-time processing transformations
        self.processed_drivers = self.driver_stream.select(
            pw.this.driver_id,
            pw.this.name,
            pw.this.safety_score,
            risk_level=pw.if_else(
                pw.this.safety_score < 7.0,
                "HIGH_RISK",
                "NORMAL"
            ),
            processed_at=datetime.now().isoformat()
        )
        
        # Output to processed folder (live updates)
        pw.io.fs.write(
            self.processed_drivers,
            pw.io.fs.write.JsonFormatter(),
            "./data/processed/live_drivers.json"
        )
        
        print("✅ Streaming ETL pipeline ready!")
    
    def start_processing(self):
        """Start real-time processing"""
        print("🚀 Starting Pathway computation engine...")
        pw.run()

if __name__ == "__main__":
    processor = RealTimeProcessor()
    processor.start_processing()
