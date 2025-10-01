import pathway as pw
from pathway.xpacks.llm import embedders, llms, parsers
from pathway.xpacks.llm.vector_store import VectorStoreServer
import os
import json
from datetime import datetime

class LiveRAGPipeline:
    def __init__(self):
        self.setup_live_indexing()
    
    def setup_live_indexing(self):
        """Setup REAL-TIME Pathway indexing pipeline"""
        print("🔥 Starting REAL Pathway Live RAG Pipeline...")
        
        # Define schema for JSON data
        class LogisticsSchema(pw.Schema):
            data: str
        
        # 1. REAL-TIME DATA INGESTION from streams folder
        self.data_source = pw.io.fs.read(
            "./data/streams",
            format="json",
            mode="streaming",
            schema=LogisticsSchema,
            with_metadata=True,
            autocommit_duration_ms=50  # Ultra-fast updates
        )
        
        # 2. LIVE DATA PARSING 
        self.parsed_data = self.data_source.select(
            text=pw.this.data,
            metadata=pw.this._metadata,
            source_path=pw.this._metadata.path
        )
        
        # 3. REAL-TIME EMBEDDING (Dynamic Indexing)
        self.embedder = embedders.SentenceTransformerEmbedder(
            model="sentence-transformers/all-MiniLM-L6-v2",
            device="cpu"  # Ensure it works without GPU
        )
        
        self.embedded_data = self.parsed_data.select(
            text=pw.this.text,
            vector=self.embedder.apply(text=pw.this.text),
            metadata=pw.this.metadata,
            source=pw.this.source_path,
            timestamp=pw.now()
        )
        
        # 4. LIVE VECTOR STORE (No Rebuilds!)
        self.vector_server = VectorStoreServer(
            self.embedded_data,
            embedder=self.embedder,
            parser=parsers.ParseUnstructured(),
            enable_feedback=True
        )
        
        # 5. Write processed data to output for API consumption
        pw.io.fs.write(
            self.embedded_data,
            pw.io.fs.write.JsonFormatter(),
            "./data/processed/"
        )
        
        print("✅ Live RAG Pipeline initialized!")
        print("📡 Real-time indexing active - NO REBUILDS NEEDED!")
        
    def start_live_processing(self):
        """Start the live processing engine"""
        print("🚀 Starting Live Pathway Computation...")
        # This runs the real-time pipeline
        try:
            pw.run(
                monitoring_level=pw.MonitoringLevel.NONE,
                with_http_server=True,
                host="0.0.0.0",
                port=8765
            )
        except Exception as e:
            print(f"⚠️ Error starting Pathway server: {e}")
            print("🔄 Attempting to restart with different configuration...")
            # Fallback configuration
            pw.run(
                monitoring_level=pw.MonitoringLevel.NONE,
                with_http_server=True,
                host="localhost",
                port=8765
            )

if __name__ == "__main__":
    pipeline = LiveRAGPipeline()
    pipeline.start_live_processing()
