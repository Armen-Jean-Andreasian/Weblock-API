from API.interface.user_registration_interface import NewUserRegistration


def main(username, password):
    log_in_check = NewUserRegistration(username=username, password=password)

    return log_in_check.main()


assert main(username='True', password='') == {'message': 'Using true is disallowed.'}

assert main(username='', password='') == {'message': 'Empty username field!'}
assert main(username='hardy_21', password='') == {'message': 'Empty password field!'}

# read the documentation of NewUserRegistration.check()
assert main(username='hardy_21', password='asdsadasd') == {'message': 'Weak password!'}
assert main(username='hardy_21', password='Abasdsap12') == {'message': 'Username is occupied!'}

assert main(username='asdasd', password='asdasd') == {'message': "Matching username and password!"}

