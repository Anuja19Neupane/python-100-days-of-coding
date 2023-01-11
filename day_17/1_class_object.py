class User:
    pass


user_1 = User()
user_1.id = "100"
user_1.username = "anuja"
print(user_1.username)


# aba arko user ko lagi feri yo sabei garna parxa so we gonna find an easy way.

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("100", "anuja")
user_2 = User("101", "abiral")
print(user_1.name)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
