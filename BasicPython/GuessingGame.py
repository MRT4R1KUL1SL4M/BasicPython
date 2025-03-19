from random import randint
guess=int(input("Enter your guess number between 1 to 5: "))
randomNumber= randint(1,5)

if guess==randomNumber:
    print("Won")
else:
    print("Lose")
    print("Random number was :",randomNumber)