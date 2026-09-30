# This program was made by Harris Domangue for CMSC-201 on Oct. 17th 2024
# This program will simulate a fighting game

import random

def hit():
    global damage
    damage = random.randint(1,100)
    
    if damage % 10:
        damage *= 2
        return damage
    else:
        return damage

def play():
    player1 = 1000
    player2 = 1000
    num_hit = 0

    while player1 > 0 and player2 > 0:
        player1 -= hit()
        player2 -= hit()
        num_hit += 1
        print(f"Player 1 Health: {player1}")
        print(f"Player 2 Health: {player2}")
        print(f"total hits {num_hit}")
        print()
        if player2 > player1 :
            print("player 2 won")
            print(f"total hits {num_hit}")
        elif player1 > player2:
            print("player 1 won")
            print(f"total hits {num_hit}")
        else:
            print()

def main():
    play()
    
if __name__ == '__main__':
    main()
