class NewUserMetaclass(type):
    def __str__(cls):
        return ("Usage: \n\treg_obj = NewUserRegistration(username=ExampleUsername123, __password=ExamplePassword123)"
                "\n\treg_obj.register_user()")