import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}")
    return [] # Return an empty list on error to prevent downstream issues

def print_names(users):
    if not users: # Handle None or empty list
        print("No users to display.")
        return

    for user in users:
        try:
            print(user["name"].upper()) # Call the method
        except KeyError:
            print("User object missing 'name' key.")
        except Exception as e:
            print(f"An unexpected error occurred while processing user: {e}")

def main():
    users = fetch_users()
    print_names(users)

main()
