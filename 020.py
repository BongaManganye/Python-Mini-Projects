from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.paaword = password
    
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email

    def set_email(self, new_email):
        self._email = new_email

user1 = User("Bonga", "Bon@gmail.com  ", "123")
print(user1.get_email())

user1.set_email("Bon@outlook.com")
print(user1.get_email())
