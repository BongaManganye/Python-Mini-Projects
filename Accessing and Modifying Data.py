# Accessing and Modifying Data:
#1. The traditional way: make the data private and use getters and setters:

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email

user1 = User("Bonga", "bon@gmail.com", "123")
print(user1._email)

user1.email = "dan"

print(user1.email)
