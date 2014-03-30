# if upper, turn to lower; if lower turn to upper


def flip_case(word):
    letters = list(word)
    new_word = ""
    for letter in letters:
        if letter.isupper():
            letter = letter.lower()
        elif letter.islower():
            letter = letter.upper()
        new_word += letter
    return new_word



### --- run code --- ###`


print flip_case("AaaaEEEE") == "aAAAeeee"
print flip_case("jhY7tRf") == "JHy7TrF"
