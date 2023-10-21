import requests


URL = "http://127.0.0.1:5001/login"


def test_incorrect_username():
    data = {
        "username": "MyUsername10",
        "password": "MyPassword12"
    }

    # Make a POST request with the JSON data
    response = requests.post(URL, json=data)
    return response.status_code, response.text


def test_incorrect_password():
    data = {
        "username": "MyUsername13",
        "password": "MyPassword1"
    }

    # Make a POST request with the JSON data
    response = requests.post(URL, json=data)
    return response.status_code, response.text


def test_success():

    # Create a dictionary with the username and password
    data = {
        "username": "MyUsername13",
        "password": "MyPassword12"
    }

    # Make a POST request with the JSON data
    response = requests.post(URL, json=data)
    return response.status_code, response.json()


if __name__ == '__main__':
    response1 = test_incorrect_username()
    response2 = test_incorrect_password()
    response3 = test_success()

    # Remove newline characters using the strip() method
    print(response1[0], response1[1].strip())
    print(response2[0], response2[1].strip())
    print(response3[0], response3[1])

