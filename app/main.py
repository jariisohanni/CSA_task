from users.user_manager import UserManager
from users.user import User, Role
from msvcrt import getch
import getpass, sys



def testOK():
    return True

def main():
   
    print("**************************")
    print("WELCOME TO NÄSA AGENCY")
    print("**************************")
    print(" ")
   
#heti suoritettava koodi


    while loginPhase():
        pass



        ##VERIFY USER ID FROM USERS DATA BASE

        ##ASK FOR PASSWORD

        ##IF OK LIST USER FILES

def loginPhase():
    agent_id = ""
    logged_in = False
    pwd = ""

    while logged_in == False and agent_id != "exit":
            manager = UserManager()
            print("Please enter your agent id:")
            agent_id = input()
            pwd = mask_input()
            role = manager.find_user_with_id(agent_id, pwd)
            if role is not None:
                print("Access granted")
                if role == 1:
                    ans = True
                    while ans:
                        print("""
                        Please select function
                        1.Manage users
                        2.Access filesystem
                        4.Exit/Quit
                        """)
                        ans = input()
                        if ans=="1":
                            manageUsers()
                        elif ans=="2":
                          print("Something else")
                          logged_in == True
                        elif ans=="4":
                          print("Goodbye")
                          return None
                else:
                    print("Not admin")
            else:
                agent_id = ""

def mask_input(prompt='Password: '):
    '''
        Prompt for a password and masks the input.
        Returns the hashed string from the password entered by the user.
    '''
    if sys.stdin is not sys.__stdin__:
        return getpass.getpass(prompt)
    else:
        pwd = ""        
        sys.stdout.write(prompt)
        sys.stdout.flush()        
        while True:
            key = ord(getch())
            if key == 13: #Return Key
                sys.stdout.write('\n')
                return pwd
                break
            if key == 8: #Backspace key
                if len(pwd) > 0:
                    # Erases previous character.
                    sys.stdout.write('\b' + ' ' + '\b')                
                    sys.stdout.flush()
                    pwd = pwd[:-1]                    
            else:
                # Masks user input.
                char = chr(key)
                sys.stdout.write('*')
                sys.stdout.flush()                
                pwd = pwd + char
        return pwd    
        
def manageUsers():
    manager = UserManager()
    
    ans = True
    while ans:
        print("""
                        Please select function
                        1.Add user
                        2.Delete user
                        3.Return to main menu
                        """)
        ans = input()
        if ans=="1":
            print("Give username: ")
            un = input()
            print("Give user group (1 = admin, 2 = user): ")
            ur = input()            
            password = manager.create_password()
            print("This is the password for user " + un + " : " + password)
            user = User(un, password, ur)
            manager.addUser(user)
        elif ans=="2":
            
            if manager.deleteUser():
                print("toimii")
                
        elif ans=="3":
            ans = None
        else:
            print("Not Valid Choice Try again")

if __name__ == '__main__':
    main()

