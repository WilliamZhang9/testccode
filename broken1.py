import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10) # Added timeout for robustness
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred during request: {req_err}")
    return [] # Return empty list on any error or non-200 status

def print_names(users):
    if users: # Check if users list is not empty or None
        for user in users:
            if "name" in user:
                print(user["name"].upper()) # Called the upper() method
            else:
                print("Warning: User object missing 'name' key.")
    else:
        print("No users to display.")

def main():
    users = fetch_users()
    print_names(users)

main()
