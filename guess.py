import random

print ("\n GUESS THE NUMBER GAME ")

n = random.randint(1,100)
no_tries = 5
player_name = input(" Enter a name :")
print(player_name," Guess the number between 1 to 100 :")

while no_tries >0:
    a = int(input())
    no_tries -=1 
    
    if n > a:
        print(" Its too low ")
    elif n< a:
        print(" its too high")
        
    elif a == n:
        print(" Congratulations you win ")
    
    if no_tries > 0:
        if n > 30:
            print(" HINT : its below 30 ")
        elif n < 30:
            print(" HINT : its is above 30")