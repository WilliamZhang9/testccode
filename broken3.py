class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18

def process_users():
    users = [
        User("Alice", 25),
        User("Bob", 17),
        User("Charlie", 30)
    ]
    for user in users:
        if user.is_adult():
            print(user.name)

if __name__ == "__main__":
    process_users()
