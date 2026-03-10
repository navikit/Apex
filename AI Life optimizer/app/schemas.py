from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str | None = None
    created_at: datetime

    class Config:
        orm_mode = True


class MetricIn(BaseModel):
    metric_key: str
    metric_value: float
    recorded_at: datetime | None = None


class RecommendationOut(BaseModel):
    summary: str
    details: dict
