# Download the helper library from https://www.twilio.com/docs/python/install
import os
import random

from twilio.rest import Client
from dotenv import load_dotenv 

#Load environmental variables
load_dotenv() 

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('SID')
auth_token = os.getenv('Auth')
client = Client(account_sid, auth_token)

def randomPregnancyIntro():
    message = ['Hello! I think I am pregnant']
    return (random.choice(message))


#Ability to change message 
message = client.messages \
                .create(
                     body=randomPregnancyIntro(),
                     from_='+13306484254',
                     to='+19152675166'
                 )



print(message.sid)