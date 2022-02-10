class User:

   def __init__(self, user_id, username):
      print("New user being created...")
      self.id = user_id
      self.username = username
      self.followers = 0
      self.following = 0

   def follow(self, user):
      user.followers += 1
      self.following =+ 1


user_1 = User("001", "Jack")

user_2 = User("002", "Boris")

# user_1.id = "001"
# user_1.username = "Josh"

user_1.follow(user_2)

print(f"User with id {user_1.id} is called {user_1.username}. They have {user_1.followers} followers.\nThey are following {user_1.following} users.")
# print(f"User {user_1.beef}"

