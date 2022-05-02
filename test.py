import requests

URL = "http://localhost:8080/auth/"


def get_token():
    response = requests.post(
        f"{URL}token/",
        json={"username": "gabriel-milan", "password": "Gazolaa1"}
    )
    return response.json()["access"]


def test_authorization_bearer():
    response = requests.get(
        URL,
        headers={"Authorization": f"Bearer {get_token()}"}
    )
    if response.text == "OK":
        print("test_authorization_bearer OK")


def test_authorization():
    response = requests.get(
        URL,
        headers={"Authorization": f"{get_token()}"}
    )
    if response.text == "OK":
        print("test_authorization OK")


def test_x_auth_token_bearer():
    response = requests.get(
        URL,
        headers={"X-Auth-Token": f"Bearer {get_token()}"}
    )
    if response.text == "OK":
        print("test_x_auth_token_bearer OK")


def test_x_auth_token():
    response = requests.get(
        URL,
        headers={"X-Auth-Token": f"{get_token()}"}
    )
    if response.text == "OK":
        print("test_x_auth_token OK")


if __name__ == "__main__":
    test_authorization_bearer()
    test_authorization()
    test_x_auth_token_bearer()
    test_x_auth_token()
