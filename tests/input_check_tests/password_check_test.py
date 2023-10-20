from interface.input_checks import InputValidator, PasswordChecker


def main(username, password):
    c = InputValidator(username=username, password=password)
    p_check = PasswordChecker(c)

    return p_check.validate_password_strength()


assert main(username="abc", password='123') == {'Error': 'Weak password!'}
assert main(username='True', password='') == {'Error': 'Weak password!'}
assert main(username='', password='') == {'Error': 'Weak password!'}
assert main(username='ABCsadsad', password='Avnkasd202') == {}