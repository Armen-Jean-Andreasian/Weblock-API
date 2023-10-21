class LogInMetaclass(type):
    def __str__(cls):
        return ("Usage: \n\tlogin_obj = ExistingUserLogIn(username=ExampleUsername123, __password=ExamplePassword123)"
                "\n\tlogin_obj.check_credentials()")