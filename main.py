import turtle
import turtle as turtle_module
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guess = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()

    data_states = pandas.read_csv("50_states.csv")

    state_list = data_states["state"].to_list()

    for state in state_list:
        state_check = state
        if answer_state == state_check:
            print(answer_state)
            guess += 1

            position = data_states[data_states.state == f"{answer_state}"]
            x = (position.x).to_string()
            y = (position.y).to_string()

            x_pos = int((x[4:9]))
            y_pos = int((y[4:9]))
            print((x_pos, y_pos))

            guess_text = turtle_module.Turtle()
            guess_text.hideturtle()
            guess_text.penup()
            guess_text.goto(x_pos, y_pos)
            guess_text.write(f"{answer_state}", font=('Arial', 8, 'normal'))

            score = turtle_module.Turtle()
            score.hideturtle()
            score.penup()
            score.goto(0, 260)
            score.write(f"{guess}/50", font=('Arial', 15, 'normal'))

screen.exitonclick()
