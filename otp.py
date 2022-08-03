from twilio.rest import Client
import random
import math

randit = str(math.floor(random.random() * 7652196 + 1))
value = int(randit[0:5])
otp = value


def send_token(account_sid, auth_token, sender_number, receiver_number):
    client = Client(account_sid, auth_token)
    msg = """\
    To reset your hyper account, please use the following OTP:

    {0}
    """.format(
        otp
    )

    message = client.messages.create(body=msg, from_=sender_number, to=receiver_number)
    return "hello"
