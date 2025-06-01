"""
Word counting utility functions:
- remove_punctuations
- count_words
- sort_words_by_frequency
"""

import string

text = "The quick brown fox jumps over the lazy dog. A fox is quick and sly; the dog, however, is lazy and slow."


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


def sort_words_by_frequency(word_counts):
    sorted_word_counts = sorted(
        word_counts.items(), key=lambda item: item[1], reverse=True
    )
    return sorted_word_counts


cleaned = remove_punctuations(text)
words = count_words(cleaned)
sorted_words = sort_words_by_frequency(words)

print(sorted_words)
