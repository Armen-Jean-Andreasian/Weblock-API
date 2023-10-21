from API.backend.checks.register_check_logic import RegisterCheckMain


def main(username, password):
    log_in_check = RegisterCheckMain(username=username, password=password)

    return log_in_check.run_check()


assert main(username="abc", password='123') == {'Error': 'Weak __password!'}
assert main(username='True', password='') == {'Error': 'Using true is disallowed.'}
assert main(username='', password='') == {'Error': 'Empty username field!'}
assert main(username='ABCsadsad', password='Avnkasd202') == {'username': 'ABCsadsad', '__password': 'Avnkasd202'}
