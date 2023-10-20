from interface.checks.script.input_checks import InputValidator, PasswordChecker


def main(username, password):
    validator = InputValidator(username=username, password=password)
    password_check = PasswordChecker(validator)

    return password_check.validate_password_strength()


assert main(username="abc", password='123') == {'Error': 'Weak password!'}
assert main(username='True', password='') == {'Error': 'Weak password!'}
assert main(username='', password='') == {'Error': 'Weak password!'}
assert main(username='ABCsadsad', password='Avnkasd202') == {}
