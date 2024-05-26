import random

def tortiose_prob():
    perc = random.uniform(0,1)
    if perc <= 0.4: # Fast move
        move = 3
    elif perc >0.4 and perc <= 0.5: # Slip
        move = -6
    else: # Slow Move
        move = 1
    return move

def hare_prob():
    perc = random.uniform(0,1)
    if perc <= 0.1: # Sleep
        move = 0
    elif perc >0.1 and perc <= 0.4: # Big hop
        move = 9
    elif perc >0.4 and perc <=0.5: # Big slip
        move = -12
    elif perc>0.5 and perc <=0.7: # Small hop
        move = 1
    else: # Small slip
        move = -2
    return move

def race_map(tort, hare):
    for line in range(1,96):
        if line == 95 and tort >= 95:
                    print('T', end='')
        if line == 95 and hare >= 95:
                    print('H', end='')
        elif line != 95:
            if line == tort and line == hare:
                print('Ouch!',end='')
            elif line == tort:
                    print('T',end='')
            elif line == hare:
                    print('H',end='')
            else:
                    print("-",end='')
    print()
    
wins_hare, wins_tort, ties = 0,0,0
for _ in range(50):
    tort, hare = 1,1
    print("Bang and they are off!")
    while tort < 95 and hare < 95:
        tort = tort + tortiose_prob()
        hare = hare + hare_prob()
        race_map(tort,hare)
        if tort < 1:
            tort =  1
        if hare < 1:
            hare = 1 
        if tort >= 95 and hare >= 95:
            print("Its a tie!")
            ties += 1
        elif tort >= 95:
            print('The Tortoise has won the race!')
            wins_tort += 1
        elif hare >= 95:
            print('The Hare has won the race!')
            wins_hare += 1
print(f'The hare has {wins_hare} wins and the tortiose has {wins_tort} wins. There was {ties} tie(s).')

