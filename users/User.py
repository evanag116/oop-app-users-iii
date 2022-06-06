from datetime import datetime
from tokenize import maybe

class User:

    def __init__(self, name, email_address, phone_number, age):
        self.name = name
        self.email_address = email_address
        self.phone_number = str(phone_number)
        self.age = age
        self.all_posts = {}

    def post(self, str):
        time = (datetime.now()).strftime("%H:%M:%S")
        self.all_posts[str] = time

    def delete(self, str):
        self.all_posts.pop(str)

    def get_all_posts(self):
        return self.all_posts


    
    
# evan = User("Evan", "evan@codeplatoon.org", 502715220, 23)
# evan.post("my first post")
# evan.post("my second post")

# print(evan.get_all_posts())




