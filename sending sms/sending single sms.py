import os
from keys import VIRTUALNUMBER, AUTHTOKEN, ACCOUNTSID
from twilio.rest import Client


number = "+233557136080"

client = Client(ACCOUNTSID, AUTHTOKEN)


message = client.messages.create(
    from_=VIRTUALNUMBER,
    body="Sunny afternoon,\n"
         "Wake up with determination, Go to bed with satisfaction",
    to=number
)

print(message.sid)

