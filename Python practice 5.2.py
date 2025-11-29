def check_number(x):
    if x>0:
        print("The number is positive")
    elif x==0:
        print("The number is zero")
    else:
        print("The number is negative")
x=(int(input("Enter the number:")))
check_number(x)