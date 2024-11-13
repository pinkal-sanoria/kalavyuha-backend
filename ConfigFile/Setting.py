import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access variables for Send Msg on Phone
ACCOUNT_SID = os.getenv("AccountSid")
AUTHTOKEN  = os.getenv("AuthToken")
