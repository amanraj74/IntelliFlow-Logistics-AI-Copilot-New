import pathway as pw
from pathway.xpacks.llm import embedders, llms, parsers
from pathway.xpacks.llm.vector_store import VectorStoreServer
import os
from datetime import datetime

class LiveLogisticsRAG:
    def __init__(self):
        self.setup_real_pathway_rag()
    
    def setup_real_pathway_rag(self):
        """Setup genuine Pathway real-time RAG system"""
        print("🔥 Starting REAL Pathway Live RAG System...")
        
        # Define schema for logistics data
        class LogisticsSchema(pw.Schema):
            content: str
            driver_id: str = pw.column_definition(default_value="")
            safety_score: float = pw.column_definition(default_value=0.0)
            timestamp: str = pw.column_definition(default_value="")
        
        # Real-time data ingestion from folder
        self.data = pw.io.fs.read(
            "./data/streams",
            format="json",
            mode="streaming",
            schema=LogisticsSchema,
            autocommit_duration_ms=500  # Ultra-fast updates
        )
        
        # Parse and prepare documents for RAG
        self.documents = self.data.select(
            text=pw.this.content,
            metadata=pw.this.driver_id + " | Score: " + pw.this.safety_score.as_str()
        )
        
        # Real-time embeddings with sentence transformers
        self.embedder = embedders.SentenceTransformerEmbedder(
            model="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        # Create live vector store (NO REBUILDS!)
        self.vector_server = VectorStoreServer(
            self.documents,
            embedder=self.embedder,
            parser=parsers.ParseUnstructured()
        )
        
        print("✅ Real-time RAG system initialized!")
        print("📡 Live indexing active - updates in real-time!")
    
    def run_rag_server(self):
        """Start the live RAG server"""
        print("🚀 Starting Pathway RAG Server...")
        pw.run(
            monitoring_level=pw.MonitoringLevel.NONE,
            with_http_server=True,
            host="0.0.0.0",
            port=8765
        )

if __name__ == "__main__":
    rag_system = LiveLogisticsRAG()
    rag_system.run_rag_server()
