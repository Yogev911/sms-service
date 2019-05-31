import nexmo
import conf
from utilities.logger import get_logger
import json

logger = get_logger(__name__)

client = nexmo.Client(key=conf.NEXMO_KEY, secret=conf.NEXMO_SECRET)


def send(src, dest, msg):
    res = client.send_message({
        'from': src,
        'to': dest,
        'text': msg,
    }
    )
    logger.info(f'SMS sent via NEXMO, {json.dumps(res)}')
    return res
