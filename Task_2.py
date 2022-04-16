import string
import random
import Task_1


def password_generator(len_password):
    lis = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits
    return ''.join(random.sample(lis, len_password))


def password_checker(password):
    return not all([Task_1.case_checker(password), Task_1.digit_checker(password),
                    Task_1.symbols_checker(password, string.punctuation), Task_1.len_checker(password)])


if password_checker(password_generator(14)):
    print(password_generator(14))
else:
    password_generator(14)
