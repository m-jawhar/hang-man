# Hangman Game

A text-based, interactive Hangman game built with Python, demonstrating object-oriented programming principles and clean code architecture.

## 🎮 Features

- **Complete Game Logic**: Fully functional Hangman game with all rules implemented
- **Object-Oriented Design**: Clean architecture using multiple classes:
  - `HangmanGame`: Main game controller
  - `Word`: Manages the secret word and guessed letters
  - `Player`: Tracks player statistics and scores
  - `HangmanDisplay`: Handles visual representation
  - `WordBank`: Manages word selection
  - `GameInterface`: Handles user interaction
- **User-Friendly Interface**: Clean command-line interface with clear prompts and feedback
- **Scoring System**: Earn points based on performance
- **Player Statistics**: Track wins, games played, and win rate
- **Replayability**: Play multiple rounds and track progress

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone or download this repository
2. Navigate to the Python directory:
   ```bash
   cd hang-man/python
   ```

### Running the Game

Simply run the main Python file:

```bash
python hangman.py
```

### Viewing the Demo

See automated demonstrations of all features:

```bash
python demo.py
```

### Running Examples

See programmatic usage examples:

```bash
python examples.py
```

## 📖 How to Play

1. **Start the Game**: Run `python hangman.py`
2. **Enter Your Name**: Personalize your gaming experience
3. **Guess Letters**: Enter one letter at a time to guess the word
4. **Win Condition**: Reveal all letters before running out of guesses
5. **Lose Condition**: Make 6 wrong guesses and the game is over

### Scoring

- Points are awarded based on performance
- Formula: `(6 - wrong_guesses) × 10 points`
- Perfect game (no wrong guesses): 60 points
- Track your total score across multiple games

## 🏗️ Project Structure

```
python/
│
├── hangman.py          # Main game file with all classes
├── demo.py             # Interactive demo showcasing features
├── examples.py         # Programmatic usage examples
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (none required)
```

## 💡 Technical Highlights

### Object-Oriented Design

The game demonstrates key OOP principles:

1. **Encapsulation**: Each class manages its own data and behavior

   - `Word` class encapsulates word-related logic
   - `Player` class manages player data
   - `HangmanDisplay` handles visual representation

2. **Separation of Concerns**: Different aspects of the game are separated into distinct classes

   - Game logic (`HangmanGame`)
   - User interface (`GameInterface`)
   - Data management (`WordBank`, `Word`)

3. **Single Responsibility Principle**: Each class has one clear purpose

### Key Programming Concepts

- **Conditional Statements**: Game logic uses if/else for decision making
- **Loops**: While loops control game flow
- **Functions/Methods**: Modular code with clear responsibilities
- **Data Structures**: Sets for efficient letter tracking, lists for word storage
- **String Manipulation**: Word display and formatting

## 🎯 Learning Outcomes

This project demonstrates:

- Building a complete, functional application from scratch
- Implementing game logic with proper state management
- Creating an intuitive user interface
- Using object-oriented programming effectively
- Breaking down complex problems into manageable components
- Writing clean, maintainable, and well-documented code

## 🔧 Customization

### Adding More Words

You can extend the word bank by modifying the `WORD_LIST` in the `WordBank` class or using the `add_words()` method:

```python
WordBank.add_words(["newword1", "newword2", "newword3"])
```

### Adjusting Difficulty

Modify `MAX_WRONG_GUESSES` in the `HangmanGame` class to change difficulty:

- Easier: Increase to 7 or 8
- Harder: Decrease to 5 or 4

## 📝 Future Enhancements

Potential features to add:

- [ ] Difficulty levels (easy, medium, hard)
- [ ] Categories for words
- [ ] Hint system
- [ ] Multiplayer mode
- [ ] High score persistence (save to file)
- [ ] Word definitions after game ends
- [ ] Timed mode
- [ ] Custom word lists from files

## 👤 Author

Created as a project to demonstrate Python programming skills and software design principles.

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Built as part of a project to showcase programming fundamentals
- Demonstrates practical application of OOP concepts
- Designed with clean code principles in mind
