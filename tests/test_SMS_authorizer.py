import unittest
from payment_system.sms_authorizer import SMSAuthorizer


class SMSAuthorizerTestCase(unittest.TestCase):
    def test_creation(self):
        an_sms_auth = SMSAuthorizer()
        self.assertIsInstance(an_sms_auth, SMSAuthorizer)


if __name__ == '__main__':
    unittest.main()
