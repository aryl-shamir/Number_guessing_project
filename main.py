import random
from art import logo
print(logo)
print("welcome to the number guessing game ")
print("I'm thinking of a number between 1 and 100.")


lives = -1
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.choice(range(1, 101))
print(f"psst , The actual number is {number}") #Remove in production

game_over = False

if difficulty == "easy":
    lives = 10
else:
    lives = 5

while not game_over:


        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess != number:
            if guess in range(number+10, 101) :
                print("Too high")
            elif guess  in range(number-10, 0, -1):
                print("Too low")
            elif guess > number:
                print("Closely high")
            elif guess < number:
                print("closely low")

            lives -= 1

            if lives == 0:
                print("Game over. You've run out of life")
                print(f"The actual number is {number}")
                game_over = True
            else:
                print("Guess again")

        else:
            print("You got it. Congratulation!")
            print(f"{number} was the actual number!")
            game_over = True

