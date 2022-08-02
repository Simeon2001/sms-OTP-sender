from twilio.rest import Client 
import random
import math

randit = str(math.floor(random.random() * 7652196 + 1))
value = int(randit[0:5])
otp = value

def send_token(sender_number,receiver_number):
    msg = """\
    hello {0},
    To reset your hyper account, please use the following OTP:

    {1}
    """.format(otp)

    return "hello"

