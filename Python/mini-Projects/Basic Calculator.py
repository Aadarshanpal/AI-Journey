#Basic Calculator 
Ans = 0
def addition(x,y):
    return x+y

def substraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

while True:
    op = input("Enter the operation to be performed i.e +,-,*,/ or press & to quit: ")
    if op == "&":
        break
    while True:
        x = input("Enter the first number or Ans for previous Ans: ")
        try:
            x = float(x)
            break
        except:
            if x == "Ans":
                x = Ans
                break
            print("Enter a Valid data(only int and float allowed or Ans)")
            continue
    while True:
        y = input("Enter the second number: ")
        try:
            y = float(y)
            break
        except:
            print("Enter a Valid data(only int and float allowed or Ans)")
            continue
    if op == "+":
        Ans = addition(x,y)
    elif op == "-":
        Ans = substraction(x,y)
    elif op == "*":
        Ans = multiplication(x,y)
    elif op == "/":
        if y == 0:
            print("Cant divide by 0.\n")
            continue
        Ans = division(x,y)
    else:
        print("Enter valid operation please.\n\n")
        continue
    print("The result of",x,""+ op +"",y,"is:",Ans)