from API.backend.checks.script.input_checks import InputValidator, InjectionChecker, NullChecker


class LogInCheckMain:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.validator = InputValidator(username=self.username, password=self.password)

    def run_check(self) -> dict:
        """
        Returns:
            1. { 'username': 'abc', '__password': '123'}
            2. {'Error': 'Error message'}
                    example: {'Error': 'Empty username field!'}
        """

        injection_checker = InjectionChecker(validator_obj=self.validator)
        injection_check_result = injection_checker.detect_malicious()

        if 'Error' in injection_check_result:
            return injection_check_result

        null_checker = NullChecker(validator_obj=self.validator)
        null_check_result = null_checker.detect_null()

        if 'Error' in null_check_result:
            return null_check_result

        return {'username': self.username, '__password': self.password}
