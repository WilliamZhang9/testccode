import requests

def fetch_users():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        # FIX: Changed '=' to '==' for comparison
        if response.status_code == 200:
            return response.json()
    except (requests.exceptions.RequestException, ValueError):
        pass
    return []

def print_names(users):
    for user in users:
        # FIX: Added () to execute the .upper() method
        name = user.get('name', 'Unknown')
        print(name.upper())

if __name__ == "__main__":
    users = fetch_users()
    print_names(users)
