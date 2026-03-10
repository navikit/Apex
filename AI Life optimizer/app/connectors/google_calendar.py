"""Google Calendar connector stub.

Implement OAuth2 and calendar event ingestion.
"""

from typing import Any, Dict, List, Optional


class GoogleCalendarConnector:
    def __init__(self, api_key: str | None = None, client_id: str | None = None, client_secret: str | None = None):
        self.api_key = api_key
        self.client_id = client_id
        self.client_secret = client_secret

    def list_events(self, calendar_id: str = "primary", time_min: str | None = None, time_max: str | None = None) -> List[Dict[str, Any]]:
        """List calendar events for the authenticated user."""
        # TODO: implement Google Calendar API integration
        return []

    def sync_events(self, user_id: int) -> None:
        """Sync events into the system for a given user."""
        # TODO: map events to internal models and store via ingestion pipeline
        print(f"[GoogleCalendarConnector] Sync events for user_id={user_id}")
