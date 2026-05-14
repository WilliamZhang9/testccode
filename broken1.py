import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching users: {e}")
        return [] # Return an empty list to prevent downstream errors
    return [] # Ensure a list is always returned if status is not 200 or an error occurs

def print_names(users):
    if users: # Check if users list is not empty or None
        for user in users:
            # Ensure 'name' key exists to prevent KeyError
            if "name" in user:
                print(user["name"].upper()) # Call upper() method
            else:
                print("User object missing 'name' key.")

def main():
    users = fetch_users()
    print_names(users)

if __name__ == "__main__": # Standard practice for runnable scripts
    main()
