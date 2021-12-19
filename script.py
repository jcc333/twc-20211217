# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv 

#Load environmental variables
load_dotenv() 

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('SID')
auth_token = os.getenv('Auth')
client = Client(account_sid, auth_token)

#Ability to change message 
message = client.messages \
                .create(
                     body="Hi, this is a test",
                     from_='+13306484254',
                     to='+19152675166'
                 )

conversation = client.conversations \
    .conversations \
    .create(
         messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
         friendly_name='Friendly Conversation'
     )

print(message.sid)