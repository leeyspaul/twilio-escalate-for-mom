from unittest.mock import MagicMock

import pytest

from app.escalate import TwilioEscalate


# ONCALL CONFIG
ONCALL = 'Browns'
FROM_NUMBER = '+123456789'
TO_NUMBER = '+987654321'


@pytest.fixture
def mock_twilio_client(mocker):
    mock_twilio_client = mocker.patch('app.get_twilio_client')
    mock_twilio_client = (
        MagicMock('twilio_client'),
    )

    return mock_twilio_client


@pytest.fixture
def twilio_escalate(mocker, mock_twilio_client):
    mock_ld_client, mock_twilio_client = mock_twilio_client

    twilio_escalate = TwilioEscalate(
        mock_twilio_client, ONCALL, FROM_NUMBER, TO_NUMBER,
    )

    return twilio_escalate


@pytest.mark.parametrize('more_positive_polarity_score', [0.3, 0.2])
def test_ping_on_positive_polarity__lower_threshold_escalation_ping(
        twilio_escalate, more_positive_polarity_score,
):

    twilio_escalate._calculate_escalation_score = MagicMock(
        name='_calculate_escalation_score',
    )
    twilio_escalate._calculate_escalation_score.return_value = more_positive_polarity_score  # noqa

    twilio_escalate._send_escalation_text = MagicMock(
        name='_send_escalation_text',
    )

    twilio_escalate._lower_threshold_escalation_ping('Hi! This feature is OK.')

    twilio_escalate._send_escalation_text.assert_called()


@pytest.mark.parametrize('more_positive_polarity_score', [0.3, 0.2])
def test_no_ping_on_positive_polarity__higher_threshold_escalation_ping(
        twilio_escalate, more_positive_polarity_score,
):

    twilio_escalate._calculate_escalation_score = MagicMock(
        name='_calculate_escalation_score',
    )
    twilio_escalate._calculate_escalation_score.return_value = more_positive_polarity_score  # noqa

    twilio_escalate._send_escalation_text = MagicMock(
        name='_send_escalation_text',
    )

    twilio_escalate._higher_threshold_escalation_ping(
        'Hi! This feature is OK.',
    )

    twilio_escalate._send_escalation_text.assert_not_called()
