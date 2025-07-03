# print(*letters) unpacking option

word = "hello"
letters = []
lives = len(word) + 1

for _ in word:
    letters.append("_")

print("Can you guess the following word?")


while True:
    if lives == 0:
        print("sorry you have lost")
        break
    else:
        print(" ".join(letters))
        print(f"you have {lives} chances")
        guess = input("Guess a letter ")

        if guess == "quit":
            break

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    letters[index] = guess

        else:
            lives -= 1

        if "_" not in letters:
            print("You have won")
            break
