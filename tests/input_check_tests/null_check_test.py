from interface.input_checks import InputValidator, NullChecker


def main(username, password):
    c = InputValidator(username=username, password=password)
    p_check = NullChecker(c)

    return p_check.detect_null()


assert main(username="", password='123') == {'Error': "Empty username field!"}
assert main(username='True', password='') == {'Error': "Empty password field!"}
assert main(username='', password='') == {'Error': "Empty username field!"}
assert main(username='ABCsadsad', password='Avnkasd202') == {}
