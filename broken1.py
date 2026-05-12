import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5) # Added timeout for safety
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching users: Status Code {response.status_code}")
            return [] # Return empty list on non-200 status
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return [] # Return empty list on request exception

def print_names(users):
    if users: # Check if users is not None and not empty
        for user in users:
            if "name" in user: # Check if 'name' key exists
                print(user["name"].upper()) # Corrected to call .upper()
            else:
                print("User object missing 'name' key.")
    else:
        print("No users to print or users list is empty.")

def main():
    users = fetch_users()
    print_names(users)

main()
