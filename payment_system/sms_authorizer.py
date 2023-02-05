class SMSAuthorizer:
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"SMSAuthorizer is verifying SMS code: {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized
