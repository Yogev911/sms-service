import nexmo
import conf


def send(src, dest, msg):
    # client = nexmo.Client(key=conf.NEXMO_KEY, secret=conf.NEXMO_SECRET)
    # client.send_message({
    #     'from': src,
    #     'to': f'972{dest}',
    #     'text': msg,
    # }
    # )
    print('sms sent!')
