import os
import sqlite3


from API.misc.definitions.user_login import LogInMetaclass

from API.backend.checks.log_in_check_logic import LogInCheckMain
from API.backend.confidential.encryption import Encryptor


class LogIn(metaclass=LogInMetaclass):
    """
    This class is designed to handle user authentication by verifying user credentials against a database.
    """

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

    def __check(self) -> dict:
        log_in_check = LogInCheckMain(username=self.username, password=self.password)
        result: dict = log_in_check.run_check()
        return result

    def __encrypt(self) -> tuple:
        """ Encrypts the text """
        username = Encryptor(self.username.lower()).encrypt()
        password = Encryptor(self.password).encrypt()
        return username, password

    def __check_against_db(self):
        """Verify user credentials against the database."""
        cursor = self.connection.cursor()

        __response = cursor.execute(f"SELECT password from user_details WHERE username='{self.username}'")
        result: list[tuple[str]] = __response.fetchall()
        self.connection.close()

        if len(result) == 0:
            return {"message": "User not found"}
            # return jsonify({"message": "User not found"}), 200
        else:
            __db_stored_password = result[0][0]

            if __db_stored_password == self.password:
                # return jsonify({"message": 'You logged in Successfully'}), 200
                return {"message": 'You logged in Successfully'}

            else:
                return {"message": 'Incorrect Password'}

    def main(self):
        """
        Log in process flow:
            1. Check the input
            2. Encrypt
            3. Connect to db
            4. Check against the database
            5. Send the result to front
        """

        """ 1. Check the input """

        check = self.__check()
        if 'Error' in check:
            # returning error message
            return {"message": f"{check['Error']}"}

        """ 2. Encrypt """

        self.username, self.password = self.__encrypt()

        """ 3. Connect to db """
        self.connection = self.__ConnectToDatabase().connect()

        """ 4. Check against the database """
        result = self.__check_against_db()

        """ 5. Send the result """
        return result
