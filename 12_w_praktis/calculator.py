def plus (n1,n2):
    #jam 
    return n1+n2
def Coefficient (n1,n2):
    #zarb 
    return n1*n2
def division (n1,n2):
    #taghsim
    return n1/n2
def subtraction (n1,n2):
    #menha
    return n1-n2

oprator=input("Enter operation (+, -, *, /):")
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
if oprator=="+":
    print (f"Result: {plus(n1,n2)}")
elif oprator=="-":
    print (f"Result: {subtraction(n1,n2)}")
elif oprator=="*":
    print (f"Result: {Coefficient(n1,n2)}")
elif oprator=="-":
    print (f"Result: {Coefficient(n1,n2)}")
elif oprator=="/":
    print (f"Result: {division(n1,n2)}")