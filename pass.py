def main():
    savedUsername, savedPassword = getUsernameAndPassword()
    
    while True:
        if infoIsValid(savedUsername, savedPassword):
            print ('Welcome')
            break
        else:
            print("Sorry, try again\n\n")

    while True:
       print('\n\t\t\tOptions\n')

       options = int(raw_input('1 Change Password \n2 End \n\n'))
       if options == 1:
           changePassword(savedUsername)

       elif options == 2:
           print('ending')
           return 0

def getUsernameAndPassword(filename='info.dat'):
    fin = open(filename, 'r')
    name = fin.readline()[:-1]
    password = fin.readline()[:-1]
    fin.close()
    return name,password

def infoIsValid(savedUsername,savedPassword):
    username = raw_input("Username:")
    password = raw_input("Password:")
    return username == savedUsername and password == savedPassword
    
def changePassword(username, filename='info.dat'):
    fout = open(filename, 'w')
    x = raw_input('New password\n')
    fout.write(username+'\n')
    fout.write(x+'\n')
    fout.close()


if __name__ == "__main__":
    main()
