# Harsha Malipeddi
'''strategy is to pick paper every time except for the first and second round'''

strategy_name = 'paper every time except first and second round'

def move(my_history, their_history):
    if len(my_history) < 1:
        return 'r'
    elif len(my_history) < 2:
        return 's'
    else:
        return 'p'