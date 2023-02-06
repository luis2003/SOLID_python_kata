from abc import ABC, abstractmethod


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class SMSAuthorizer(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"SMSAuthorizer is verifying SMS code: {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class NotARobotAuth(Authorizer):
    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        print(f"NotARobotAuth is checking you are not a robot...")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
