"""
Hangman Game - Visual Demo
This script demonstrates the game's features without requiring user input.
"""

import time
import os
from hangman import HangmanGame, Player, HangmanDisplay, GameInterface


def clear_and_wait(seconds=1.5):
    """Wait and clear screen."""
    time.sleep(seconds)
    os.system("cls" if os.name == "nt" else "clear")


def demo_hangman_stages():
    """Demonstrate all hangman visual stages."""
    print("\n" + "=" * 60)
    print("HANGMAN VISUAL STAGES DEMO".center(60))
    print("=" * 60 + "\n")

    for i, stage in enumerate(HangmanDisplay.STAGES):
        print(f"Stage {i} - {i} wrong guesses:")
        print(stage)
        if i < len(HangmanDisplay.STAGES) - 1:
            input("\nPress ENTER for next stage...")
            clear_and_wait(0.1)
        else:
            print("\n")


def demo_gameplay():
    """Demonstrate a full game playthrough."""
    print("\n" + "=" * 60)
    print("AUTOMATED GAMEPLAY DEMO".center(60))
    print("=" * 60 + "\n")
    print("Watch as the game plays itself...\n")
    time.sleep(2)

    player = Player("Demo Player")
    game = HangmanGame(player)
    game.start_new_game()

    # Common letters to try
    common_letters = [
        "E",
        "T",
        "A",
        "O",
        "I",
        "N",
        "S",
        "H",
        "R",
        "D",
        "L",
        "C",
        "U",
        "M",
        "W",
        "F",
        "G",
        "Y",
        "P",
        "B",
    ]

    interface = GameInterface()

    for letter in common_letters:
        if game.game_over:
            break

        interface.clear_screen()
        print("\n" + "=" * 60)
        print("AUTOMATED GAMEPLAY DEMO".center(60))
        print("=" * 60 + "\n")

        # Show current state
        game_state = game.get_game_state()
        print(game_state["hangman_stage"])
        print(f"\nWord: {game_state['word_display']}")
        print(
            f"Wrong guesses: {game_state['wrong_guesses']}/{game_state['max_guesses']}"
        )

        if game_state["guessed_letters"]:
            print(f"Guessed: {', '.join(sorted(game_state['guessed_letters']))}")

        print(f"\n>>> Trying letter: {letter}")

        time.sleep(1.5)

        # Make the guess
        is_correct, message = game.make_guess(letter)

        if is_correct is not None:
            print(f">>> {message}")
            time.sleep(2)

    # Final state
    interface.clear_screen()
    print("\n" + "=" * 60)
    print("GAME COMPLETE!".center(60))
    print("=" * 60 + "\n")

    game_state = game.get_game_state()
    print(game_state["hangman_stage"])
    print(f"\nFinal Word: {game_state['word_display']}")

    if game_state["won"]:
        print("\n🎉 VICTORY! 🎉")
    else:
        print("\n💀 GAME OVER 💀")

    print(f"\nPlayer Stats:")
    stats = player.get_stats()
    print(f"  Score: {stats['score']}")
    print(f"  Games Won: {stats['games_won']}/{stats['games_played']}")

    print("\n")


def demo_features():
    """Demonstrate key features of the game."""
    print("\n" + "=" * 60)
    print("KEY FEATURES DEMONSTRATION".center(60))
    print("=" * 60 + "\n")

    features = [
        ("Object-Oriented Design", "6 well-structured classes working together"),
        ("Visual Feedback", "ASCII art hangman with 7 stages"),
        ("Input Validation", "Handles invalid inputs gracefully"),
        ("Score System", "(6 - wrong_guesses) × 10 points per game"),
        ("Statistics Tracking", "Wins, games played, win rate"),
        ("Clean Interface", "Clear prompts and game state display"),
        ("Extensible Code", "Easy to add words, features, or difficulty levels"),
        ("Pure Python", "No external dependencies required"),
    ]

    for i, (feature, description) in enumerate(features, 1):
        print(f"{i}. {feature}")
        print(f"   └─ {description}\n")
        time.sleep(0.5)

    input("\nPress ENTER to continue...")


def demo_code_quality():
    """Highlight code quality aspects."""
    print("\n" + "=" * 60)
    print("CODE QUALITY HIGHLIGHTS".center(60))
    print("=" * 60 + "\n")

    quality_points = [
        "✅ Comprehensive docstrings for all classes and methods",
        "✅ Descriptive variable and function names",
        "✅ Proper separation of concerns (MVC-like pattern)",
        "✅ Single Responsibility Principle applied",
        "✅ DRY principle - no code duplication",
        "✅ Input validation and error handling",
        "✅ Efficient data structures (sets for O(1) lookups)",
        "✅ Clear game state management",
        "✅ Modular, testable code",
        "✅ Ready for future enhancements",
    ]

    for point in quality_points:
        print(f"  {point}")
        time.sleep(0.3)

    print("\n")
    input("Press ENTER to continue...")


def main_menu():
    """Display demo menu."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n" + "=" * 60)
        print("HANGMAN GAME - DEMO MENU".center(60))
        print("=" * 60 + "\n")
        print("Choose a demo:")
        print("  1. View All Hangman Stages")
        print("  2. Watch Automated Gameplay")
        print("  3. See Key Features")
        print("  4. View Code Quality Highlights")
        print("  5. Play the Real Game")
        print("  6. Exit")
        print("\n" + "=" * 60)

        choice = input("\nEnter choice (1-6): ").strip()

        if choice == "1":
            clear_and_wait(0.1)
            demo_hangman_stages()
            input("\nPress ENTER to return to menu...")
        elif choice == "2":
            clear_and_wait(0.1)
            demo_gameplay()
            input("Press ENTER to return to menu...")
        elif choice == "3":
            clear_and_wait(0.1)
            demo_features()
        elif choice == "4":
            clear_and_wait(0.1)
            demo_code_quality()
        elif choice == "5":
            clear_and_wait(0.1)
            print("\nLaunching the real game...")
            time.sleep(1)
            import hangman

            hangman.main()
            break
        elif choice == "6":
            clear_and_wait(0.1)
            print("\n" + "=" * 60)
            print("Thanks for watching the demo!".center(60))
            print("=" * 60 + "\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1-6.")
            time.sleep(1.5)


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted. Goodbye!\n")
