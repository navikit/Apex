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

### 4) Run the FastAPI backend + website

```powershell
uvicorn app.main:app --reload --port 8000
```

Then open:
- Website UI: http://localhost:8000/
- API docs: http://localhost:8000/docs

> The root URL serves a minimal web UI that talks to the API to create users, log metrics, and display recommendations.

### 5) (Optional) Run the Streamlit dashboard

```powershell
streamlit run streamlit_app.py
```

---

## 🛠️ Project Structure

- `app/` - backend services, API routes, and ML scaffolding
- `web/` - minimal static website frontend for interacting with the API
- `streamlit_app.py` - dashboard prototype
- `requirements.txt` - Python dependencies
- `config.py` - configuration and environment helpers
- `README.md` - this document

---

## 🧩 Extending the Project

To complete the vision described in the prompt, add or extend these scaffolds:

- **Data collectors / connectors** for external APIs (Google Calendar, Fitbit, banking, etc.)
  - See `app/connectors/` for stub connector classes.
- **Continuous ingestion pipeline** (scheduler/cron) that pulls new data regularly
  - See `app/ingestion.py` for a scheduled ingestion scaffold.
- **ML models** that learn from past history and generate predictions
  - See `app/services/ml_models.py` for a starter regression analysis.
- **Recommendation engine** (LLM + rule engine) for generating schedules and plan updates
  - See `app/recommendations.py` for a basic placeholder.
- **Notifications / habit-tracking** to keep users on track
  - See `app/notifications.py` for notification hooks and habit plan scaffolding.
- **Subscription & SaaS features** (tiers, billing, premium analytics)
  - See `app/subscriptions.py` for a stubbed tier system.

---

## 📄 License

MIT
