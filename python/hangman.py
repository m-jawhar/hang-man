"""
Hangman Game - Main Module
A text-based interactive Hangman game with OOP design.
"""

import random
import os


class HangmanDisplay:
    """Handles the visual representation of the hangman."""

    STAGES = [
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        GAME OVER!
        """,
    ]

    @staticmethod
    def get_stage(wrong_guesses):
        """Return the hangman stage based on wrong guesses."""
        stage_index = min(wrong_guesses, len(HangmanDisplay.STAGES) - 1)
        return HangmanDisplay.STAGES[stage_index]


class WordBank:
    """Manages the word list and word selection."""

    WORD_LIST = [
        "python",
        "javascript",
        "programming",
        "developer",
        "algorithm",
        "function",
        "variable",
        "database",
        "interface",
        "framework",
        "computer",
        "software",
        "hardware",
        "network",
        "security",
        "encryption",
        "debugging",
        "repository",
        "deployment",
        "terminal",
        "abstract",
        "inheritance",
        "polymorphism",
        "encapsulation",
        "recursion",
        "iteration",
        "compilation",
        "exception",
        "middleware",
    ]

    @staticmethod
    def get_random_word():
        """Return a random word from the word bank."""
        return random.choice(WordBank.WORD_LIST).upper()

    @staticmethod
    def add_words(words):
        """Add new words to the word bank."""
        WordBank.WORD_LIST.extend(words)


class Word:
    """Represents the secret word to be guessed."""

    def __init__(self, word):
        self.word = word.upper()
        self.letters = set(self.word)
        self.guessed_letters = set()

    def guess_letter(self, letter):
        """
        Add a guessed letter and return True if correct, False otherwise.
        """
        letter = letter.upper()
        self.guessed_letters.add(letter)
        return letter in self.letters

    def is_solved(self):
        """Check if the word has been completely guessed."""
        return self.letters.issubset(self.guessed_letters)

    def get_display(self):
        """Return the word with unguessed letters as underscores."""
        return " ".join(
            letter if letter in self.guessed_letters else "_" for letter in self.word
        )

    def get_word(self):
        """Return the original word."""
        return self.word


class Player:
    """Represents a player in the game."""

    def __init__(self, name="Player"):
        self.name = name
        self.score = 0
        self.games_played = 0
        self.games_won = 0

    def add_win(self):
        """Record a win for the player."""
        self.games_won += 1
        self.games_played += 1

    def add_loss(self):
        """Record a loss for the player."""
        self.games_played += 1

    def add_score(self, points):
        """Add points to player's score."""
        self.score += points

    def get_stats(self):
        """Return player statistics."""
        win_rate = (
            (self.games_won / self.games_played * 100) if self.games_played > 0 else 0
        )
        return {
            "name": self.name,
            "score": self.score,
            "games_played": self.games_played,
            "games_won": self.games_won,
            "win_rate": win_rate,
        }


class HangmanGame:
    """Main game controller for Hangman."""

    MAX_WRONG_GUESSES = 6

    def __init__(self, player=None):
        self.player = player if player else Player()
        self.word = None
        self.wrong_guesses = 0
        self.game_over = False
        self.won = False

    def start_new_game(self):
        """Initialize a new game."""
        self.word = Word(WordBank.get_random_word())
        self.wrong_guesses = 0
        self.game_over = False
        self.won = False

    def make_guess(self, letter):
        """
        Process a letter guess.
        Returns a tuple: (is_correct, message)
        """
        if not letter or len(letter) != 1 or not letter.isalpha():
            return None, "Please enter a single letter."

        letter = letter.upper()

        if letter in self.word.guessed_letters:
            return None, f"You already guessed '{letter}'. Try a different letter."

        is_correct = self.word.guess_letter(letter)

        if is_correct:
            if self.word.is_solved():
                self.won = True
                self.game_over = True
                self.player.add_win()
                points = (self.MAX_WRONG_GUESSES - self.wrong_guesses) * 10
                self.player.add_score(points)
                return True, f"Correct! You won! +{points} points"
            return True, f"Good guess! '{letter}' is in the word."
        else:
            self.wrong_guesses += 1
            if self.wrong_guesses >= self.MAX_WRONG_GUESSES:
                self.game_over = True
                self.player.add_loss()
                return False, f"Wrong! The word was: {self.word.get_word()}"
            return False, f"Sorry, '{letter}' is not in the word."

    def get_game_state(self):
        """Return the current game state for display."""
        return {
            "word_display": self.word.get_display(),
            "wrong_guesses": self.wrong_guesses,
            "max_guesses": self.MAX_WRONG_GUESSES,
            "guessed_letters": sorted(self.word.guessed_letters),
            "hangman_stage": HangmanDisplay.get_stage(self.wrong_guesses),
            "game_over": self.game_over,
            "won": self.won,
        }


class GameInterface:
    """Handles user interface and interaction."""

    @staticmethod
    def clear_screen():
        """Clear the terminal screen."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def display_header():
        """Display the game header."""
        print("\n" + "=" * 50)
        print("          HANGMAN GAME".center(50))
        print("=" * 50 + "\n")

    @staticmethod
    def display_game_state(game_state):
        """Display the current game state."""
        print(game_state["hangman_stage"])
        print(f"\nWord: {game_state['word_display']}")
        print(
            f"\nWrong guesses: {game_state['wrong_guesses']}/{game_state['max_guesses']}"
        )

        if game_state["guessed_letters"]:
            print(f"Guessed letters: {', '.join(game_state['guessed_letters'])}")
        else:
            print("Guessed letters: None yet")

    @staticmethod
    def display_player_stats(player):
        """Display player statistics."""
        stats = player.get_stats()
        print("\n" + "-" * 50)
        print(f"Player: {stats['name']}")
        print(
            f"Score: {stats['score']} | Games: {stats['games_played']} | Wins: {stats['games_won']}"
        )
        if stats["games_played"] > 0:
            print(f"Win Rate: {stats['win_rate']:.1f}%")
        print("-" * 50 + "\n")

    @staticmethod
    def get_user_input(prompt):
        """Get input from the user."""
        return input(prompt).strip()

    @staticmethod
    def display_message(message):
        """Display a message to the user."""
        print(f"\n>>> {message}")

    @staticmethod
    def display_welcome():
        """Display welcome message and rules."""
        GameInterface.clear_screen()
        print("\n" + "=" * 50)
        print("       WELCOME TO HANGMAN!".center(50))
        print("=" * 50)
        print("\nRULES:")
        print("  • Guess letters to reveal the hidden word")
        print("  • You have 6 wrong guesses before game over")
        print("  • Scoring: (6 - wrong_guesses) × 10 points")
        print("  • Enter 'quit' anytime to exit")
        print("\n" + "=" * 50)
        input("\nPress ENTER to start...")


def main():
    """Main game loop."""
    interface = GameInterface()
    interface.display_welcome()

    # Get player name
    interface.clear_screen()
    player_name = interface.get_user_input(
        "Enter your name (or press ENTER for 'Player'): "
    )
    player = Player(player_name if player_name else "Player")

    game = HangmanGame(player)
    playing = True

    while playing:
        # Start a new game
        game.start_new_game()

        while not game.game_over:
            interface.clear_screen()
            interface.display_header()
            interface.display_player_stats(player)

            game_state = game.get_game_state()
            interface.display_game_state(game_state)

            # Get user input
            guess = interface.get_user_input(
                "\nEnter a letter (or 'quit' to exit): "
            ).lower()

            if guess == "quit":
                playing = False
                break

            # Process the guess
            is_correct, message = game.make_guess(guess)

            if message:
                interface.clear_screen()
                interface.display_header()
                interface.display_player_stats(player)
                game_state = game.get_game_state()
                interface.display_game_state(game_state)
                interface.display_message(message)

                if game.game_over:
                    print()
                    input("Press ENTER to continue...")
                else:
                    import time

                    time.sleep(1.5)

        if not playing:
            break

        # Ask to play again
        interface.clear_screen()
        interface.display_player_stats(player)
        play_again = interface.get_user_input("Play again? (yes/no): ").lower()

        if play_again not in ["yes", "y"]:
            playing = False

    # Display final stats
    interface.clear_screen()
    print("\n" + "=" * 50)
    print("       THANKS FOR PLAYING!".center(50))
    print("=" * 50)
    interface.display_player_stats(player)
    print("\nGoodbye!\n")


if __name__ == "__main__":
    main()
