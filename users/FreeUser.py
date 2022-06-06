from User import User
from datetime import datetime

class FreeUser(User):
    def __init__(self, name, email_address, phone_number, age):
        super().__init__(name, email_address, phone_number, age)
        


    def post(self, str):
        if len(self.all_posts) >= 2:
            print(f"Please upgrade to Premium to post '{str}'")
        else:
            time = (datetime.now()).strftime("%H:%M:%S")
            self.all_posts[str] = time
            


    






