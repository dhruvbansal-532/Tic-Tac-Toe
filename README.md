::: {align="center"}

# 🎮 Tic-Tac-Toe

### A classic game built with Python and Tkinter

A beginner-friendly desktop game where two players take turns placing
**X** and **O** on a 3 × 3 board. The game detects wins and draws,
highlights the winning cells, and lets you restart for another round.

`<br>`{=html}

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-Tkinter-2E8B57?style=for-the-badge)
![Project](https://img.shields.io/badge/Project-Beginner%20Friendly-8A63D2?style=for-the-badge)
:::

---

## 📸 Screenshots

> Add screenshots of your own running game to the `screenshots` folder,
> using the filenames below. The images will appear here automatically
> once you commit them to GitHub.

::: {align="center"}

---

               Game board                              Winning move

---

           ![Tic-Tac-Toe game                         ![Winning cells

board](screenshots/game-board.png) highlighted](screenshots/win-highlight.png)

        *The game ready to play*           *The three winning cells highlighted*

---

---

              Restarted game                           Draw result

---

                ![Restarted                               ![Draw

game](screenshots/restarted-game.png) result](screenshots/draw-result.png)

       *A fresh round after restart*           *The game reporting a draw*

---

:::

---

## ✨ Features

- 🧩 **Interactive 3 × 3 board** --- play locally with two players.
- 🔄 **Alternating turns** --- X and O take turns automatically.
- 🏆 **Win detection** --- checks rows, columns, and both diagonals.
- 🟩 **Winning-cell highlight** --- the three cells in a winning line
  turn green.
- 🤝 **Draw detection** --- recognizes when the board is full without
  a winner.
- 🔁 **Restart button** --- clears the board and starts a new round.
- 🎨 **Custom interface** --- midnight-blue background, light-blue
  cells, and clear status text.

## 🛠️ Built With

- **Python** --- game logic and event handling.
- **Tkinter** --- graphical user interface (included with many
  standard Python installations).

## 🚀 Getting Started

### 1. Check Python

Install Python if you don't already have it:
[python.org/downloads](https://www.python.org/downloads/).

Check that Python is available from your terminal:

```bash
python --version
```

On some systems, you may need:

```bash
python3 --version
```

### 2. Clone this repository

Replace `dhruvbansal-532` with your GitHub username and `Tic-Tac-Toe`
with the repository name:

```bash
git clone https://github.com/dhruvbansal-532/Tic-Tac-Toe.git
cd Tic-Tac-Toe
```

### 3. Run the game

Replace `script.py` below with the actual filename of your Python
file if it is different.

```bash
python script.py
```

On some systems:

```bash
python3 script.py
```

A desktop window should open. No internet connection is needed to play
after Python and the project files are available locally.

## 🎯 How to Play

1.  Run the Python file.
2.  Player **X** starts.
3.  Players take turns selecting an empty cell.
4.  Get three matching symbols in a row, column, or diagonal to win.
5.  If all nine cells are filled and nobody wins, the game is a draw.
6.  Select **Restart Game** to play again.

## 📂 Suggested Project Structure

Keep the Python file and screenshots organized like this:

```text
tic-tac-toe/
│
├── script.py
├── README.md
├── .gitignore
└── screenshots/
    ├── game-board.png
    ├── win-highlight.png
    ├── restarted-game.png
    └── draw-result.png
```

If your Python file has a different name, keep your existing filename
and update the run command above.

## 🧠 What I Practised

This project helped me practise:

- Python functions, conditions, loops, and lists.
- Working with Tkinter widgets and layout using `grid()`.
- Handling button clicks and callbacks.
- Passing arguments to functions.
- Detecting winning combinations and draws.
- Updating widget text and colours dynamically.
- Resetting the game state.

## 🔮 Possible Future Improvements

- Keep a score for X wins, O wins, and draws.
- Add a hover effect to the board cells.
- Add a single-player mode against a computer opponent.
- Add sound effects and more visual themes.

## 👤 Author

**DHRUV BANSAL**

- GitHub: [@dhruvbansal-532](https://github.com/dhruvbansal-532)

---

::: {align="center"}
**Built with Python, curiosity, and a lot of debugging. 💙**

If you found this project interesting, consider giving the repository a
⭐
:::
