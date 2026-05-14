class User:
    def __init__(self, name, age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18  # Fixed: int vs string comparison

def create_users():
    users = [
        User("Alice", 25),
        User("Bob", 17),  # Fixed: missing age, now set to a non-adult age
        User("Charlie", 30)  # Fixed: wrong type, now an int
    ]
    return users

def print_adults(users):
    for user in users:
        if user.is_adult():
            print(user.name)

users = create_users()
print_adults(users)
