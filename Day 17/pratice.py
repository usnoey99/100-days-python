class User: # class name is written with PascalCase
    # pass: if the class is empty, we can use pass for no error

    # def __init__(self):
    # every time create a new object from this class, this funktion is going to be triggered

    def __init__(self, user_id, username, ):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Amanda")
user_2 = User("002", "Jack")
# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"

user_1.follow(user_2) # user_1 follows user_2
print(user_1.followers) # 0
print(user_1.following) # 1
print(user_2.followers) # 1
print(user_2.following) # 0

