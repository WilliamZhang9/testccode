class User:
    def __init__(self, name, age):
        self.name = name
        # FIX: Ensure age is stored as an integer for comparison
        try:
            self.age = int(age)
        except (ValueError, TypeError):
            self.age = 0
    
    def is_adult(self):
        # FIX: Compare against integer 18 instead of string "18"
        return self.age >= 18

users = [
    User("Alice", 25),
    User("Bob", 17),      # FIX: Added missing age argument
    User("Charlie", 30)   # FIX: Changed "30" to 30 (integer)
]

for user in users:
    if user.is_adult():
        print(user.name)
