import random

def play_game():
    number = random.randint(1,10)
    guess = 0
    counter = 0

    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            counter += 1
            if guess < number:
                print("Enter a larger number.")
            elif guess > number:
                print("Enter a small number")
            else:
                print("Correct🎉")
                print(f" You reported it {counter} times")
        except  ValueError:
            print("Please enter only numbers!!")


while True:
    play_game()

    again = input("Would you like to play again? (y/n): ").lower()
    if again != "y":
        break
    
