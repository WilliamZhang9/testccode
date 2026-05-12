class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18

users = [
    User("Alice", 25),
    User("Bob", 20),
    User("Charlie", 30)
]

for user in users:
    if user.is_adult():
        print(f"{user.name} is an adult.")
