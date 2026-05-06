import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # Fix: Changed assignment (=) to equality (==)
    if response.status_code == 200:
        return response.json()

def print_names(users):
    for user in users:
        # Fix: Added parentheses to execute the .upper() method
        print(user["name"].upper())

def main():
    users = fetch_users()
    if users:
        print_names(users)
    else:
        print("Failed to fetch users or no users found.")

main()
