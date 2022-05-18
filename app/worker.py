import json
from contextlib import contextmanager
from datetime import datetime, timedelta

import redis
from celery.schedules import crontab
from sqlalchemy.dialects.postgresql import insert

from app.core.celery_app import celery_app
from app.core.config import settings
from app.db.session import SessionLocal
from app.external_apis import FeedWebService
from app.logger import log

redisConn = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()
