import nexmo
import conf
from utilities.logger import get_logger
from utilities.exceptions import SMSSendError
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
    if res['status'] != '0':
        raise SMSSendError(res['error-text'])
