class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username},it's {self.username}")

user1 = User("Bonga", "man@gmail.com", "123")
print(user1.email)

user1.email = "danny@gmail.com"
print(user1.email)
