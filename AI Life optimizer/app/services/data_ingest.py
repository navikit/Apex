"""Data ingestion helpers.

This module is a placeholder for connectors to external sources such as:
- Google Calendar
- Fitbit / Apple Health
- Email and task management systems
- Banking and financial data aggregators

Implement connector classes and schedule periodic polling to ingest new data.
"""

from datetime import datetime
from typing import Any, Dict, Optional


def ingest_calendar_event(user_id: int, event: Dict[str, Any]) -> None:
    """Ingest a calendar event into the system."""
    # TODO: implement connector logic and persist into the database
    print(f"[ingest_calendar_event] user_id={user_id} event={event}")


def ingest_metric(user_id: int, metric_key: str, metric_value: float, recorded_at: Optional[datetime] = None) -> None:
    """Store a rudimentary metric value (e.g., sleep hours, steps, screen-time)."""
    # TODO: implement persistence using app.db.SessionLocal
    print(f"[ingest_metric] user_id={user_id} key={metric_key} value={metric_value} recorded_at={recorded_at}")
