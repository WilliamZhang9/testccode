import requests

def fetch_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(user['name'].upper())

if __name__ == "__main__":
    fetch_users()
