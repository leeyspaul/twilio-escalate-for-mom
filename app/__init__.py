import json

from twilio.rest import Client

# Helpers
def _get_json_credentials(creds_path):
    creds_dict = None

    with open(creds_path) as creds_file:
        creds_dict = json.loads(creds_file.read())

    return creds_dict


def _get_twilio_credentials(creds_path):
    creds = _get_json_credentials(creds_path)

    return (creds['ACCOUNT_SID'], creds['AUTH_TOKEN'])


def get_twilio_client(twilio_creds_path):
    # setup twilio creds
    ACCOUNT_SID, AUTH_TOKEN = _get_twilio_credentials(twilio_creds_path)

    # get twilio client
    return Client(ACCOUNT_SID, AUTH_TOKEN)
