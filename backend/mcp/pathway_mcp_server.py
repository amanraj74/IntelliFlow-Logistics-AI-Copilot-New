import pathway as pw
from pathway.xpacks.llm.mcp_server import McpServable, McpServer, PathwayMcp
import json
import os
import glob
from datetime import datetime

class LogisticsMCPServer(McpServable):
    """Pathway MCP Server for Logistics Intelligence"""
    
    def __init__(self):
        self.live_data = {}
        self.load_live_streams()
    
    def load_live_streams(self):
        """Load live streaming data from all available streams"""
        try:
            # Load drivers data
            drivers_data = []
            for file_path in glob.glob('data/streams/drivers*.json'):
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            drivers_data.extend(data)
                        else:
                            drivers_data.append(data)
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
            self.live_data['drivers'] = drivers_data
            
            # Load shipments data
            shipments_data = []
            for file_path in glob.glob('data/streams/shipments*.json'):
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            shipments_data.extend(data)
                        else:
                            shipments_data.append(data)
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
            self.live_data['shipments'] = shipments_data
            
            # Load invoices data
            invoices_data = []
            for file_path in glob.glob('data/streams/invoices*.json'):
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            invoices_data.extend(data)
                        else:
                            invoices_data.append(data)
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
            self.live_data['invoices'] = invoices_data
            
            print(f"✅ Loaded {len(drivers_data)} drivers, {len(shipments_data)} shipments, {len(invoices_data)} invoices")
        except Exception as e:
            print(f"Error loading streams: {e}")
            # Initialize with empty data if loading fails
            self.live_data = {'drivers': [], 'shipments': [], 'invoices': []}
    
    def get_driver_safety_analysis(self, query_table: pw.Table) -> pw.Table:
        """MCP Tool: Real-time driver safety analysis"""
        self.load_live_streams()  # Always fresh data
        
        high_risk_drivers = [
            d for d in self.live_data.get('drivers', []) 
            if isinstance(d, dict) and d.get('safety_score', 10) < 8.0
        ]
        
        result = {
            "analysis_type": "driver_safety",
            "timestamp": datetime.now().isoformat(),
            "high_risk_count": len(high_risk_drivers),
            "high_risk_drivers": high_risk_drivers,
            "live_update": "✅ Data refreshed in real-time"
        }
        
        return query_table.select(mcp_response=json.dumps(result))
    
    def get_live_logistics_data(self, query_table: pw.Table) -> pw.Table:
        """MCP Tool: Get live logistics data"""
        self.load_live_streams()  # Fresh data every call
        
        result = {
            "data_sources": list(self.live_data.keys()),
            "total_drivers": len(self.live_data.get('drivers', [])),
            "total_shipments": len(self.live_data.get('shipments', [])),
            "total_invoices": len(self.live_data.get('invoices', [])),
            "last_update": datetime.now().isoformat(),
            "live_streaming": "✅ Active"
        }
        
        return query_table.select(mcp_response=json.dumps(result))
    
    def detect_anomalies(self, query_table: pw.Table) -> pw.Table:
        """MCP Tool: Detect anomalies in shipments"""
        self.load_live_streams()  # Fresh data every call
        
        # Detect route deviations and value anomalies
        anomalies = []
        for shipment in self.live_data.get('shipments', []):
            if isinstance(shipment, dict):
                if shipment.get('deviation', 0) > 20:
                    anomalies.append({
                        "shipment_id": shipment.get('shipment_id', 'unknown'),
                        "anomaly_type": "route_deviation",
                        "severity": "high",
                        "details": f"Route deviation of {shipment.get('deviation')} km detected"
                    })
        
        result = {
            "analysis_type": "anomaly_detection",
            "timestamp": datetime.now().isoformat(),
            "anomaly_count": len(anomalies),
            "anomalies": anomalies,
            "live_update": "✅ Data refreshed in real-time"
        }
        
        return query_table.select(mcp_response=json.dumps(result))
    
    def register_mcp(self, server: McpServer):
        """Register MCP tools with the server"""
        
        class EmptySchema(pw.Schema):
            pass
        
        server.tool(
            "get_driver_safety_analysis",
            request_handler=self.get_driver_safety_analysis,
            schema=EmptySchema
        )
        
        server.tool(
            "get_live_logistics_data", 
            request_handler=self.get_live_logistics_data,
            schema=EmptySchema
        )
        
        server.tool(
            "detect_anomalies",
            request_handler=self.detect_anomalies,
            schema=EmptySchema
        )

def start_mcp_server():
    """Start the Pathway MCP Server"""
    print("🔥 Starting Pathway MCP Server...")
    
    # Ensure data directories exist
    os.makedirs('data/streams', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    logistics_tools = LogisticsMCPServer()
    
    try:
        pathway_mcp_server = PathwayMcp(
            name="IntelliFlow Logistics MCP Server",
            transport="streamable-http",
            host="0.0.0.0",
            port=8123,
            serve=[logistics_tools]
        )
        
        print("✅ MCP Server running on port 8123")
        pw.run()
    except Exception as e:
        print(f"⚠️ Error starting MCP server: {e}")
        print("🔄 Attempting to restart with different configuration...")
        # Fallback configuration
        pathway_mcp_server = PathwayMcp(
            name="IntelliFlow Logistics MCP Server",
            transport="streamable-http",
            host="localhost",
            port=8123,
            serve=[logistics_tools]
        )
        
        print("✅ MCP Server running on port 8123 (localhost)")
        pw.run()

if __name__ == "__main__":
    start_mcp_server()
