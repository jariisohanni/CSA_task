import hashlib
<<<<<<< HEAD
import os, sys, uuid, random, string, pickle, csv
from users.user import User, Role
=======
import uuid, random, string
from User_class import User, Role
>>>>>>> 9fe66f9087f8c2079a4dfe86556854bedf12307f

class UserManager:
    def __init__(self):
        self.user_list = []


    def addUser(self,user):
<<<<<<< HEAD
        
        user.password = self.hash_password(user.password)
        user.create_keys()
=======
        user.password = self.hash_password(user.password)
        user.create_keys()

>>>>>>> 9fe66f9087f8c2079a4dfe86556854bedf12307f
        self.user_list.append(user)
        tosave = []
        for i in range(0, len(self.user_list)):
            data = [self.user_list[i].username,
                    self.user_list[i].password,
                    self.user_list[i].role,]
            
            tosave.append(data)
        
        pwdFile = open(os.path.join(sys.path[0], "pwd.txt"), "a", newline="")
        with pwdFile:
            writer = csv.writer(pwdFile)
            writer.writerows(tosave)
           
        print("\nSaved user....\n")

             

    def find_user_with_id(self,toFind, pwd):
        with open(os.path.join(sys.path[0], "pwd.txt"), 'r') as pwdFile:        
            reader = csv.reader(pwdFile)
            for row in reader:
                if row[0] == toFind and self.check_password(row[1], pwd):
                    return int(row[2])
                else:
                    print("User not found")
                    return None

    def checkUser(self, toFind):
        
        with open(os.path.join(sys.path[0], "pwd.txt"), 'r', newline="") as pwdFile:
            reader = csv.reader(pwdFile)
            try:
                for row in reader:
                    if row[0] == toFind:
                        return True
            except IndexError:
                pass

    def deleteUser(self):
        print("Give username to delete: ")
        toFind = input()
        user_check = self.checkUser(toFind)
        if user_check:
            with open(os.path.join(sys.path[0], "pwd.txt"), 'r', newline="") as pwdFile:        
                data = list(csv.reader(pwdFile))
            
            with open(os.path.join(sys.path[0], "pwd.txt"), 'w', newline="") as pwdFile:
                writer = csv.writer(pwdFile)
                for row in data:
                    if row[0] != toFind:
                        writer.writerow(row)
            print("User deleted")
        else:
            print("No user found")
        
                            


    def create_password(self):
        length = 10
        lettersDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersDigits) for i in range (length))


    def hash_password(self, password):
        # uuid is used to generate a random number of the password
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ":" + salt

    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
        
       

           


<<<<<<< HEAD
    
=======
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

>>>>>>> 9fe66f9087f8c2079a4dfe86556854bedf12307f
