import Task_1
from string import punctuation

test_word = "The quick br0wn fox jumps 0ver the lazy d0g."


def test_case_checker():
    assert Task_1.case_checker(test_word), "Password not contains both lowercase and uppercase characters"


def test_digit_checker():
    return Task_1.digit_checker(test_word), "Password not contains at least one digit"


def test_symbols_checker():
    assert Task_1.symbols_checker(test_word, punctuation), "Password not contains at least one punctuation character"


def test_len_checker():
    assert Task_1.len_checker(test_word), "Password contains less than 14 characters"


def test_password_checker():
    assert Task_1.password_checker(test_word, punctuation) == "Strong password", "Not all criteria are met"
