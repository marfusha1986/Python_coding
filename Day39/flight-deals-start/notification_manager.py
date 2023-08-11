from twilio.rest import Client

TWILIO_SID = 'AC96ff8f1e4119a93e0b9f1473ba29abe4'
TWILIO_AUTH_TOKEN = '10663249385fb8e2c301c0d38f5414a7'
TWILIO_VIRTUAL_NUMBER = '+12187182869'
TWILIO_VERIFIED_NUMBER = '+905366458227'


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID,TWILIO_AUTH_TOKEN)

    def send_sms(self,message):
        message = self.client.messages.create(
            body = message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)
