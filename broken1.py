import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    if response.status_code == 200:  # Fixed: Changed = to ==
        return response.json()
    else:
        print(f"Failed to fetch users. Status code: {response.status_code}")
        return None

def print_names(users):
    for user in users:
        print(user["name"].upper())  # Fixed: Added () to call the method

def main():
    users = fetch_users()
    if users: # Added: Check if users were successfully fetched
        print_names(users)
    else:
        print("No users to display.")

main()
