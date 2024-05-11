def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return "not defined" if y == 0 else x/y
        
print("-----------------------------Welcome to simple calculator-----------------------------")
count =  1
while count:
    num1  = float(input("Enter the number 1: "))
    num2  = float(input("Enter the number 2: "))
    opr = input("Enter the operation to be performed *,/,+,-: ")
    if   opr == '*': print(mul(num1,num2))     
    elif opr == '/': print(div(num1,num2))      
    elif opr == '+': print(add(num1,num2))
    elif opr == '-': print(sub(num1,num2))
    else           : print('Invalid operation')
    x = input("Do you want to calculate again? Type Y/N: ").upper()
    if x =='Y': 
        count = 1
        print()
    else:
        count = 0
        print("Thanks, visit again")
