MINIMUM_LENGTH = 4


def main():
    """get the password and print the stars"""
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)


def get_password(minimum_length):
    """get the password from user"""
    password = input(f"Input your password (at least {minimum_length} letters): ")
    while len(password) < minimum_length:
        print("Password less than the minimum requirement, please try again.")
        password = input(f"Input your password (at least {minimum_length} letters): ")
    return password


def print_stars(password):
    """print the stars as many as te length of password"""
    print('*'*len(password))


main()