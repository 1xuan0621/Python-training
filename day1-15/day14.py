# 2020/02/14 day12
import day14_data
import random
import os
# 隨機選一筆資料A
def creat_dataA():
    dataA = random.choice(day14_data.data)
    day14_data.data.remove(dataA)
    return(dataA)
# 隨機選一筆不重複資料B
def create_dataB():
    dataB = random.choice(day14_data.data)
    day14_data.data.remove(dataB)
    return dataB
dataA = creat_dataA()
dataB = create_dataB()
score = 0

# 計算分數

gameover = False 
# 判斷A大還B大
while not gameover :
    print(f'your current score: {score}')
    print(f'Compare A: {dataA["name"]}, a {dataA["description"]}, from {dataA["country"]}')
    print(f'Compare B: {dataB["name"]}, a {dataB["description"]}, from {dataB["country"]}')
    if input('Who has more follower? Type"A" or "B" ') == 'A':
        if dataA['follower_count'] > dataB['follower_count']:
            score += 1
            dataB = create_dataB()
            os.system('cls')
        else:
            print('Wrong answer')
            gameover = True
    else:
        if dataA['follower_count'] < dataB['follower_count']:
            score += 1
            dataA = dataB
            dataB = create_dataB()
            os.system('cls')
        else:
            print('Wrong answer')
            gameover = True
print(f'your final score :{score}')