import urllib2
import urllib

MVAAYOO_USERNAME = ""
MVAAYOO_PASSWORD = ""
MVAAYOO_API_URL_SENDSMS = 'https://www.smsglobal.com.au/http-api.php'
MVAAYOO_API_URL_CHECKBALANCE = 'https://www.smsglobal.com/credit-api.php'


class Mvaayoo:
    """
    A wrapper that manages the Mvaayoo
    """

    def get_username(self):
        return MVAAYOO_USERNAME

    def get_password(self):
        return MVAAYOO_USERNAME

    def get_balance(self):
        """
        Get balance with provider.
        """
        params = {
            'user': self.get_username(),
            'password': self.get_password(),
        }

        req = urllib2.Request(urllib.urlencode(params))
        response = urllib2.urlopen(req).read()

    def send_messages(self, sms_messages):
        """
        Sends one or more SmsMessage objects and returns the number of sms
        messages sent.
        """
        if not sms_messages:
            return

        num_sent = 0
        for message in sms_messages:
            if self._send(message):
                num_sent += 1
        return num_sent

    def _send(self, message):
        """A helper method that does the actual sending."""
        return True

    def _parse_response(self, result_page):
        """
        pass
