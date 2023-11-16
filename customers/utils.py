import random
from django.conf import settings
from twilio.rest import Client


def generate_otp(length=4):
    otp = ''.join(random.choice('0123456789') for _ in range(length))
    return otp


def send_otp(phone_number, otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Your verification code is: {otp}',
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
