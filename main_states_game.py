# Importing
import turtle
import pandas

# Setting screen up
screen = turtle.Screen() # We are creating the object
screen.title("U.S States Game")
screen.addshape('blank_states_img.gif') # We are adding this shape
turtle.shape('blank_states_img.gif') # We will now be using this new added shape


guess_total = []
# missed_states = []

# Reads from your Stats CSV file, which states all 50 states.
data_reading = pandas.read_csv('50_states.csv')
print(data_reading)
# Add each of the lines into a list format.
states_as_lst = data_reading.state.to_list()

# For allowing us to update the screen later.
screen.tracer(0)

# Main loop
# Runs as long as you haven't gotten all states correctly, or you quit.
while len(guess_total) != len(states_as_lst):
    # Updates the screen each time we loop through.
    screen.update()
    # The user can input the state name
    answer_state = screen.textinput(title=f"{len(guess_total)}/{len(states_as_lst)} States Correct",
                                    prompt= "What's another state name").title()

    # Allow them to quit the game.
    if answer_state == 'Quit':
        break

    # This is so we do not have duplicates in the guess list.
    elif answer_state in guess_total:
        pass

    elif answer_state in states_as_lst:
        # Adding to the guess list if it is unique.
        guess_total.append(answer_state)

        # Getting the location using the state subheading.
        location = data_reading[data_reading.state == answer_state]
        # We are printing the state name onto the map at its respected state position.
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        # Note that the original values come out as strings
        tim.goto(int(location.x), int(location.y))
        tim.write(answer_state)   # or tim.write((data_reading.state.x.item()) could work

# Using string concatenation.
missed_states = [t_states for t_states in states_as_lst if t_states not in guess_total]

# Creating a new file with missing states for you to practice
data_learning = pandas.DataFrame(missed_states)
data_learning.to_csv('states_to_learn')

