# #* Goal
# word_counts("hello world hello")
# Output: {'hello': 2, 'world': 1}

# todo
# !✨ Bonus Challenges
# Bonus 1: Make it case-insensitive ("Hello" and "hello" count the same).
# Bonus 2: Remove basic punctuation (,, ., !, etc.).
# Bonus 3: Return the dictionary sorted by the most frequent words.
# Bonus 4: Add an optional stop word to remove or keep

# "The quick brown fox jumps over the lazy dog. A fox is quick and sly; the dog, however, is lazy and slow."
# text = "This is a text Text and text"
import string

text = "hello, world hello"


def remove_punctuations(text):
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    return text


def count_words(text):
    word_counts = {}
    word_normalized = text.lower()
    words = word_normalized.split()
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


cleaned_text = remove_punctuations(text)

print(count_words(cleaned_text))
