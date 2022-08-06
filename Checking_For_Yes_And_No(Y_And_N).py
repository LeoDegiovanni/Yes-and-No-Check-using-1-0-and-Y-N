x = str(input("Type N/n to say no, and Y/y to say yes: "))

while 1 == 1:  
    while len(x) == 0 or len(x) > 1:
        x = input("Type N/n to say no, and Y/y to say yes: ")   
        
    while not x == "Y":
        if x == "N" or x == "y" or x == "n":
            break
        x = input("Type N/n to say no, and Y/y to say yes: ")
    break

if x == "Y" or x == "y":
    print("You said yes!")
elif x == "N" or x == "n":
    print("You said no!")

