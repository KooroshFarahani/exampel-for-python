try:
    operation=input("Enter operation:")
    first=int(input("Enter first number:"))
    second=int(input("Enter first number:"))
    
    if operation=="*":
        result=first*second
        print(result)
    elif operation=="/":
        result=first/second
        print(result)
    elif operation=="+":
        result=first+second
        print(result)
    elif operation=="-":
        result=first-second
        print(result)
except :
    pass