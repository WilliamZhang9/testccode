import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:  # Corrected from = to ==
        return response.json()

def print_names(users):
    for user in users:
        print(user["name"].upper())  # Corrected: added ()

def main():
    users = fetch_users()
    if users:
        print_names(users)
    else:
        print("Failed to fetch users.")

main()
