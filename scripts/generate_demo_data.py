import json
import random
from datetime import datetime, timedelta
import os

def generate_professional_demo_data():
    """Generate 50+ drivers, shipments, invoices for professional demo"""
    
    print("🚀 Generating Professional Demo Data...")
    
    # Ensure directories exist
    os.makedirs('./data/streams', exist_ok=True)
    
    # Generate 50 realistic drivers
    drivers_data = []
    driver_names = [
        "John Smith", "Maria Garcia", "David Chen", "Sarah Johnson", "Mike Wilson",
        "Lisa Anderson", "James Brown", "Jennifer Davis", "Robert Miller", "Jessica Moore",
        "William Taylor", "Ashley Jackson", "Christopher White", "Amanda Harris", "Matthew Martin",
        "Stephanie Thompson", "Joshua Garcia", "Michelle Martinez", "Andrew Robinson", "Nicole Clark",
        "Daniel Rodriguez", "Elizabeth Lewis", "Joseph Lee", "Kimberly Walker", "Mark Hall",
        "Linda Allen", "Paul Young", "Karen Hernandez", "Steven King", "Betty Wright",
        "Edward Lopez", "Helen Hill", "Brian Scott", "Susan Green", "Ronald Adams",
        "Donna Baker", "Anthony Gonzalez", "Carol Nelson", "Kevin Carter", "Ruth Mitchell",
        "Jason Perez", "Sharon Roberts", "Ryan Turner", "Laura Phillips", "Gary Campbell",
        "Cynthia Parker", "Nicholas Evans", "Amy Edwards", "Eric Collins", "Deborah Stewart"
    ]
    
    cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Hyderabad", "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Surat"]
    
    for i in range(50):
        safety_score = round(random.uniform(4.5, 9.8), 1)
        incidents = random.choices([0, 1, 2, 3, 4, 5], weights=[40, 25, 15, 10, 7, 3])[0]
        
        driver = {
            "driver_id": f"D-{str(i+1).zfill(3)}",
            "name": driver_names[i],
            "safety_score": safety_score,
            "incidents": incidents,
            "experience_years": random.randint(1, 15),
            "home_city": random.choice(cities),
            "vehicle_type": random.choice(["Truck", "Van", "Heavy Truck", "Container"]),
            "license_class": random.choice(["CDL-A", "CDL-B", "Commercial"]),
            "status": "high_risk" if safety_score < 6.5 else "active",
            "last_violation": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat(),
            "rating": round(safety_score + random.uniform(-0.5, 0.5), 1),
            "timestamp": datetime.now().isoformat()
        }
        drivers_data.append(driver)
    
    # Save drivers data
    with open('./data/streams/drivers_comprehensive.json', 'w') as f:
        json.dump(drivers_data, f, indent=2)
    
    print(f"✅ Generated {len(drivers_data)} professional drivers")
    
    # Generate 30 shipments
    shipments_data = []
    routes = [
        "Mumbai-Delhi", "Delhi-Bangalore", "Chennai-Hyderabad", "Pune-Mumbai", "Kolkata-Delhi",
        "Ahmedabad-Mumbai", "Jaipur-Delhi", "Surat-Pune", "Hyderabad-Chennai", "Bangalore-Mumbai"
    ]
    
    cargo_types = ["Electronics", "Pharmaceuticals", "Textiles", "Automotive Parts", "Food Items", 
                   "Chemicals", "Construction Materials", "Consumer Goods", "Raw Materials", "Machinery"]
    
    for i in range(30):
        value = random.randint(50000, 500000)
        deviation = random.choice([0, 0, 0, 15, 25, 45, 60])  # Most normal, few anomalies
        
        shipment = {
            "shipment_id": f"SH-{str(i+1).zfill(4)}",
            "route": random.choice(routes),
            "cargo_type": random.choice(cargo_types),
            "value": value,
            "weight_kg": random.randint(1000, 10000),
            "status": "anomaly_detected" if deviation > 30 else "in_transit",
            "deviation_km": deviation,
            "driver_assigned": f"D-{str(random.randint(1, 50)).zfill(3)}",
            "expected_delivery": (datetime.now() + timedelta(days=random.randint(1, 7))).isoformat(),
            "risk_level": "high" if deviation > 30 or value > 300000 else "normal",
            "gps_tracking": True,
            "insurance_covered": value * random.uniform(1.1, 1.5),
            "timestamp": datetime.now().isoformat()
        }
        shipments_data.append(shipment)
    
    # Save shipments data
    with open('./data/streams/shipments_comprehensive.json', 'w') as f:
        json.dump(shipments_data, f, indent=2)
    
    print(f"✅ Generated {len(shipments_data)} professional shipments")
    
    # Generate 25 invoices
    invoices_data = []
    companies = ["TechCorp Ltd", "Global Logistics", "Prime Industries", "Metro Transport", "Swift Cargo",
                 "Elite Shipping", "Express Delivery", "Reliable Transport", "Quick Move Logistics", "Fast Track"]
    
    for i in range(25):
        amount = random.randint(10000, 150000)
        days_until_due = random.randint(-10, 30)  # Some overdue, some upcoming
        due_date = datetime.now() + timedelta(days=days_until_due)
        
        status = "overdue" if days_until_due < 0 else "pending" if days_until_due < 7 else "scheduled"
        
        invoice = {
            "invoice_id": f"INV-{str(i+1).zfill(4)}",
            "company": random.choice(companies),
            "amount": amount,
            "due_date": due_date.isoformat(),
            "issue_date": (datetime.now() - timedelta(days=random.randint(1, 45))).isoformat(),
            "status": status,
            "payment_terms": random.choice(["Net 30", "Net 15", "Due on Receipt", "Net 45"]),
            "discount_available": amount * 0.02 if days_until_due > 10 else 0,
            "late_fee": amount * 0.05 if status == "overdue" else 0,
            "service_type": random.choice(["Full Truckload", "LTL", "Express", "Standard"]),
            "compliance_score": random.randint(75, 100),
            "timestamp": datetime.now().isoformat()
        }
        invoices_data.append(invoice)
    
    # Save invoices data
    with open('./data/streams/invoices_comprehensive.json', 'w') as f:
        json.dump(invoices_data, f, indent=2)
    
    print(f"✅ Generated {len(invoices_data)} professional invoices")
    
    # Generate fleet optimization data
    fleet_data = []
    for i in range(15):
        fleet = {
            "vehicle_id": f"VH-{str(i+1).zfill(3)}",
            "type": random.choice(["Heavy Truck", "Medium Truck", "Van", "Container Truck"]),
            "fuel_efficiency": round(random.uniform(6.5, 12.5), 1),
            "maintenance_due": random.choice([True, False]),
            "location": random.choice(cities),
            "utilization_rate": random.randint(65, 95),
            "monthly_costs": random.randint(25000, 75000),
            "driver_assigned": f"D-{str(random.randint(1, 50)).zfill(3)}",
            "last_service": (datetime.now() - timedelta(days=random.randint(1, 90))).isoformat(),
            "timestamp": datetime.now().isoformat()
        }
        fleet_data.append(fleet)
    
    # Save fleet data
    with open('./data/streams/fleet_optimization.json', 'w') as f:
        json.dump(fleet_data, f, indent=2)
    
    print(f"✅ Generated {len(fleet_data)} fleet vehicles")
    
    # Generate summary statistics
    summary = {
        "generation_date": datetime.now().isoformat(),
        "total_drivers": len(drivers_data),
        "high_risk_drivers": len([d for d in drivers_data if d['safety_score'] < 6.5]),
        "total_shipments": len(shipments_data),
        "anomaly_shipments": len([s for s in shipments_data if s['deviation_km'] > 30]),
        "total_invoices": len(invoices_data),
        "overdue_invoices": len([i for i in invoices_data if i['status'] == 'overdue']),
        "fleet_vehicles": len(fleet_data),
        "total_records": len(drivers_data) + len(shipments_data) + len(invoices_data) + len(fleet_data)
    }
    
    with open('./data/streams/system_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    print("\n🏆 PROFESSIONAL DEMO DATA GENERATED:")
    print(f"  📊 {summary['total_drivers']} Drivers ({summary['high_risk_drivers']} high-risk)")
    print(f"  📦 {summary['total_shipments']} Shipments ({summary['anomaly_shipments']} anomalies)")
    print(f"  💰 {summary['total_invoices']} Invoices ({summary['overdue_invoices']} overdue)")
    print(f"  🚛 {summary['fleet_vehicles']} Fleet Vehicles")
    print(f"  📈 Total Records: {summary['total_records']}")
    print("\n✅ Ready for professional hackathon demo!")

if __name__ == "__main__":
    generate_professional_demo_data()
