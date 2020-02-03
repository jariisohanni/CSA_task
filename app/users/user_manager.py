class UserManager:
    def __init__(self):
        self.user_list = []


    def addUser(self,user):
        self.user_list.append(user)

    def find_user_with_id(self,toFind):
        for user in self.user_list:
            if user.username == toFind:
                return user

        return None
