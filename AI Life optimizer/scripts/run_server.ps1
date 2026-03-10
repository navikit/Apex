# Run the FastAPI server for AI Life Optimizer.

$env:DOTENV = ".env"

Write-Host "Starting FastAPI server on http://localhost:8000"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
