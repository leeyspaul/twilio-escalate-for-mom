from app import get_twilio_client
from app.config import FROM_NUMBER
from app.config import ONCALL
from app.config import TO_NUMBER
from app.config import TWILIO_CREDS_PATH
from app.config import MOMS_NUMBER
from app.escalate import TwilioEscalate


if __name__ == '__main__':
    # get client
    twilio_client = get_twilio_client(
        TWILIO_CREDS_PATH
    )

    # run the feature!
    twilio_escalate = TwilioEscalate(
        twilio_client, ONCALL, FROM_NUMBER, TO_NUMBER, MOMS_NUMBER
    )
    
    # example negative sentiment message for demo purposes
    twilio_escalate.ping('hey, you forgot to clean your room, get back home and clean your room! I am not happy with you.')
    twilio_escalate.console_mom_ping()