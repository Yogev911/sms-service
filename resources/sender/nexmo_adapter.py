import nexmo
import conf

def send(src, dest, msg):
    client = nexmo.Client(key=conf.NEXMO_KEY, secret=conf.NEXMO_SECRET)
    res = client.send_message({
        'from': src,
        'to': dest,
        'text': msg,
    }
    )
    print('sms sent!')
    print(src, dest, msg)
    return res
