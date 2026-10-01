import random

def play_game():
    number = random.randint(1, 10)
    gues = 0
    chances = 3
    gues_counter = []

    while gues != number and len(gues_counter) < chances:
        try:
            gues = int(input(f"You have {chances - len(gues_counter)} chances to gues: "))

            if gues < 1 or gues > 10:
                print("Gues between 1 to 10")
            elif gues in gues_counter:
                print("You already tried this number")
            else:
                gues_counter.append(gues)

                if number > gues:
                    if chances - len(gues_counter) > 0:
                        print("Try to with big number")
                elif number < gues:
                    if chances - len(gues_counter) > 0:
                        print("Try to with small number")
                else:
                    print("Congratulations you gussed!")
                    print(f"{len(gues_counter)} times you was tested.")

        except ValueError:
            print("Please enter number!")

    if gues != number:
        print("Your chance is finish!!")
        print(f"Number was:{number}")

    print(f"You guessed numbers: {gues_counter}")

while True:
    play_game()
 
    again = input("Would you like to play again? (y/n): ").lower()
    
    if again != "y":
        break