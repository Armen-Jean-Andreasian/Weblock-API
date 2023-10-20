from interface.checks.script.input_checks import InputValidator, InjectionChecker, NullChecker


class LogInCheckMain:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.validator = InputValidator(username=self.username, password=self.password)

    def run_check(self) -> dict:

        injection_checker = InjectionChecker(validator_obj=self.validator)
        injection_check_result = injection_checker.detect_malicious()

        if 'Error' in injection_check_result:
            return injection_check_result

        null_checker = NullChecker(validator_obj=self.validator)
        null_check_result = null_checker.detect_null()

        if 'Error' in null_check_result:
            return null_check_result

        return {'username': self.username, 'password': self.password}


if __name__ == '__main__':
    l1 = LogInCheckMain(username="abc", password='123')
    print(l1.run_check())

    l2 = LogInCheckMain(username='True', password='')
    print(l2.run_check())

    l3 = LogInCheckMain(username='', password='')
    print(l3.run_check())

    l4 = LogInCheckMain(username='ABCsadsad', password='Avnkasd202')
    print(l4.run_check())