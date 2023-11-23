def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1-n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
print("CALCULATOR")
print("PRESS 1 FOR ADDITION \nPRESS 2 FOR SUBTRACTION \nPRESS 3 FOR MULTIPLICATION\nPRESS 4 FOR DIVISION")
choice=int(input("ENTER YOUR CHOICE : "))
if choice<=4 and choice>=1:
    num1=int(input("ENTER YOUR FIRST NUMBER : "))
    num2=int(input("ENTER YOUR SECOND NUMBER : "))
    if choice==1:
        print("ADDITION OF TWO NUMBERS :",addition(num1,num2))
    elif choice==2:
        print("SUBTRACTION OF TWO NUMBERS :",subtraction(num1,num2))
    elif choice==3:
        print("MULTIPLICATION OF TWO NUMBERS :",multiplication(num1,num2))
    elif choice==4:
        print("DIVISION OF TWO NUMBERS :",division(num1,num2))
else:
    print("INVALID CHOICE")