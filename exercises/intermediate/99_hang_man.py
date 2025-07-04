import random

with open("random_words.txt", "r") as file:
    word_list = [line.strip() for line in file]
word = random.choice(word_list)
letters = []
guessed_letters = []
lives = len(word) + 1

for _ in word:
    letters.append("_")

print("Can you guess the following word?")


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

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    letters[index] = guess

        elif guess in guessed_letters:
            print(f"You have already guessed {guess}.")

        else:
            lives -= 1
            guessed_letters.append(guess)

        if "_" not in letters:
            print("You have won")
            break
