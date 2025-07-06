import random


def load_words():
    with open("random_words.txt", "r") as file:
        return [line.strip() for line in file]


def choose_word(word_list):
    return random.choice(word_list)


def initialize_word(word):
    return ["_" for _ in word]


def display_word(word):
    print("Can you guess the following word?")


def play_game(word):
    letters = initialize_word(word)
    guessed_letters = []
    lives = len(word) + 1
    while True:
        if lives == 0:
            print(f"sorry you have lost, and the word was {word}")
            break
        else:
            print(" ".join(letters))
            print(f"Guessed Letters : {' '.join(guessed_letters)}")
            print(f"you have {lives} chances")
            guess = input("Guess a letter ")

            if guess == "quit":
                break

            if guess in guessed_letters:
                print(f"You have already guessed {guess}.")
                continue
            guessed_letters.append(guess)

            if guess in word:
                for index, letter in enumerate(word):
                    if letter == guess:
                        letters[index] = guess

            else:
                lives -= 1

            if "_" not in letters:
                print("You have won")
                break


word_list = load_words()
word = choose_word(word_list)
display_word(word)
play_game(word)
