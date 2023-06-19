class User:
    def __init__(self, username):
        self.username = username
        self.id = id(self)
        self.followers = 0
        self.following = 0


    def __repr__(self):
        return f"ID: {self.id} | Username: {self.username}"

    def getName(self):
        print(self.username)


    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("name")
user_2 = User("name2")
user_1.follow(user_2)
user_2.follow(user_1)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)
user_1.getName()
