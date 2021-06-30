import os

# CREDENTIALS CONFIG
TWILIO_CREDS_FILE_NAME = 'twilio_creds.json'
TWILIO_CREDS_PATH = f'{os.path.abspath(os.path.dirname(__file__))}/{TWILIO_CREDS_FILE_NAME}' # hacky way to find your rel path from execution point

# ONCALL CONFIG
ONCALL = 'YOUR_NAME'
FROM_NUMBER = 'TWILIO_TRIAL_PHONE_NUMBER'
TO_NUMBER = 'ON_CALL_NUMBER_TO_SEND_TO'
MOMS_NUMBER = 'MOMS_NUMBER'
