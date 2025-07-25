import my_math
number1=int(input("Enter your number :"))
operator = input("Enter your operator (2,3) :")
if operator=="2":
   print(my_math.square(number1))
elif operator=="3":
    print(my_math.cube(number1))
