class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age > 18

users = [
    User("Alice", 25),
    User("Bob", 30),
    User("Charlie", 30)
]

print([u.name for u in users if u.age > 18])
