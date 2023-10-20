from interface.checks.log_in_check_logic import LogInCheckMain


def main(username, password):
    log_in_check = LogInCheckMain(username=username, password=password)
    
    return log_in_check.run_check()


assert main(username="abc", password='123') == {'username': 'abc', 'password': '123'}
assert main(username='True', password='') == {'Error': 'Using true is disallowed.'}
assert main(username='', password='') == {'Error': 'Empty username field!'}
assert main(username='ABCsadsad', password='Avnkasd202') == {'username': 'ABCsadsad', 'password': 'Avnkasd202'}
