import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=500)

# Määritetään kuva uudeksi muodoksi ja taustakuvaksi
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("./50_states.csv")

# Määritetään kirjoittaja
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# score
score = 0
game_on = True
states_len = len(states.state)
correct_guessed = []
while game_on:
    if score == 50:
        game_on = False
# Kysytään käyttäjältä osavaltio
    answer_state = screen.textinput(title=f"{score}/{states_len} States Correct.", prompt="What's another state's name?").title()
    goto = states[states["state"] == answer_state]
    if not goto.empty:
        x = int(goto.x)
        y = int(goto.y)
        # state_name = str(goto.state)
        score += 1
        correct_guessed.append(answer_state)
        writer.goto(x, y)
        writer.write(answer_state, font=("Arial", 10, "bold"))
    elif answer_state == "Exit":
        game_on = False
        # all_states = states.state.to_list()
        missing_states = [state for state in states.state.to_list() if state not in correct_guessed]
        # for state in all_states:
        #     if state not in correct_guessed:
        #         missing_states.append(state)

        exit_data = pandas.DataFrame(missing_states)
        exit_data.to_csv("./states_to_learn.csv")






# def get_mouse_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_coor)
#
# turtle.mainloop()

screen.exitonclick()