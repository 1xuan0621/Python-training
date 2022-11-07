# 2022/02/11

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = random.sample(cards,2)
computer_cards = random.sample(cards,2)
def computer_check():
    computer_score = 0
    # print(computer_cards)
    for i in computer_cards:
        computer_score += i
        # print(computer_score)
    if computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_check()
        # print(computer_score)
        # print(computer_cards)
    return calculate_score(computer_cards)

print(user_cards)
print(computer_cards[0])
def calculate_score(list_of_cards):
    score = 0
    for i in list_of_cards:
        score = score + i
    if score == 21:
        return 0
    elif score > 21:
        for i in list_of_cards:
            if i == 11:
                list_of_cards.remove(11)
                list_of_cards.append(1)
                calculate_score(list_of_cards)
    return score
def player_score():  
    pcore = calculate_score(user_cards)
    if pcore == 0:
        return 0
    elif pcore > 21:
        return 1
    else:
        if input('do you want to draw another card? "y" "n"') == 'y':
            user_cards.append(random.choice(cards))
            calculate_score
            print(user_cards)
            player_score()
    print(pcore)
    return calculate_score(user_cards)
player_score()
computer_check()
def compare(player,computer):
    if computer == 0:
        print('player lose')
    elif player == 0:
        print('win')
    elif player == computer:
        print('draw')
    elif player > computer:
        print('win')
    else:
        print('lose') 
    # if input('want to restart?"y" "n" ') == 'y':
        # start()
print(player_score)
if not player_score == 1:
    print(computer_cards)
    compare(calculate_score(user_cards),calculate_score(computer_cards))