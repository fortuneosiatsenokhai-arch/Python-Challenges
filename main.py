import random

def intro():
    global name, number
    number = random.randint(1, 100)
    print("May I know your name?")
    name = input(": ")
    print(f"Hi {name}, we are going to play a game. Guess a number between 1 and 100")
    x = "even" if number % 2 == 0 else "odd"
    print(f"This is an {x} number")
    print("Go ahead and guess!")

def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        enter = input("Guess: ")
        try:
            guess = int(enter)
            if 1 <= guess <= 100:
                guessesTaken += 1
                if guess < number:
                    print("Too low")
                elif guess > number:
                    print("Too high")
                else:
                    print(f"Good job {name}, you guessed right!! The number is {number}")
                    return
                if guessesTaken < 6:
                    print("Try again!")
            else:
                print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 100")
        except ValueError:
            print(f"I don't think that {enter} is a number. Sorry")
    print(f"Nope, the number I was thinking of was {number}")

playAgain = "yes"
while playAgain.lower() in ["yes", "y"]:
    intro()
    pick()
    playAgain = input("Do you want to play again? ")
