"""
Hangman Game - Quick Start Guide

This is a simple example to demonstrate how to use the game classes
programmatically or extend them.
"""

from hangman import HangmanGame, Player, WordBank, GameInterface


def example_programmatic_usage():
    """
    Example: Using the game programmatically without the interactive UI
    """
    print("=== Programmatic Usage Example ===\n")

    # Create a player
    player = Player("Alice")

    # Create a game
    game = HangmanGame(player)
    game.start_new_game()

    # Simulate some guesses
    test_guesses = ["E", "A", "R", "T", "O", "I", "N"]

    for letter in test_guesses:
        if game.game_over:
            break

        _, message = game.make_guess(letter)
        game_state = game.get_game_state()

        print(f"Guess: {letter}")
        print(f"Word: {game_state['word_display']}")
        print(f"Result: {message}")
        print(
            f"Wrong guesses: {game_state['wrong_guesses']}/{game_state['max_guesses']}"
        )
        print()

    # Display final stats
    print("\nFinal Player Stats:")
    stats = player.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")


def example_custom_word_bank():
    """
    Example: Using a custom word bank
    """
    print("\n=== Custom Word Bank Example ===\n")

    # Add custom words to the word bank
    custom_words = ["portfolio", "python", "developer", "creative"]
    WordBank.add_words(custom_words)

    print(f"Total words in bank: {len(WordBank.WORD_LIST)}")
    print(f"Sample words: {WordBank.WORD_LIST[:5]}")


def example_game_integration():
    """
    Example: Integrating the game into another application
    """
    print("\n=== Game Integration Example ===\n")

    # Create multiple players
    players = [Player("Bob"), Player("Carol"), Player("Dave")]

    # Simulate a tournament
    for player in players:
        game = HangmanGame(player)

        # Play 3 games per player (simplified simulation)
        for _ in range(3):
            game.start_new_game()
            # Simulate random completion
            import random

            player.add_win() if random.choice([True, False]) else player.add_loss()

    # Display leaderboard
    print("Tournament Results:")
    print(f"{'Player':<10} {'Score':<10} {'Wins':<8} {'Win Rate'}")
    print("-" * 45)

    for player in sorted(players, key=lambda p: p.score, reverse=True):
        stats = player.get_stats()
        print(
            f"{stats['name']:<10} {stats['score']:<10} {stats['games_won']:<8} {stats['win_rate']:.1f}%"
        )


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("HANGMAN GAME - USAGE EXAMPLES".center(60))
    print("=" * 60 + "\n")

    # Run examples
    example_programmatic_usage()
    example_custom_word_bank()
    example_game_integration()

    print("\n" + "=" * 60)
    print("For the full interactive game, run: python hangman.py")
    print("=" * 60 + "\n")
