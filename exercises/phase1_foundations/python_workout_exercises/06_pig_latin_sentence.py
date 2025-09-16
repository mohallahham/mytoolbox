from mytoolbox.utils.cli_utlis import prompt_input


def pl_sentence(sentence):
    output = []
    for word in sentence.split():
        if word[0] in "aeiou":
            output.append(f"{word}way")
        else:
            output.append(f"{word[1:]}{word[0]}ay")
    return " ".join(output)


while True:
    sentence = prompt_input(
        prompt="Type a sentence to translate to Pig-Latin (or 'q' to quit): "
    )
    print(pl_sentence(sentence))
