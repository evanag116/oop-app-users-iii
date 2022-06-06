from FreeUser import FreeUser
from PremiumUser import PremiumUser



user1 = PremiumUser("User1", "nathan@codeplatoon.org", 3125550123, 20)
user1.post("first")
user1.post("second")
user1.post("third")


evan = FreeUser("Evan", "evan@codeplatoon.org", 5027152210, 23)

evan.post("my first post")
evan.post("my second post")
evan.post("my third post")
evan.delete("my second post")
evan.post("my third post")


print(evan.all_posts)



