def case_checker(password):
    return all([any(map(str.isupper, password)), any(map(str.islower, password))])


def digit_checker(password):
    return any(map(str.isdigit, password))


def symbols_checker(password, sym):
    return any(map(lambda x: x in sym, password))


def len_checker(password):
    return len(password) >= 14


def password_checker(password, sym):
    return ["Weak password:", "Strong password"][all([case_checker(password), digit_checker(password),
                                                     symbols_checker(password, sym), len_checker(password)])]


if __name__ == "__main__":
    inp = input('Enter the password: ')
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    print(password_checker(inp, symbols))

    if not case_checker(inp):
        print("- Password must contain both lowercase and uppercase characters")
    if not digit_checker(inp):
        print("- Password must contain digits")
    if not symbols_checker(inp, symbols):
        print(f"- Password must contain  at least one punctuation character ({symbols}")
    if not len_checker(inp):
        print("- Password must be at least 14 characters long")
 
