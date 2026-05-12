import requests

def fetch_user_data():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    return []

def print_names(users):
    for user in users:
        print(user['name'].upper())
