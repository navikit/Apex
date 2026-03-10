from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import db
from app.models import User, UserMetric
from app.schemas import MetricIn, RecommendationOut, UserCreate, UserOut
from app.services import data_ingest, ml_models


router = APIRouter(prefix="/api", tags=["ai-life-optimize"])


def get_db():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


@router.post("/users", response_model=UserOut)
def create_user(user: UserCreate, session: Session = Depends(get_db)):
    existing = session.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    record = User(email=user.email, full_name=user.full_name)
    session.add(record)
    session.commit()
    session.refresh(record)
    return record


@router.post("/users/{user_id}/metrics")
async def add_user_metric(user_id: int, metric: MetricIn, session: Session = Depends(get_db)):
    user = session.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # persist metric
    record = UserMetric(
        user_id=user_id,
        metric_key=metric.metric_key,
        metric_value=metric.metric_value,
        recorded_at=metric.recorded_at,
    )
    session.add(record)
    session.commit()
    session.refresh(record)

    # placeholder for a more complete ingestion pipeline
    data_ingest.ingest_metric(user_id, metric.metric_key, metric.metric_value, metric.recorded_at)

    return {"status": "accepted"}


@router.get("/users/{user_id}/recommendations", response_model=RecommendationOut)
async def get_recommendations(user_id: int, session: Session = Depends(get_db)):
    user = session.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # load latest metrics
    metrics = (
        session.query(UserMetric)
        .filter(UserMetric.user_id == user_id)
        .order_by(UserMetric.recorded_at.desc())
        .limit(30)
        .all()
    )

    # convert to pandas for quick analysis
    import pandas as pd

    df = pd.DataFrame(
        [
            {"recorded_at": m.recorded_at, "metric_value": m.metric_value}
            for m in metrics
        ]
    )

    trend = ml_models.estimate_productivity_trend(df)

    return {
        "summary": "Recommendation engine is not yet configured.",
        "details": {
            "trend": trend,
            "next_steps": [
                "Connect external data sources (calendar, sleep, finance).",
                "Train custom ML models for personalized insights.",
                "Implement an LLM-backed reasoning engine.",
            ],
        },
    }
