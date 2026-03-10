"""Ingestion pipeline and scheduling.

This module provides a lightweight scheduler to orchestrate periodic data ingestion
from external connectors.
"""

from datetime import datetime
from typing import Callable, Optional

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from app.connectors import GoogleCalendarConnector, FitbitConnector, BankingConnector


class IngestionScheduler:
    def __init__(
        self,
        calendar: GoogleCalendarConnector,
        fitbit: FitbitConnector,
        banking: BankingConnector,
    ):
        self.calendar = calendar
        self.fitbit = fitbit
        self.banking = banking
        self._scheduler: Optional[BackgroundScheduler] = None

    def start(self):
        if self._scheduler is not None:
            return

        scheduler = BackgroundScheduler()
        scheduler.add_job(self._sync_calendar, IntervalTrigger(minutes=30), id="sync_calendar")
        scheduler.add_job(self._sync_fitness, IntervalTrigger(minutes=60), id="sync_fitness")
        scheduler.add_job(self._sync_bank, IntervalTrigger(hours=6), id="sync_bank")

        scheduler.start()
        self._scheduler = scheduler

    def stop(self):
        if self._scheduler is not None:
            self._scheduler.shutdown()
            self._scheduler = None

    def _sync_calendar(self):
        # TODO: determine which user IDs to sync
        print(f"[{datetime.utcnow()}] Running calendar sync")

    def _sync_fitness(self):
        print(f"[{datetime.utcnow()}] Running fitness sync")

    def _sync_bank(self):
        print(f"[{datetime.utcnow()}] Running banking sync")


_scheduler: Optional[IngestionScheduler] = None


def get_scheduler(
    calendar: GoogleCalendarConnector,
    fitbit: FitbitConnector,
    banking: BankingConnector,
) -> IngestionScheduler:
    global _scheduler
    if _scheduler is None:
        _scheduler = IngestionScheduler(calendar=calendar, fitbit=fitbit, banking=banking)
    return _scheduler
