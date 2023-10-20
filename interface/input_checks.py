import input_armor  # pip install input_armor


class InputValidator:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class InjectionChecker:

    def __init__(self, validator_obj: InputValidator):
        self.username = validator_obj.username
        self.password = validator_obj.password

    def detect_malicious(self) -> dict:
        """
        Checks the input for malicious behaviour and suspicious characters using the lib input_armor

        Returns: {'Error': 'Error message'} or {}
        """
        login = input_armor.check(rabbit=self.username)
        password = input_armor.check(rabbit=self.password)

        if False in login.keys():
            return {'Error': login[False]}

        if False in password.keys():
            return {'Error:': password[False]}

        else:
            return {}  # correct password


class NullChecker:
    def __init__(self, validator_obj: InputValidator):
        self.username = validator_obj.username.strip()
        self.password = validator_obj.password.strip()

    def detect_null(self):
        """
        Checks for empty input

        Returns: {'Error': "Empty username field!"} or {'Error': "Empty password field!"} or {}
        """
        if len(self.username) == 0:
            return {'Error': "Empty username field!"}

        elif len(self.password) == 0:
            return {'Error': "Empty password field!"}

        else:
            return {}  # non-null


class PasswordChecker:
    def __init__(self, validator_obj: InputValidator):
        self.password = validator_obj.password

    def validate_password_strength(self) -> dict:

        """
        Password strength check.

        Passwords should be:
            - Eight or more characters long
            - Contain at least one number
            - Contain at least one upper letter

        Returns: {'Error': "Weak password!"} or {}
        """
        if len(self.password) >= 8 and any(i.isdigit() for i in self.password) and any(
                i.isupper() for i in self.password):
            return {}  # not weak
        else:
            return {'Error': "Weak password!"}
