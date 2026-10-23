# 🔢 Centry

**A command-line number guessing game where you track down a secret number between 1 and 100 before your attempts run out.**

Centry is a simple guessing game for the terminal. The computer thinks of a random number from 1 to 100, you pick a difficulty, and every guess gets a "Too High" or "Too Low" hint. Find the number within your allowed attempts to win.

---

## ✨ Features

- 🎯 **Random secret number**: a new number between 1 and 100 is picked every time you run the game
- 🎚️ **Two difficulty levels**: Easy gives you 10 attempts, Hard gives you 5
- 💡 **Instant hints**: every wrong guess tells you whether it was too high or too low
- 🔢 **Attempts counter**: shows how many attempts you have left before each guess
- ✅ **Difficulty validation**: the game keeps asking until you type `easy` or `hard`
- 🎨 **ASCII art logo**: a custom title banner shown when the game starts
- 🏁 **Clear endings**: a win message that reveals the number, or a loss message when you run out of attempts
- 🛡️ **Input validation**: typing something that isn't a number asks you again instead of crashing, and doesn't cost you an attempt

---

## 🛠️ Tech Stack

- **Python 3**: built entirely on the standard library (`random`)

---

## 📁 Project Structure

```
centry/
├── code.py              # Full game logic
├── LICENSE
└── README.md
```

---

## ▶️ Getting Started

### Prerequisites
- Python 3 (pure standard library, nothing else needed)

### Running It

```
git clone https://github.com/rhitamcoder/centry.git
```
```
cd centry
```
```
python code.py
```

Choose `easy` or `hard`, then type a number between 1 and 100 on each turn. Use the hints to narrow it down before you run out of attempts.

---

## 🧠 How It Works

- **`random.randint(1, 100)`** picks the secret number once when the game starts
- **The difficulty prompt** loops until you type `easy` or `hard`
- **`play_game(attempts_allowed)`** is the core loop:
  - Each turn shows your remaining attempts and asks for a guess
  - Invalid input (like letters) is caught with `try/except` and the prompt repeats
  - A guess above the secret number prints "Too High", and a guess below it prints "Too Low"
  - A correct guess reveals the answer and ends the game
  - If you use your last attempt without guessing correctly, the game ends with a loss message
- **Easy mode** calls `play_game(10)` and **Hard mode** calls `play_game(5)`

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
