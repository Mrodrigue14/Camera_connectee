import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

def sends_sms(action):
    numbers_to_message = [## Add the phone numbers you want to message here]
    for number in numbers_to_message:
        if action == "human":
            message = client.messages.create(
            body="Une personne est entrée dans la classe!",
            from_="+12028837248",
            to=number)
        elif action == "sabotage":
            message = client.messages.create(
            body="Votre caméra a été saboté!",
            from_="+12028837248",
            to=number)
    print(message.body)