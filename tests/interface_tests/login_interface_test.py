from API.interface.user_log_in_interface import ExistingUserLogIn


def main(username, password):
    log_in_check = ExistingUserLogIn(username=username, password=password)

    return log_in_check.main()


assert main(username='True', password='') == {'message': 'Using true is disallowed.'}
assert main(username='', password='') == {'message': 'Empty username field!'}
assert main(username='ABCsasdasdasdadsad', password='Avnkasd202') == {'message': 'User not found'}
assert main(username='hardy_21', password='asdsadasd') == {"message": 'Incorrect Password'}
assert main(username='hardy_21', password='Doomguy123') == {'message': 'You logged in Successfully'}
