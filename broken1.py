import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:  # Corrected: assignment instead of comparison
        return response.json()

def print_names(users):
    for user in users:
        print(user["name"].upper())  # Corrected: missing ()

def main():
    users = fetch_users()
    print_names(users)

main()
