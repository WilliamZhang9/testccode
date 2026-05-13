import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=5) # Added timeout for robustness
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error occurred: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Timeout error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An unexpected error occurred: {e}")
    return [] # Return an empty list on failure

def print_names(users):
    if not users: # Handle empty or None users list
        print("No users to print.")
        return

    for user in users:
        if isinstance(user, dict) and "name" in user: # Check if user is a dict and has 'name' key
            print(user["name"].upper()) # Corrected: added ()
        else:
            print(f"Invalid user object or missing 'name' key: {user}")

def main():
    users = fetch_users()
    print_names(users)

if __name__ == "__main__": # Added standard entry point
    main()
