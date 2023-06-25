from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client()
    def send_sms(self, message):
        self.message = self.client.messages.create(body=message, from_="+12176263597", to="+358406832703")
        print(self.message.status)
