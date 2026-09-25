
################################# calculator code
def add(x,y):
    print(x+y)
def subtract(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)

print("welcome to my awesome calc app only 69.99")
print("What math we doing man")

while(True):
    print("Type (a)dd (s)ubtract (m)ultiply (d)ivide (q)uit")
    user_choice = input(": ")
############## addition ###################
    if user_choice == 'a':
        x = int(input("enter the first number"))
        y = int(input("enter the second number"))
        add(x,y)

############# subtraction #################
    elif user_choice == 's':
        x = int(input("enter the first number"))
        y = int(input("enter the second number"))
        subtract(x,y)

############# multiplication ###############
    elif user_choice == 'm':
        x = int(input("enter the first number"))
        y = int(input("enter the second number"))
        multiply(x,y)

############# divide #######################
    elif user_choice == 'd':
        x = int(input("enter the first number"))
        y = int(input("enter the second number"))
        divide(x,y)
    elif user_choice == 'q':
        break
    else:
        print("Try Again")



