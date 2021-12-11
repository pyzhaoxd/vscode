import getpass

try:
    u = getpass.getuser()
    while True:
        p = getpass.getpass("Enter your password: ")
        if p .lower() == "zhaoxd":
            print("Welcome!!!")
            break
        else:
            print("The password entered is incorrect!!!")

except Exception as error:
    print('ERROR',error)

else:
    print("Output-username: ",u)
    print("Password entered:", p)
    