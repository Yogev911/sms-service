import nexmo


def send(src, dest, msg):
    client = nexmo.Client(key='3fdf633b', secret='mVZW9LHrKGS7IFn7')
    res = client.send_message({
        'from': src,
        'to': dest,
        'text': msg,
    }
    )
    print('sms sent!')
    print(src, dest, msg)
    return res
