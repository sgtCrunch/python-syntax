
def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase."""

    for word in words:
        if 'e' == word.lower()[0]:
            print(word)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])