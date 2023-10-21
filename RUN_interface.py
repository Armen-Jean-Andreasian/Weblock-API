from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from API.interface.user_log_in_interface import ExistingUserLogIn
from API.interface.user_registration_interface import NewUserRegistration

from icecream import ic

api_http = Flask(__name__)
CORS(api_http)


@api_http.route('/')
def default():
    text = ("For logging in send a request in /login/<login><password> format \n"
            "For registration send a request in /registration/<login><password> format")
    return text


@api_http.route('/login', methods=['POST'])
@cross_origin()
def login():
    data = ic(request.get_json())  # Assuming data is sent as JSON

    if 'username' in data and 'password' in data:
        username, password = ic(data['username'], data['password'])

        user_login = ExistingUserLogIn(username=username, password=password)
        result = user_login.main()
        return jsonify(result)
    else:
        return "Invalid request, missing 'login' or 'password' in the request body", 400


@api_http.route('/registration', methods=['POST'])
@cross_origin()
def registration():
    data = ic(request.get_json())  # Assuming data is sent as JSON

    if 'username' in data and 'password' in data:
        username, password = ic(data['username'], data['password'])

        user_registration = NewUserRegistration(username=username, password=password)
        result = user_registration.main()
        return jsonify(result), 200

    else:
        return "Invalid request, missing 'login' or 'password' in the request body", 400


if __name__ == '__main__':
    api_http.run(host='127.0.0.1', port=5001)
