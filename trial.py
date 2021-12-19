# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('SID')
auth_token = os.getenv('Auth')
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations \
                     .create(friendly_name='My First Conversation')

print(conversation.sid)