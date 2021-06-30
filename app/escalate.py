import logging

from textblob import TextBlob

logging.basicConfig()
logging.root.setLevel(logging.INFO)  # demo purposes to see all info logs
logger = logging.getLogger()


class TwilioEscalate:
    """This class utilizes the global Twilio Client."""

    def __init__(
        self,
        twilio_client,
        oncall,
        from_number,
        to_number,
        moms_number,
    ):
        """Constructs a new TwilioEscalate instance.

        :param TwilioClient twilio_client: Twilio client.
        :param string oncall: name of the oncall.
        :param string from_number: number of the Twilio app.
        :param string to_number: number of the oncall to ping.
        :param string moms_number: moms number to ping.
        """
        self.twilio_client = twilio_client
        self.oncall = oncall
        self.from_number = from_number
        self.to_number = to_number
        self.moms_number = moms_number

    def ping(self, text):
        """Pings a user with the corresponding text.

        :param string text: text submitted by the user.
        """
        lower_threshold_escalation_feature = True # optional: substitute with feature flag service

        logger.info(
            'lower threshold feature is %s',
            lower_threshold_escalation_feature,
        )

        if lower_threshold_escalation_feature:
            self._lower_threshold_escalation_ping(text)
            return

        self._higher_threshold_escalation_ping(text)
    
    def console_mom_ping(self):
        """Send mom a consoling text."""
        self._send_mom_text(self.moms_number)

    def _calculate_escalation_score(self, text):
        """Calculates a polarity score based on the given text.

        :param string text: text submitted by the user.
        """
        blob = TextBlob(text)

        text_polarity_scores = []

        for sentence in blob.sentences:
            text_polarity_scores.append(sentence.sentiment.polarity)

        avg_polarity_score = (
            sum(text_polarity_scores) /
            len(text_polarity_scores)
        )

        logger.info('text sentiment score: %s', avg_polarity_score)

        return avg_polarity_score

    def _send_escalation_text(self, to_number):
        """Pings a phone number with the given message.

        :param string to_number: the phone number to send the message to.
        """
        ESCALATION_MSG = f'Hey, {self.oncall}, Mom is not so happy, you might want to check in on that and maybe buy her favorite wine while you are at it.'

        logger.info('sending message to %s: %s', self.oncall, to_number)

        message = self.twilio_client.messages \
            .create(
                body=ESCALATION_MSG,
                from_=self.from_number,
                to=to_number,
            )

    def _send_mom_text(self, moms_number):
        """Pings moms phone with the given message.

        :param int moms_number: moms phone number to send the message to.
        """
        MOMS_MSG = 'Hey ma, did I tell you today that you are the greatest and most beautiful Mom ever?'

        logger.info('sending message to mom: %s', self.moms_number)

        essage = self.twilio_client.messages \
            .create(
                body=MOMS_MSG,
                from_=self.from_number,
                to=moms_number,
            )

    def _lower_threshold_escalation_ping(self, text):
        """Sends a message based on a lower threshold calculated from the parsed text.

        :param string text: text submitted by the user.
        """
        threshold_passed = self._calculate_escalation_score(text) < 0.4

        if threshold_passed:
            self._send_escalation_text(self.to_number)

    def _higher_threshold_escalation_ping(self, text):
        """Sends a message based on a higher threshold calculated from the parsed text.

        :param string text: text submitted by the user.
        """
        threshold_passed = self._calculate_escalation_score(text) < 0

        if threshold_passed:
            self._send_escalation_text(self.to_number)
