import random
random_number= random.randrange(1,100)
number=int(input("Enter your guess a number between 1 and 100 :"))
while True:
    
    if number>random_number :
        print(f"{number} is too high !")
    elif number<random_number :
        print(f"{number} is too low !")
    elif number==random_number:
        print(f"***Your gouess number {number} is True***")
        break
    number= int(input("Enter Number again:"))