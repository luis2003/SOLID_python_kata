import unittest
from payment_system.authorizers import SMSAuthorizer, Authorizer, NotARobotAuth


class AuthorizersTestCase(unittest.TestCase):
    def setUp(self):
        self.an_sms_auth = SMSAuthorizer()
        self.an_not_a_robot_auth = NotARobotAuth()
        self.assertIsInstance(self.an_sms_auth, Authorizer)
        self.assertIsInstance(self.an_not_a_robot_auth, Authorizer)

    def test_uses_base_class(self):
        self.assertIsInstance(self.an_sms_auth, Authorizer)

    def test_verify_code(self):
        self.an_sms_auth.verify_code(123456)
        assert self.an_sms_auth.authorized

    def test_is_authorized(self):
        self.assertEqual(False, self.an_sms_auth.is_authorized())

    def test_not_a_robot_auth(self):
        self.an_not_a_robot_auth.not_a_robot()
        assert self.an_not_a_robot_auth.authorized

    def test_notarobot_is_authorized(self):
        self.assertEqual(False, self.an_not_a_robot_auth.is_authorized())


if __name__ == '__main__':
    unittest.main()
