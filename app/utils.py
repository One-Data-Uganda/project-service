import json
import logging

import nsq.client
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.core.config import settings
from app.core.logger import log

# Disable verbose logging from nsq library
logging.getLogger("nsq").setLevel(logging.WARNING)


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(1),
    before=before_log(log, logging.INFO),
    after=after_log(log, logging.WARN),
)
def postToNSQ(channel: str, payload: str):
    nsqClient = nsq.client.Client()

    conn = nsqClient.connect(settings.NSQD_HOST, settings.NSQD_PORT)

    nsq_message = str.encode(json.dumps(payload))

    if conn:
        nsqClient.pub(str.encode(channel), nsq_message)
