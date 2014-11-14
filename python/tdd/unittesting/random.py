import re


def count(word):
    """
    Count number of characters in text
    :return: Length
    """

    return len(word)


def count_alpha(word):
    """
    Count number of alphabetic characters in text
    :return: Number of alphabetic characters
    """

    alpha = re.compile(r'[a-z]', re.IGNORECASE)
    return len(alpha.findall(word))


def count_numeric(word):
    """
    Count number of numeric characters in text
    :return: Number of numeric characters
    """

    alpha = re.compile(r'[0-9]')
    return len(alpha.findall(word))


def count_vowels(word):
    """
    Count number of vowels in text
    :return: Number of vowels
    """

    vowels = re.compile(r'[aeouy]', re.IGNORECASE)
    return len(vowels.findall(word))


def is_phonenumber(number):
    """
    Check if text is a valid US phone number
    :return: True or False
    """

    phonenum = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
    if phonenum.match(number) is None:
        return False
    else:
        return True
