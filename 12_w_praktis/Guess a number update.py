
import random
def findnumber():
    
    number = random.randint(1,100)
    count=0
    while True :
        count+=1
        gest=int(input("Guess a number between 1 and 100:"))
        if gest>number:
            print( "Too high!")
        elif gest<number:
            print( "Too low!")
        else :
            return f"You guess is {number} is corect \n You guessed it in {count} tries!"
            
        
print(findnumber())
