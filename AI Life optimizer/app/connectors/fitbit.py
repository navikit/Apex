"""Fitbit connector stub.

Implement OAuth2 and fitness data ingestion.
"""

from typing import Any, Dict, List, Optional


class FitbitConnector:
    def __init__(self, client_id: str | None = None, client_secret: str | None = None):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_activity_data(self, user_id: int, date: str) -> Dict[str, Any]:
        """Retrieve activity summary for a given date."""
        # TODO: implement Fitbit API requests
        return {}

    def sync_daily(self, user_id: int) -> None:
        """Sync today's fitness data into the system."""
        # TODO: map Fitbit activity data into stored metrics
        print(f"[FitbitConnector] Sync daily data for user_id={user_id}")
