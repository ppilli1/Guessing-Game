import random

print("Number Guessing Game")
number = random.randint(1,9)
chances = 5
print("Guess a number between 1 and 9")
while(chances > 0):
    guess = int(input("Enter your guess: "))
    if(guess == number):
        print("You won the game!")
        break
    elif(guess < number):
        print("Your guess is too low")
        print("Guess a higher number")
    else:
        print("Your guess is too high")
        print("Guess a lower number")
    chances -= 1
if(chances == 0):
    print("You lose the game!")

#print prime numbers before 50
#maybe define an integer list saying (0,50) and use modulus --> if __ % 2 == 1 then print num

