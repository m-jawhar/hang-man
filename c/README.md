# Hangman - C Implementation

A console-based hangman game written in C that demonstrates fundamental programming concepts including variables, loops, conditional statements, functions, and user input handling.

## Features

- Random word selection from built-in word bank
- Custom word mode for two players
- Visual hangman display
- Input validation and guess tracking
- 6 wrong guesses allowed before game over

## Build

Compile with GCC:

```bash
gcc hangman.c -o hangman
```

Or with Make (if you add a Makefile):

```bash
make
```

## Run

### Windows (PowerShell/Command Prompt)

```powershell
.\hangman.exe
```

### Linux/macOS

```bash
./hangman
```

## Game Instructions

1. Choose from the main menu:

   - Play with a random word from the word bank
   - Play with a custom word (2-player mode)
   - Exit

2. Guess one letter at a time
3. You have 6 incorrect guesses before losing
4. Win by guessing all letters before running out of tries

## Requirements

- GCC compiler (or any C compiler)
- Standard C library support
