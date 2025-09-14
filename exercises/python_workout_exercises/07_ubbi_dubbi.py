from mytoolbox.utils.cli_utlis import prompt_input


def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in "aeiou":
            output.append(f"ub{letter}")
        else:
            output.append(letter)

    return "".join(output)


while True:
    word = prompt_input(
        prompt="Type a word to translate to Ubbi Dubbi (or 'q' to quit): "
    )
    print(ubbi_dubbi(word))
