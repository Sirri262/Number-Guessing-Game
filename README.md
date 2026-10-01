# 🎯 Number Guessing Game (Python)

A beginner-friendly Python project where the computer generates a random number and the user tries to guess it.

This project was created to practice core Python concepts such as loops, conditionals, functions, lists, input validation, and error handling.

---

## 🧩 How the Game Works

- The computer selects a random number between 1 and 10.
- The player has 3 valid attempts to guess the number.
- After each valid guess, the program gives feedback:
  - "Try a bigger number"
  - "Try a smaller number"
- Numbers outside the 1–10 range are not accepted.
- Repeated guesses do not use an attempt.
- Invalid inputs such as letters are handled with `try / except`.
- The game stores the numbers guessed by the player.
- If the player guesses correctly, the game shows how many attempts were used.
- If the player uses all 3 attempts, the correct number is displayed.
- At the end of the game, the player can choose to play again or exit.
- The program only accepts `yes` or `no` for the replay option.

---

## ✨ Features

- Random number generation
- 3-attempt limit
- User input validation
- Error handling using `try / except`
- Repeated guess detection
- Guessed numbers tracking
- Bigger / smaller number hints
- Replay option
- Function-based game structure
- Clean and beginner-friendly Python code

---

## ▶️ How to Run

1. Make sure Python is installed on your computer.
2. Clone this repository or download the project files.
3. Open the project folder in a terminal.
4. Run the game with:

```bash
python main.py