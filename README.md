# escalate

escalate is a demo app built to send a text through Twilio SMS Python based on a text sentiment score given some piece of text (e.g. text, Whatsapp, email, Slack).

It utilizes a flag that when toggled to `True` the Twilio SMS feature will have a higher sensitivity to the text. If toggled to `False`, the Twilio SMS feature will have a lower sensitivity.

## Feature overview

The `ping` functionality depends on the feature flag to be toggled `True` or `False`. 

When `True` the text sensitivty will be raised higher (the range is between -1.0 and 1.0). With the higher sensitivity, it will trigger a Twilio SMS based on text that are not outright "angry" or "sad". 

When `False` the text sensitivity will be lowered and the Twilio SMS trigger will on send on text that are directly "angry" or "sad". 

## Instructions

The instructions here assume you have a Twilio account to get the respective `ACCOUNT_SID`, `ACCOUNT_TOKEN`, and trial phone number.

1. Set your credentials in a separate JSON file called `twilio_creds.json`. You can optionally pass them in directly by modifying the code in `__init__.py`

2. Set your on-call config values in `config.py`

3. Start a `venv` with `python3 -m venv twilio-escalate`

4. Install requirements with `pip3 install -r requirements.txt`

5. Run the demo code in `run.py` with `python3 run.py` or optionally set this up as a cronjob somewhere and pass in the args. :]
