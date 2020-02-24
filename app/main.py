from users.user_manager import UserManager
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

    while logged_in == False and agent_id != "exit":

        while agent_id == "":
            print("Please enter your agent id and password (or type exit:)")
            agent_id = input()
            pwd = mask_input()
            if manager.find_user_with_id(agent_id, pwd) is not None:
                print("Access granted")
                
            else:
                agent_id = ""

def mask_input(prompt='Password: '):
    '''
        Prompt for a password and masks the input.
        Returns the hashed string from the password entered by the user.
    '''

    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
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
                
        return hash_password(pwd)

if __name__ == '__main__':
    main()

