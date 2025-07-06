from mytoolbox.utils.cli_utlis import prompt_input


def pig_latin(word):
    if word[0] in "aeiou":
        return f"{word}way"
    return f"{word[1:]}{word[0]}ay"


while True:
    word = prompt_input("Type a word to translate to Pig-Latin (or 'q' to quit): ")
    print(pig_latin(word))
