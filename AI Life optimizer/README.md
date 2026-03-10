# AI Life Optimizer

**AI Life Optimizer** is a scaffold for an intelligent personal operating system that continuously analyzes and improves a user’s daily life decisions using data, predictive modeling, and behavioral analysis.

> This repo is a starting point. It includes a basic FastAPI backend, a local SQLite store, and a Streamlit dashboard skeleton. Expand the connectors, ML models, and decision logic to meet your needs.

---

## 🧰 Features (scaffold)

- FastAPI backend for data ingestion and recommendations
- SQLite database via SQLAlchemy for storing behavioral history
- Placeholder integration points for:
  - Calendar + task managers (Google Calendar, Todo apps)
  - Fitness & sleep trackers (Fitbit, Apple Health)
  - Financial spending data
- ML/analysis pipeline scaffold using pandas / NumPy / scikit-learn
- Streamlit dashboard scaffold for visualization

---

## 🚀 Getting Started

### 1) Create a Python virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```powershell
pip install -r requirements.txt
```

### 3) Configure environment variables

Copy the example `.env.example` to `.env` and fill in any API keys / settings required.

```powershell
copy .env.example .env
```

### 4) Run the FastAPI backend

```powershell
uvicorn app.main:app --reload --port 8000
```

Then open:
- API docs: http://localhost:8000/docs

### 5) Run the dashboard (Streamlit)

```powershell
streamlit run streamlit_app.py
```

---

## 🛠️ Project Structure

- `app/` - backend services, API routes, and ML scaffolding
- `streamlit_app.py` - dashboard prototype
- `requirements.txt` - Python dependencies
- `config.py` - configuration and environment helpers
- `README.md` - this document

---

## 🧩 Extending the Project

To complete the vision described in the prompt, add:

- Data collectors / connectors for external APIs (Google Calendar, Fitbit, banking, etc.)
- Continuous ingestion pipeline (scheduler/cron)
- ML models that learn from past history and generate predictions
- Recommendation engine (LLM + rule engine) for generating schedules and plan updates
- Notifications / habit-tracking
- Subscription & SaaS features

---

## 📄 License

MIT
