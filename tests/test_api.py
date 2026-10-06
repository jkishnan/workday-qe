import requests


URL = "https://jsonplaceholder.typicode.com/users/1"


def test_get_user_status_code():
    response = requests.get(URL, timeout=10)

    assert response.status_code == 200


def test_get_user_id():
    response = requests.get(URL, timeout=10)
    data = response.json()

    assert data["id"] == 1


def test_get_user_required_fields():
    response = requests.get(URL, timeout=10)
    data = response.json()

    required_fields = [
        "id",
        "name",
        "username",
        "email"
    ]

    for field in required_fields:
        assert field in data

def test_user_not_found():
    url = "https://jsonplaceholder.typicode.com/users/9999"

    response = requests.get(url, timeout=10)

    assert response.status_code == 404