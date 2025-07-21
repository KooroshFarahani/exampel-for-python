sum = 0
while True:
    number = int(input("Enter number for exit enter 0 :"))
    sum = number + sum
    print(f"Your sum is {sum}")
    if number == 0:
        break