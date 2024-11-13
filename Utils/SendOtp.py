
import os
import sys
# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ConfigFile.Setting import ACCOUNT_SID,AUTHTOKEN
from twilio.rest import Client

#just work for verifed number on my account in free version
def sendOtpOnMobileNumber(otp:int, UserContact:int):

    accountSid = ACCOUNT_SID
    authToken = AUTHTOKEN

    print(accountSid,authToken)
    client = Client(accountSid, authToken)

    # Highlight OTP with symbols
    message_body = f"Dear User,\n\nYour One-Time Password (OTP) is: {otp}.\nPlease do not share this code with anyone.\n\nThank you for choosing us!\n\nRegards,\nKalaVayhu Team"

    client.messages.create(
    from_='+18508101810', 
    body=message_body,
    to='+917837110083'
    )

