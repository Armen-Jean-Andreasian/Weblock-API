import requests



URL = "http://127.0.0.1:5001/registration"


def create_data(username: str, password: str) -> dict[str, str]:
    data = {
        "username": f"{username}",
        "password": f"{password}"
    }
    return data


def make_request(data):
    # Make a POST request with the JSON data
    response = requests.post(url=URL, json=data)
    return response.status_code, response.text


def malicious_input():
    # {'message': 'Using true is disallowed.'}
    username = "if True is True"
    password = "' or 1 == 1 "
    data = create_data(username=username, password=password)

    return make_request(data)


def empty_username_field():
    # {'message': 'Empty username field!'}
    data = create_data(username="", password="Password123")
    return make_request(data)


def empty_password_field():
    # {'message': 'Empty password field!'}
    data = create_data(username="username123", password="")
    return make_request(data)


def weak_password():
    # {'message': 'Weak password!'}
    data = create_data(username="MyUsername22", password="pas")
    return make_request(data)


def occupied_username():
    # {'message': 'Username is occupied!'}
    data = create_data(username='hardy_21', password='Abasdsap12')
    return make_request(data)


def matching_input():
    # {'message': "Matching username and password!"}
    data = create_data(username='asdasd', password='asdasd')
    return make_request(data)


def success(new_username, new_password):
    # Create a dictionary with the username and password
    data = {
        "username": f"{new_username}",
        "password": f"{new_password}"
    }

    # Make a POST request with the JSON data
    response = requests.post(URL, json=data)
    return response.status_code, response.text.strip()




if __name__ == '__main__':
    response1 = malicious_input()
    print(response1[0], response1[1].strip())

    print(malicious_input())
    print(empty_username_field())
    print(empty_password_field())
    print(occupied_username())
    print(matching_input())

