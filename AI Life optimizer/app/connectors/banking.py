"""Banking/financial data connector stub.

Implement integration with financial data aggregators such as Plaid, Yodlee, or other providers.
"""

from typing import Any, Dict, List, Optional


class BankingConnector:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    def get_transactions(self, user_id: int, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        """Fetch transaction data for a user between two dates."""
        # TODO: implement transaction retrieval
        return []

    def sync_transactions(self, user_id: int) -> None:
        """Sync the latest transactions into the system."""
        print(f"[BankingConnector] Sync transactions for user_id={user_id}")
