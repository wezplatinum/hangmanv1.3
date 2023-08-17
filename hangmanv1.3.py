import random
import string

# Sample words (replace with your actual words)
from words import words

# Dictionary to store high scores
high_scores = {"easy": 0, "medium": 0, "hard": 0}

def categorize_words(words):
    easy_words = [word for word in words if len(word) < 4]
    medium_words = [word for word in words if 4 <= len(word) < 8]
    hard_words = [word for word in words if len(word) >= 8]
    return easy_words, medium_words, hard_words

def get_word_by_difficulty(difficulty, easy_words, medium_words, hard_words):
    if difficulty == "easy":
        return random.choice(easy_words)
    elif difficulty == "medium":
        return random.choice(medium_words)
    elif difficulty == "hard":
        return random.choice(hard_words)

def display_high_scores():
    print("\nHigh Scores:")
    for difficulty, score in high_scores.items():
        print(f"{difficulty.capitalize()}: {score}")

def hangman():
    alphabet = set(string.ascii_uppercase)

    print("Welcome to Hangman!")

    easy_words, medium_words, hard_words = categorize_words(words)

    while True:
        display_high_scores()

        difficulty = input("\nChoose your difficulty (easy, medium, hard), or 'quit' to exit: ").lower()
        if difficulty == "quit":
            print("Exiting the game.")
            break

        while difficulty not in ["easy", "medium", "hard"]:
            print("Invalid difficulty level. Please choose between easy, medium, or hard.")
            difficulty = input("Choose your difficulty (easy, medium, hard), or 'quit' to exit: ").lower()

        word = get_word_by_difficulty(difficulty, easy_words, medium_words, hard_words).upper()
        word_letters = set(word)

        lives = 6
        used_letters = set()

        while lives > 0:
            print('\nCurrent lives left:', lives)
            print('You have used these letters:', ' '.join(used_letters))

            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('Current word:', ' '.join(word_list))

            user_letter = input('\nGuess a letter: ').upper()

            if len(user_letter) != 1 or user_letter not in alphabet:
                print('Invalid character. Please guess a single letter.')
                continue

            if user_letter in used_letters:
                print('You have already used that letter. Please try again.')
                continue

            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                life_text = "life" if lives == 1 else "lives"
                print(f"Wrong letter, you lost 1 life. You now have {lives} remaining out of 6 {life_text}.")

            if len(word_letters) == 0:
                print('\nYou have guessed the word', word, '!! Lives remaining:', lives)
                high_scores[difficulty] += 1
                print("Congratulations! You guessed the word correctly!")
                break

        if lives == 0:
            print('\nYou hanged the man. No more lives left. The word was:', word)

        continue_game = input("\nDo you want to play again? (yes/no): ").lower()
        if continue_game != "yes":
            print("Exiting the game.")
            break

hangman()
