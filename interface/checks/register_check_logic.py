from interface.checks.script.input_checks import InputValidator, InjectionChecker, NullChecker, PasswordChecker


class RegisterCheckMain:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.validator = InputValidator(username=self.username, password=self.password)

    def run_check(self) -> dict:

        injection_checker = InjectionChecker(validator_obj=self.validator)
        injection_check_result: dict = injection_checker.detect_malicious()

        if 'Error' in injection_check_result:
            return injection_check_result

        null_checker = NullChecker(validator_obj=self.validator)
        null_check_result: dict = null_checker.detect_null()

        if 'Error' in null_check_result:
            return null_check_result

        password_checker = PasswordChecker(validator_obj=self.validator)
        password_check_result: dict = password_checker.validate_password_strength()

        if 'Error' in password_check_result:
            return password_check_result

        return {'username': self.username, 'password': self.password}

