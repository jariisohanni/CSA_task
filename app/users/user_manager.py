import hashlib
import uuid, random, string
from User_class import User, Role

class UserManager:
    def __init__(self):
        self.user_list = []


    def addUser(self,user):
        user.password = self.hash_password(user.password)
        user.create_keys()

        self.user_list.append(user)

    def find_user_with_id(self,toFind):
        for user in self.user_list:
            if user.username == toFind:
                return user

        return None

    def create_password(self):
        length = 10
        lettersDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersDigits) for i in range (length))


    def hash_password(self, password):
        # uuid is used to generate a random number of the password
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


#Checked with below code that user with password hashing, role, and public key works

if __name__ == "__main__":

    manager = UserManager()
    password = manager.create_password()
    print(password)
    user = User("sarioik", password, Role.Admin)
    manager.addUser(user)

    print(user)

