# 🐍 12 Python Projects

A curated collection of **12 Python projects** ranging from beginner-friendly games to intermediate algorithm implementations. Each project is self-contained and designed to reinforce core Python concepts through hands-on practice.

---

## 📂 Project Overview

| # | Project | Category | Key Concepts |
|---|---------|----------|--------------|
| 01 | [Binary Search](#01-binary-search) | Algorithm | Recursion, Divide & Conquer |
| 02 | [Guess Number (User)](#02-guess-number-user) | Game | Loops, Random, User Input |
| 03 | [Guess Number (Computer)](#03-guess-number-computer) | Game | Logic, Feedback Loop |
| 04 | [Hangman](#04-hangman) | Game | Sets, String Manipulation |
| 05 | [Madlibs](#05-madlibs) | Fun | F-Strings, User Input |
| 06 | [Markov Chain Text Composer](#06-markov-chain-text-composer) | AI / NLP | Graphs, Probability, NLP |
| 07 | [Minesweeper](#07-minesweeper) | Game | OOP, 2D Arrays, Recursion |
| 08 | [Photo Manipulation](#08-photo-manipulation) | Image Processing | NumPy, Pixel Operations, Kernels |
| 09 | [Rock Paper Scissors](#09-rock-paper-scissors) | Game | Conditionals, Random |
| 10 | [Sudoku Solver](#10-sudoku-solver) | Algorithm | Backtracking, Recursion |
| 11 | [Tic Tac Toe](#11-tic-tac-toe) | Game | OOP, Game Loop |
| 12 | [Tic Tac Toe AI](#12-tic-tac-toe-ai) | AI / Game | Minimax Algorithm, OOP |

---

## 🚀 Getting Started

**Prerequisites:** Python 3.7+

```bash
# Clone the repository
git clone https://github.com/your-username/12-python-projects.git
cd 12-python-projects

# Most projects have no external dependencies — just run with Python!
python3 <project_folder>/<script_name>.py
```

> **Note:** The *Photo Manipulation* project requires `numpy`. Install it with:
> ```bash
> pip install numpy
> ```

---

## 📌 Project Details

---

### 01. Binary Search

**📁 Folder:** `Binary Search/`  
**▶️ Run:** `python3 binary_search.py`

A recursive implementation of the classic **Binary Search** algorithm. Given a sorted list, it efficiently locates a target element by repeatedly halving the search space.

- **Time Complexity:** O(log n)
- **Technique:** Divide and Conquer, Recursion
- **Returns:** Index of the target, or `-1` if not found

```python
# Example
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_search(l, 5)  # → 4
```

---

### 02. Guess Number (User)

**📁 Folder:** `Guess Number (User)/`  
**▶️ Run:** `python3 main.py`

A classic **number guessing game** where the computer picks a random number and the **user tries to guess it**. The program provides "too high" or "too low" hints after each guess.

- **Concepts:** `random` module, `while` loops, user input validation
- **Range:** 1 to 10 (configurable)

---

### 03. Guess Number (Computer)

**📁 Folder:** `Guess Number(Computer)/`  
**▶️ Run:** `python3 main.py`

The reverse of Project 02 — the **user thinks of a number** and the **computer guesses it**. The user responds with High (H), Low (L), or Correct (C), and the computer narrows down its range accordingly.

- **Concepts:** Interactive feedback loop, range narrowing logic
- **Demonstrates:** How a binary-search-like strategy can be applied to games

---

### 04. Hangman

**📁 Folder:** `Hangman/`  
**▶️ Run:** `python3 hangman.py`

The classic **Hangman word guessing game**. The computer picks a random word from a large word bank (`words.py`) and the player guesses letters one at a time with a limited number of lives.

- **Concepts:** Python `set` operations, string manipulation, `random` module
- **Features:**
  - Filters out words with hyphens or spaces
  - Tracks used letters and remaining lives (6 lives)
  - Displays current progress with blanks for unguessed letters

---

### 05. Madlibs

**📁 Folder:** `Madlibs/`  
**▶️ Run:** `python3 madlibs.py`

A fun, interactive **Madlibs-style story generator**. The user inputs a name, age, and programming language, and the program outputs a personalized story using Python **f-strings**.

- **Concepts:** String formatting, f-strings, user input
- **Bonus:** `random_madlibs.py` extends the concept with randomised templates from the `sample_madlibs/` folder

---

### 06. Markov Chain Text Composer

**📁 Folder:** `Markov Chain Text Composer/`  
**▶️ Run:** `python3 compose.py`

An **AI-powered text composer** that uses **Markov Chains** to learn word relationships from song lyrics and generate new, original (interpretive!) poetry. It models the probability of word transitions as a directed graph.

- **Concepts:** Graph theory, Markov Chains, NLP, probability
- **Files:**
  - `graph.py` — builds the Markov Chain graph from text
  - `compose.py` — traverses the graph to generate new text
  - `lyrics.py` — processes song lyric files
  - `songs/` — source text files used as vocabulary
- **Customization:** Edit `compose.py` to change output length or swap the input file

---

### 07. Minesweeper

**📁 Folder:** `Minesweeper/`  
**▶️ Run:** `python3 minesweeper.py`

A fully playable **terminal-based Minesweeper** game. The board is generated with randomly placed bombs, and the player digs cells by entering row/column coordinates.

- **Concepts:** OOP (`Board` class), 2D arrays, recursion (flood-fill for empty cells)
- **Features:**
  - Configurable board size and bomb count (default: 10×10, 10 bombs)
  - Auto-reveals neighbouring empty cells recursively
  - Displays remaining board on game over
- **Win Condition:** Uncover all non-bomb cells

```bash
# Default game
python3 minesweeper.py

# Custom board (modify the play() call)
play(dim_size=15, num_bombs=20)
```

---

### 08. Photo Manipulation

**📁 Folder:** `Photo Manipulation/`  
**▶️ Run:** `python3 transform.py`

A **from-scratch image processing library** built without PIL/OpenCV. Uses `numpy` to manipulate raw pixel arrays and apply various transformations.

- **Dependency:** `pip install numpy`
- **Transformations available:**
  | Function | Description |
  |----------|-------------|
  | `brighten(image, factor)` | Multiply pixel values by a factor |
  | `adjust_contrast(image, factor, mid)` | Shift contrast around a midpoint |
  | `blur(image, kernel_size)` | Box blur using a sliding window |
  | `apply_kernel(image, kernel)` | Convolve image with a custom kernel |
  | `combine_images(image1, image2)` | Merge two images (Sobel edge detection) |

- **Input:** PNG images in the `input/` folder
- **Output:** Processed images saved to the `output/` folder

---

### 09. Rock Paper Scissors

**📁 Folder:** `Rock Paper Scissors/`  
**▶️ Run:** `python3 main.py`

A simple **Rock Paper Scissors** game against the computer. The user picks `r`, `p`, or `s` and the computer makes a random choice. The winner is determined by classic game rules.

- **Concepts:** `random.choice()`, conditionals, function decomposition
- **Clean Design:** Win logic is separated into an `is_win()` helper function

---

### 10. Sudoku Solver

**📁 Folder:** `Sudoku Solver/`  
**▶️ Run:** `python3 sudoku.py`

An automatic **Sudoku puzzle solver** using the **Backtracking algorithm**. It fills in empty cells (represented as `-1`) by trying digits 1–9 and recursively validating each placement.

- **Concepts:** Backtracking, recursion, constraint satisfaction
- **Validation checks:** Row uniqueness, column uniqueness, 3×3 sub-grid uniqueness
- **Algorithm:** Returns `True` when the puzzle is fully solved, backtracks on failure

---

### 11. Tic Tac Toe

**📁 Folder:** `Tic Tac Toe/`  
**▶️ Run:** `python3 game.py`

A classic **two-player Tic Tac Toe** game in the terminal. Play as `X` against a `RandomComputerPlayer` that picks moves at random.

- **Concepts:** OOP (`TicTacToe`, `Player` classes), game loop, win detection
- **Features:**
  - Displays board with position numbers before the game starts
  - Detects wins across all rows, columns, and diagonals
  - Handles ties gracefully

---

### 12. Tic Tac Toe AI

**📁 Folder:** `Tic Tac Toe AI/`  
**▶️ Run:** `python3 game.py`

An upgraded Tic Tac Toe with an **unbeatable AI opponent** powered by the **Minimax algorithm**. The `GeniusComputerPlayer` evaluates every possible game state to always make the optimal move.

- **Concepts:** Minimax algorithm, game trees, recursive state evaluation, OOP
- **Players available:**
  | Class | Description |
  |-------|-------------|
  | `HumanPlayer` | Takes input from the terminal |
  | `RandomComputerPlayer` | Picks a random valid move |
  | `GeniusComputerPlayer` | Uses Minimax — **never loses** |

- **How Minimax works:** Recursively simulates all possible future moves, assigning scores based on win/loss/draw outcomes, then picks the move with the best guaranteed outcome.

---

## 🧠 Concepts Covered

```
✅ Recursion & Backtracking      ✅ Object-Oriented Programming
✅ Graph Theory & Markov Chains  ✅ Minimax / Game AI
✅ Image Processing (NumPy)      ✅ String & Set Operations
✅ Random & Probability          ✅ 2D Arrays & Grid Logic
✅ Algorithm Design              ✅ User Input Handling
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">
  <sub>Built with ❤️ using Python 3</sub>
</div>
