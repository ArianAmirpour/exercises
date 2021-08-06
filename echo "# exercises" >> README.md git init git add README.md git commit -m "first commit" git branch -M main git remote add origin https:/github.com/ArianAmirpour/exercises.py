
from random import randint
game = {
    's': 'sang',
    'k': 'kaghaz', 
    'g': 'gheychi'
}
player_score = 0
computer_score = 0

while True:
    i = input('sang(s) , kaghaz(k) , gheychi(g) : ')
    if i not in ['s' , 'k' , 'g']:
        print('not a valid input!')
        continue
    print('Your choose ' + game[i])

    choices = ['s', 'k' , 'g']
    random_number = randint(0, 2)
    c = choices[random_number]
    
    print('Computer Choose ' + game[c])

    if i == c:
        print('Mosavi Shod !')
    elif i =='s':
        if c =='k':
            print('Computer Wins!')
            computer_score += 1
        else:
            print('You Win')
            player_score += 1
    

    elif i == 'k':
        if c == 'g':
            print('Computer Wins!')
            computer_score += 1
        else:
            print('You Wins !')
            player_score += 1

    
    elif i == 'g':
        if c == 's':
            print('Computer Wins!')
            computer_score += 1
        else:   
            print('You Wins !')
            player_score += 1
    
    print('..................')
    print('Your total score : ' + str(player_score))
    print('Computer total score : ' + str(computer_score))
    print('..................')

    t = input('Continue ? (y/n)')

    if t == 'y':
        continue
    elif t == 'n':
        break

