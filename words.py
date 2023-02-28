
def print_upper_words(words):
    """Given a list of words, print out each word on a separate line, but in all uppercase."""

    for word in words:
        if 'e' == word.lower()[0]:
            print(word.upper())

print_upper_words(["ello", "hey", "goodbye", "Easy", "yes"])

def print_upper_words2(words, must_start_with):
    """For a list of words, print out each word on a separate line if
     the frist letter is contained in a given set, but in all uppercase."""

    for word in words:
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words2(["ello", "hey", "goodbye", "Easy", "yes"],
                   must_start_with={"h", "y"})