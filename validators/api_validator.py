import requests


URL = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(URL, timeout=10)

print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")