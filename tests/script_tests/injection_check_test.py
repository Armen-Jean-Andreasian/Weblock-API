from API.backend.checks.script.input_checks import InputValidator, InjectionChecker


def main(username, password):
    validator = InputValidator(username=username, password=password)
    injection_check = InjectionChecker(validator)

    return injection_check.detect_malicious()


assert 'Error' in main(username="'", password='123')
assert 'Error' in main(username='1==1', password='')
assert 'Error' in main(username='drop table', password='True')
assert 'Error' not in main(username='ABCsadsad', password='Avnkasd202')
