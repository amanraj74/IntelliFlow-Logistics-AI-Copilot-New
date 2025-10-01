@echo off
echo ===================================================
echo    IntelliFlow Logistics - Hackathon Startup
echo ===================================================
echo.

echo Creating necessary directories...
mkdir data\streams 2>nul
mkdir data\processed 2>nul
mkdir logs 2>nul

echo.
echo Starting Pathway components in separate windows...

echo.
echo 1. Starting Pathway Live RAG Pipeline...
start "Pathway Live RAG Pipeline" cmd /k "python -m backend.pathway.live_rag_pipeline"

echo.
echo 2. Starting Pathway MCP Server...
start "Pathway MCP Server" cmd /k "python -m backend.mcp.pathway_mcp_server"

echo.
echo 3. Starting FastAPI Backend...
start "FastAPI Backend" cmd /k "uvicorn backend.api.main:app --reload --port 8000"

echo.
echo 4. Starting Streamlit Frontend...
start "Streamlit Frontend" cmd /k "streamlit run app.py"

echo.
echo ===================================================
echo    System startup complete!
echo.
echo    Access points:
echo    - Streamlit UI: http://localhost:8501
echo    - API Endpoint: http://localhost:8000
echo    - Pathway RAG: http://localhost:8765
echo    - MCP Server: http://localhost:8123
echo ===================================================
echo.
echo Press any key to exit this window...
pause > nul