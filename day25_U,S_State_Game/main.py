import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'day25/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

score = 0

data = pandas.read_csv('day25/50_states.csv')

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f'State Correct {score}/50', prompt='What\'s another states\'s name?').title()
    # test = (data[data.state == 'Ohio']).x
    # print(test)
    for name in data.state.to_list():
        if answer_state == name:
            timmy = turtle.Turtle()
            timmy.hideturtle()
            timmy.penup()
            timmy.goto(int((data[data.state == name]).x),int((data[data.state == name]).y))
            timmy.write(name, align='center')
            score += 1

# missing_states = [state for state in all_stastes if state not in guessed]