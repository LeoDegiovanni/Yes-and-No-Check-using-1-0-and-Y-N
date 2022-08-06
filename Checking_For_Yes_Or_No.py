x = str(input("Type 0 to say no, and 1 to say yes: "))

while 1 == 1:  
    while len(x) == 0 or len(x) > 1:
        x = str(input("Type 0 to say no, and 1 to say yes: "))
    
    x = int(x)   
        
    while x < 0 or x > 1:
            x = int(input("Type 0 to say no, and 1 to say yes: "))
    break

x = int(x)

if x == 1:
    print("You said yes!")
elif x == 0:
    print("You said no!")
