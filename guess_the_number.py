import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 10.")
    print("You have 3 attempts to guess it correctly.")

    # Computer selects a random number
    number = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number!")
        
        if attempts == max_attempts and guess != number:
            print(f"Sorry, you've used all your attempts. The correct number was {number}. Better luck next time!")
            break

if __name__ == "__main__":
    guess_the_number()
