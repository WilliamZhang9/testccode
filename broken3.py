class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18

def create_users():
    users = [
        User("Alice", 25),
        User("Bob", 19),
        User("Charlie", 30)
    ]
    return users

def print_adults(users):
    for user in users:
        if user.is_adult():
            print(user.name)

users = create_users()
print_adults(users)
