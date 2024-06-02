def main():
    '''menu loop for this program'''
    score = get_valid_score()
    menu()
    choice = input('').upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print(determine_result(score))
        elif choice == 'S':
            show_stars(score)
        else:
            print('Invalid choice')
        menu()
        choice = input('').upper()
    print('farewell')


def get_valid_score():
    '''get a valid score from user (must be 0-100 inclusive)'''
    score = int(input('Enter score: '))
    while score < 0 or score > 100:
        print('Invalid score')
        score = int(input('score: '))
    return score


def determine_result(score):
    '''determine the result'''
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    '''print as many stars as the score'''
    print('*'*score)


def menu():
    '''display the menu for user'''
    print('''(G)et a valid score
(P)rint result
(S)how stars
(Q)uit''')


main()