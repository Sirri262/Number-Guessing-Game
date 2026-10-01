import random

def play_game():
    number = random.randint(1, 10)
    guess = 0
    chances = 3
    guessed_numbers = []

    while guess != number and len(guessed_numbers) < chances:
        try:
            guess = int(input(f"You have {chances - len(guessed_numbers)} chances left. Enter your guess: "))

            if guess < 1 or guess > 10:
                print("Guess a number between 1 and 10")
            elif guess in guessed_numbers:
                print("You already tried this number")
            else:
                guessed_numbers.append(guess)

                if number > guess:
                    if chances - len(guessed_numbers) > 0:
                        print("Try a bigger number")
                elif number < guess:
                    if chances - len(guessed_numbers) > 0:
                        print("Try a smaller number")
                else:
                    print("Congratulations! You guessed it!")
                    print(f"You guessed it in {len(guessed_numbers)} attempts")

        except ValueError:
            print("Please enter a number!")

    if guess != number:
        print("You are out of chances!")
        print(f"The number was: {number}")

    print(f"You guessed numbers: {guessed_numbers}")

while True:
    play_game()
 
    again = input("Would you like to play again? (yes/no): ").lower()
    
    while again != "yes" and again != "no":
        again = input("Please enter only yes or no: ").lower()
        
    if again == "no":
        break
        