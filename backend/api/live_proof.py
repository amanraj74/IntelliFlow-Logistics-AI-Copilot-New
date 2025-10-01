from fastapi import FastAPI, HTTPException
import json
import os
from datetime import datetime
import glob

app = FastAPI(title="IntelliFlow: LIVE DATA PROOF")

@app.get("/")
async def root():
    return {
        "message": "🏆 IntelliFlow: LIVE DATA PROOF SYSTEM",
        "current_time": datetime.now().isoformat(),
        "pathway_status": "MONITORING FILES IN REAL-TIME"
    }

@app.get("/current-drivers")
async def get_current_drivers():
    """Show CURRENT state of drivers - this will change!"""
    
    try:
        # Read ALL files from streams folder (what Pathway monitors)
        driver_files = glob.glob('./data/streams/*.json')
        all_drivers = []
        
        for file_path in driver_files:
            try:
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_drivers.extend(data)
                    elif isinstance(data, dict) and 'driver_id' in data:
                        all_drivers.append(data)
            except:
                continue
        
        # Show LIVE data state
        high_risk = [d for d in all_drivers if d.get('safety_score', 10) < 7.0]
        
        return {
            "live_timestamp": datetime.now().isoformat(),
            "total_drivers": len(all_drivers),
            "high_risk_drivers": len(high_risk),
            "high_risk_details": high_risk,
            "data_source": "LIVE FILES - Pathway monitoring",
            "files_read": len(driver_files),
            "proof": "This data changes when files change!"
        }
        
    except Exception as e:
        return {"error": str(e), "status": "checking files..."}

@app.post("/add-emergency-driver")
async def add_emergency_driver():
    """Add NEW emergency driver - Pathway will detect this!"""
    
    timestamp = datetime.now().strftime('%H%M%S')
    emergency_driver = {
        "driver_id": f"D-EMERGENCY-{timestamp}",
        "name": f"Emergency Driver {timestamp}",
        "safety_score": 1.5,  # VERY HIGH RISK
        "status": "EMERGENCY - IMMEDIATE ACTION REQUIRED",
        "incidents": 5,
        "timestamp": datetime.now().isoformat(),
        "emergency_type": "CRITICAL SAFETY VIOLATION"
    }
    
    # Write to file (Pathway will detect this change!)
    filename = f"./data/streams/emergency_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(emergency_driver, f, indent=2)
    
    return {
        "message": "🚨 EMERGENCY DRIVER ADDED TO LIVE STREAM",
        "driver": emergency_driver,
        "file_created": filename,
        "pathway_action": "Pathway will detect this file immediately!",
        "test_instruction": "Now call /current-drivers to see the change!"
    }

@app.get("/live-query/{question}")
async def live_query(question: str):
    """Answer questions using LIVE data from files"""
    
    # Read current live data
    driver_files = glob.glob('./data/streams/*.json')
    all_drivers = []
    
    for file_path in driver_files:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                if isinstance(data, list):
                    all_drivers.extend(data)
                elif isinstance(data, dict) and 'driver_id' in data:
                    all_drivers.append(data)
        except:
            continue
    
    # Generate response based on CURRENT data
    if "emergency" in question.lower() or "critical" in question.lower():
        emergency_drivers = [d for d in all_drivers if d.get('safety_score', 10) < 2.0]
        response = f"""
🚨 EMERGENCY ANALYSIS - Live Data at {datetime.now().strftime('%H:%M:%S')}

Critical Drivers Found: {len(emergency_drivers)}
        """
        for driver in emergency_drivers:
            response += f"""
- {driver.get('driver_id', 'Unknown')}: Score {driver.get('safety_score', 'N/A')} 
  Status: {driver.get('status', 'Unknown')}
  Action: {driver.get('emergency_type', 'Review required')}
            """
    else:
        high_risk = [d for d in all_drivers if d.get('safety_score', 10) < 7.0]
        response = f"""
📊 LIVE DRIVER ANALYSIS at {datetime.now().strftime('%H:%M:%S')}

Total Drivers: {len(all_drivers)}
High Risk Drivers: {len(high_risk)}
Data Source: {len(driver_files)} live files
        """
    
    return {
        "question": question,
        "live_response": response,
        "data_timestamp": datetime.now().isoformat(),
        "files_processed": len(driver_files),
        "proof": "This answer changes when data files change!"
    }
