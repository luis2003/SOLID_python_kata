import unittest
from payment_system.sms_authorizer import SMSAuthorizer


class SMSAuthorizerTestCase(unittest.TestCase):
    def setUp(self):
        self.an_sms_auth = SMSAuthorizer()
        self.assertIsInstance(self.an_sms_auth, SMSAuthorizer)

    def test_verify_code(self):
        self.an_sms_auth.verify_code(123456)
        assert self.an_sms_auth.authorized

    def test_is_authorized(self):
        self.assertEqual(False, self.an_sms_auth.is_authorized())


if __name__ == '__main__':
    unittest.main()