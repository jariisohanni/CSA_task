
from app.users.user_manager import  UserManager


def testOK():
    return True

def main():
    print("**************************")
    print("WELCOME TO NÄSA AGENCY")
    print("**************************")
    print(" ")

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
            print("Please enter your agent id (or type exit):")
            agent_id = input()
            if user_manager.find_user_with_id(agent_id) is not None:
                print("Found user, logging in")
            else:
                agent_id = ""



#user_manager = UserManager()
#main()
