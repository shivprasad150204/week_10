# testing.py
import doctest


def repeat_string(string, times):
    """Repeat a given string a specified number of times.

    >>> repeat_string('abc', 3)
    'abcabcabc'
    >>> repeat_string('hello', 2)
    'hellohello'
    """
    return string * times


def is_long_word(word):
    """Return True if the word has more than 7 letters.

    >>> is_long_word('abcdefgh')
    True
    >>> is_long_word('abcdefg')
    False
    """
    return len(word) > 7


def format_as_sentence(phrase):
    """Format a phrase as a sentence - start with a capital and end with a full stop.

    >>> format_as_sentence('hello')
    'Hello.'
    >>> format_as_sentence('Hello world')
    'Hello world.'
    """
    if not phrase:
        return ''
    return phrase[0].upper() + phrase[1:] + '.'


if __name__ == '__main__':
    doctest.testmod()
