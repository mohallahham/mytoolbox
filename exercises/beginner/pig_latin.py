# if a word starts with vowel just add yay to the end.
# if a word starts with constant, move first litter and add ay to the end.

# user input a word

vowels = ["a", "e", "i", "o", "u"]

while True:
    word = input(
        "Please type a word to translate to pig latin (or type 'q' to exit): \n"
    ).lower()

    if word == "q":
        print("Goodbye")
        break

    char_list = list(word)

    if char_list[0] in vowels:
        print(f"{word}yay")
    else:
        f_letter = char_list.pop(0)
        char_list.append(f_letter)
        print(f"{''.join(char_list)}ay")  # need to understand this better!!
