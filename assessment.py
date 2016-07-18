"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    word_count = {}
    given_string = phrase.split()


    for word in given_string:

        if word not in word_count:
            # if word is not in dict. then add it to dict and set it to 1.
            word_count[word] = 1
        else:
            # if it is take the value of the dict. at the word and add one to it.
            word_count[word] = word_count[word] + 1
    return (word_count)


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """
    melons = {"Watermelon": 2.95, "Cantaloupe": 2.50, "Musk": 3.25, "Christmas": 14.25}
    # using conditional; the funct.takes a string and the string is the argument is called melon_name
    # checks to see if the string melon name is in the keys of the dict. melons.
    if melon_name in melons:
        # if the melon name in the melons dict. exists retrun the value.
        return melons[melon_name]
    else:
        return "No price found"



def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    # creating a dict first
    # iterate once to get the len of every word
    # sort every list alph. (might be another iteration??)
    # create tuples and sort tuples by len?

    return []


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
# def translate_to_pirate_talk(phrase):
    # Translate phrase to pirate talk. gonna use dict to set english words as key and pirate
    # words as value.2qqq212

    english_to_pirate = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie", "man": "matey", "professor": "foul blaggart", 
                         "restaurant": "galley", "your": "yer", "excuse": "arr", "students": "swabbies", "are": "be",
                         "restroom": "head", "my": "me", "is": "be"}

    # english = "sire hotel student man professor restaurant your excuse students are restroom are restroom my is"
    #     english.split()
    #     pirate = "matey fleabag swabbie matey foul blaggart galley yer arr swabbies be head me be"
    #     pirate.split()

    # created an empty list to add the translated words
    translated_phrase = []
    # used iteration to get every word in phrase which is the argument which is string. when a string
    # is split it returns a list i think?
    for word in phrase.split():
        # used conditional to check if word exists in dict.
        if word in english_to_pirate:
        #if word exists in english_to_pirate dict then add to the translated phrase list. i just
        # learned reading this code backwards makes sense!
            translated_phrase.append(english_to_pirate[word])
        else:
            # if it doesn't exist in the dict. then append the word to the list, translated_phrase.
            translated_phrase.append(word)
# example from online:
# s = "-";
# seq = ("a", "b", "c"); # This is sequence of strings.
# print s.join( seq )
    s = " "
    return s.join(translated_phrase) 


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    return []

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
