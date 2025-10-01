FROM pathwaycom/pathway:latest

WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY . .

# Create directories
RUN mkdir -p data/streams data/processed logs

# Create simple startup script with REAL Pathway
RUN echo '#!/bin/bash\n\
echo "🚀 STARTING REAL PATHWAY HACKATHON SYSTEM..."\n\
echo "🔥 Starting Simple Pathway Implementation..."\n\
python backend/pathway/simple_pathway.py &\n\
sleep 5\n\
echo "🤖 Starting FastAPI Backend..."\n\
uvicorn backend.api.live_proof:app --host 0.0.0.0 --port 8000 &\n\
sleep 3\n\
echo "🎯 Starting Streamlit Dashboard..."\n\
streamlit run app.py --server.port 8501 --server.address 0.0.0.0 --server.headless true &\n\
echo "✅ PATHWAY SYSTEM STARTED!"\n\
wait\n\
' > start.sh && chmod +x start.sh

EXPOSE 8000 8501

CMD ["./start.sh"]
