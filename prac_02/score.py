import random

def main():
    '''get a score and determine the result'''
    score = get_valid_score()
    print(determine_result(score))
    
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


main()
random_score = random.randint(0,100)
print('Random score: ',random_score)
print(determine_result(random_score))