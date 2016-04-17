"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    char_dict = {}
    most_frequent_characters = []
    input_string = input_string.replace(" ","")

    for character in input_string:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1

    highest_frequency = max(char_dict.values())

    for character, frequency in char_dict.items():
        if frequency == highest_frequency:
            most_frequent_characters.append(character)

    return sorted(most_frequent_characters)

    # About 15-20 minutes



def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    tuples_dict = {}

    for word in words:
        if len(word) not in tuples_dict:
            tuples_dict[len(word)] = [word]
        else:
            for length, word_list in tuples_dict.items():
                if length == len(word):
                    word_list.append(word)
                # word_list = sorted(word_list) # although this saves the sorted word_list, it doesn't save it back within the dictionary
                tuples_dict[length] = sorted(word_list) #saves the sorted word_list back into the dictionary!

    return tuples_dict.items()

    # About 15-20 minutes because I based it on the similar problem in skills.py


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
