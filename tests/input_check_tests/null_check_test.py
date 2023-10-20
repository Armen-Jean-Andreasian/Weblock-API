from interface.checks.script.input_checks import InputValidator, NullChecker


def main(username, password):
    validator = InputValidator(username=username, password=password)
    null_check = NullChecker(validator)

    return null_check.detect_null()


assert main(username="", password='123') == {'Error': "Empty username field!"}
assert main(username='True', password='') == {'Error': "Empty password field!"}
assert main(username='', password='') == {'Error': "Empty username field!"}
assert main(username='ABCsadsad', password='Avnkasd202') == {}
