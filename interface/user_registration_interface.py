import os
import sqlite3

from API.backend.confidential.encryption import Encryptor

from API.backend.checks.register_check_logic import RegisterCheckMain
from API.misc.definitions.new_user import NewUserMetaclass


class NewUserRegistration(metaclass=NewUserMetaclass):

    class __ConnectToDatabase:
        def __init__(self):
            self.__db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend/database/database.db"))

        def connect(self) -> sqlite3.Connection:
            """
            Connects to the database and returns the connection
            """
            connection = sqlite3.connect(self.__db_path)
            return connection

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.connection = None

    def check(self) -> dict:
        """
        IMPORTANT note: in case of registration with an occupied username,
            the code prioritizes password checks before verifying the username's existence.
                This behavior is implemented to prevent overloading the server.

            Example:
                - If a user with the username 'hardy_21' exists:
                    - NewUserRegistration(username='hardy_21', password='asdsadasd') => {'message': 'Weak password!'}
                    - NewUserRegistration(username='hardy_21', password='Abasdsap12') => {'message': 'Username is occupied!'}

        It's not a bug, it's a feature ;)
        """
        registration_check = RegisterCheckMain(username=self.username, password=self.password)
        result: dict = registration_check.run_check()
        return result

    def encrypt(self) -> tuple:
        """ Encrypts the text """
        username = Encryptor(self.username.lower()).encrypt()
        password = Encryptor(self.password).encrypt()
        return username, password

    def check_against_db(self):
        """Verify user credentials against the database."""
        cursor = self.connection.cursor()

        __response = cursor.execute(f"SELECT username from user_details WHERE username='{self.username}'")
        result = __response.fetchall()
        self.connection.close()

        if len(result) > 0:
            return {"Error": "Username is occupied!"}
        else:
            return {"Success": "Username is available"}


    def register_user(self):
        self.connection = self.__ConnectToDatabase().connect()
        cursor = self.connection.cursor()

        new_user = (self.username, self.password)
        cursor.execute('INSERT INTO user_details VALUES (?, ?)', new_user)

        self.connection.commit()
        self.connection.close()

        return {"message": "User registered!"}

    def main(self):
        """
        Registration in process flow:
            1. Check the input
            2. Encrypt
            3. Connect to db
            4. Check if the login exists => Abort / Register
            5. Send the result to front
        """

        """ 1. Check the input """

        check = self.check()
        if "Error" in check:
            # returning error message
            return {"message": f"{check['Error']}"}


        """ 2. Encrypt """

        self.username, self.password = self.encrypt()


        """ 3. Connect to db """
        self.connection = self.__ConnectToDatabase().connect()


        """ 4. Check against the database """

        username_availability = self.check_against_db()

        if "Error" in username_availability:
            # returning error message
            return {"message": f"{username_availability['Error']}"}
            # return jsonify({"message": f"{username_availability['Error']}"}), 200

        elif "Success" in username_availability:
            return self.register_user()
            # return jsonify(self.register_user()), 200


if __name__ == '__main__':
    nu = NewUserRegistration(username='hardy_21', password='asdsadasd')
    print(nu.main())

