#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_WORD_LENGTH 50
#define MAX_TRIES 6

// Function prototypes
void displayWelcome();
void displayMenu();
void displayHangman(int wrongGuesses);
void displayWord(const char* word, const char* guessed, int length);
int playGame(const char* word);
void displayGameOver(int won, const char* word);
char getGuess(const char* alreadyGuessed);
int isLetterInWord(char letter, const char* word);
void addToGuessed(char* guessed, char letter);
int hasWon(const char* word, const char* guessed);

// Word bank for the game
const char* wordBank[] = {"programming", "computer",  "keyboard",  "function",
                          "variable",    "algorithm", "database",  "network",
                          "software",    "hardware",  "developer", "debugging",
                          "compiler",    "memory",    "processor"};

int main() {
  int choice;
  int playAgain = 1;

  srand(time(NULL));  // Seed random number generator

  displayWelcome();

  while (playAgain) {
    displayMenu();
    printf("Enter your choice: ");
    scanf("%d", &choice);
    getchar();  // Clear newline

    switch (choice) {
      case 1: {
        // Play with random word
        int randomIndex = rand() % (sizeof(wordBank) / sizeof(wordBank[0]));
        const char* selectedWord = wordBank[randomIndex];
        int won = playGame(selectedWord);
        displayGameOver(won, selectedWord);
        break;
      }
      case 2: {
        // Play with custom word
        char customWord[MAX_WORD_LENGTH];
        printf("\nEnter a word for player 2 to guess: ");
        fgets(customWord, MAX_WORD_LENGTH, stdin);
        customWord[strcspn(customWord, "\n")] = 0;  // Remove newline

        // Convert to lowercase
        for (int i = 0; customWord[i]; i++) {
          customWord[i] = tolower(customWord[i]);
        }

// Clear screen (works on most systems)
#ifdef _WIN32
        system("cls");
#else
        system("clear");
#endif

        int won = playGame(customWord);
        displayGameOver(won, customWord);
        break;
      }
      case 3:
        printf("\nThanks for playing! Goodbye!\n");
        playAgain = 0;
        break;
      default:
        printf("\nInvalid choice! Please try again.\n\n");
    }

    if (playAgain && choice != 3) {
      printf("\nPlay again? (1 = Yes, 0 = No): ");
      scanf("%d", &playAgain);
      getchar();  // Clear newline
      printf("\n");
    }
  }

  return 0;
}

void displayWelcome() {
  printf("\n");
  printf("========================================\n");
  printf("    WELCOME TO HANGMAN GAME!\n");
  printf("========================================\n");
  printf("\nGuess the word one letter at a time.\n");
  printf("You have %d wrong guesses before you lose!\n\n", MAX_TRIES);
}

void displayMenu() {
  printf("========================================\n");
  printf("             MAIN MENU\n");
  printf("========================================\n");
  printf("1. Play with Random Word\n");
  printf("2. Play with Custom Word (2 Players)\n");
  printf("3. Exit\n");
  printf("========================================\n");
}

void displayHangman(int wrongGuesses) {
  printf("\n");
  printf("  +---+\n");
  printf("  |   |\n");

  if (wrongGuesses >= 1) {
    printf("  O   |\n");
  } else {
    printf("      |\n");
  }

  if (wrongGuesses >= 4) {
    printf(" /|\\  |\n");
  } else if (wrongGuesses >= 3) {
    printf(" /|   |\n");
  } else if (wrongGuesses >= 2) {
    printf("  |   |\n");
  } else {
    printf("      |\n");
  }

  if (wrongGuesses >= 6) {
    printf(" / \\  |\n");
  } else if (wrongGuesses >= 5) {
    printf(" /    |\n");
  } else {
    printf("      |\n");
  }

  printf("      |\n");
  printf("=========\n");
  printf("\nWrong guesses: %d / %d\n", wrongGuesses, MAX_TRIES);
}

void displayWord(const char* word, const char* guessed, int length) {
  printf("\nWord: ");
  for (int i = 0; i < length; i++) {
    if (strchr(guessed, word[i]) != NULL) {
      printf("%c ", word[i]);
    } else {
      printf("_ ");
    }
  }
  printf("\n");
}

int playGame(const char* word) {
  int wordLength = strlen(word);
  char guessed[27] = "";  // Store guessed letters
  int wrongGuesses = 0;
  int won = 0;

  printf("\n========================================\n");
  printf("         GAME STARTED!\n");
  printf("========================================\n");

  while (wrongGuesses < MAX_TRIES && !won) {
    displayHangman(wrongGuesses);
    displayWord(word, guessed, wordLength);

    if (strlen(guessed) > 0) {
      printf("\nGuessed letters: %s\n", guessed);
    }

    char guess = getGuess(guessed);

    if (isLetterInWord(guess, word)) {
      printf("\nCorrect! '%c' is in the word.\n", guess);
      addToGuessed(guessed, guess);

      if (hasWon(word, guessed)) {
        won = 1;
      }
    } else {
      printf("\nWrong! '%c' is not in the word.\n", guess);
      addToGuessed(guessed, guess);
      wrongGuesses++;
    }

    printf("\n");
  }

  // Display final state
  displayHangman(wrongGuesses);
  displayWord(word, guessed, wordLength);

  return won;
}

char getGuess(const char* alreadyGuessed) {
  char guess;
  int valid = 0;

  while (!valid) {
    printf("\nEnter your guess (a-z): ");
    scanf(" %c", &guess);
    getchar();  // Clear newline

    guess = tolower(guess);

    if (!isalpha(guess)) {
      printf("Invalid input! Please enter a letter.\n");
    } else if (strchr(alreadyGuessed, guess) != NULL) {
      printf("You already guessed '%c'! Try another letter.\n", guess);
    } else {
      valid = 1;
    }
  }

  return guess;
}

int isLetterInWord(char letter, const char* word) {
  return strchr(word, letter) != NULL;
}

void addToGuessed(char* guessed, char letter) {
  int len = strlen(guessed);
  guessed[len] = letter;
  guessed[len + 1] = '\0';
}

int hasWon(const char* word, const char* guessed) {
  for (int i = 0; word[i] != '\0'; i++) {
    if (strchr(guessed, word[i]) == NULL) {
      return 0;
    }
  }
  return 1;
}

void displayGameOver(int won, const char* word) {
  printf("\n========================================\n");
  if (won) {
    printf("    CONGRATULATIONS! YOU WON!\n");
    printf("========================================\n");
    printf("\nYou guessed the word: %s\n", word);
  } else {
    printf("        GAME OVER!\n");
    printf("========================================\n");
    printf("\nThe word was: %s\n", word);
    printf("Better luck next time!\n");
  }
}
