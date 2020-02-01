def testOK():
    return True

def main():
    print("**************************")
    print("WELCOME TO NÄSA AGENCY")
    print("**************************")
    print(" ")

    agent_id = ""
    logged_in = False
    while logged_in == False and agent_id != "exit":

        while agent_id == "":
            print("Please enter your agent id (or type exit):")
            agent_id = input()

        ##VERIFY USER ID FROM USERS DATA BASE

        ##ASK FOR PASSWORD

        ##IF OK LIST USER FILES


main()
