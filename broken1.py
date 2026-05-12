import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Fixes the syntax error and adds validation
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def print_names(users):
    if not users:
        print("No users to display.")
        return
    for user in users:
        print(user["name"].upper()) # Added () to execute the method

def main():
    users = fetch_users()
    print_names(users)

main()
