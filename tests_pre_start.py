import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.core.config import settings
from app.db.init_db import init_db
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 3  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        # Try to create session to check if DB is awake
        db = SessionLocal()
        print(settings)
        init_db(db)
        db.commit()
        # create some sample data
        db.execute("INSERT INTO country VALUES ('UG', 'Uganda', '256')")
        db.execute("INSERT INTO broker VALUES ('B01', 'Test Broker', true, 'ABCD')")
        db.execute("INSERT INTO bank VALUES ('BNK01', 'Bank 01', 'UG')")
        db.execute(
            "INSERT INTO branch (bank_id, code, name) VALUES ('BNK01', 'BR01', 'Branch 01')"
        )
        db.commit()
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
