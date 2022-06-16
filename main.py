import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=750, height=525)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = list()
states_data = pandas.read_csv("50_states.csv")
write_state = turtle.Turtle()
write_state.hideturtle()
write_state.penup()
all_states = states_data.state.tolist()
missed_states = list()
screen.tracer(0)

while len(guessed_states) != 50:
    screen.update()
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Enter the name of a "
                                                                                             "state: ").title().strip()
    if answer_state == "Exit":
        missed_states = [state_name for state_name in all_states if state_name not in guessed_states]
        break
    state = states_data[states_data["state"] == answer_state]
    if not state.empty and answer_state not in guessed_states:
        write_state.goto(int(state.x), int(state.y))
        write_state.write(arg=answer_state)
        guessed_states.append(answer_state)

for state_name in missed_states:
    write_state.color("red")
    state = states_data[states_data["state"] == state_name]
    write_state.goto(int(state.x), int(state.y))
    write_state.write(arg=state_name)

screen.update()
screen.exitonclick()
