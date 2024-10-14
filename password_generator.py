import random as r

a =int(1)
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
character = uppercase + lowercase + digits + special 
while a != 0:
    password =""
    l = int(input("Enter Password Length You Want : "))

    for i in range(l):
        password+= r.choice(character)
    print(f"The Password Is : {password}\n")
    a = int(input("Enter  0 to exit or any key to continue : "))
    
        