import turtle
import pandas as pd

# Setup screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read in our data and create pandas dataframe
states_file = pd.read_csv("50_states.csv")
states = pd.DataFrame(states_file)

# Number of correct states
correct_answers = []

# Initial playing state
is_playing = True


# Write states to screen at x,y location
def write_states(user_guess, data):
    # Create object to hold state's name
    state_letters = turtle.Turtle()
    state_letters.hideturtle()
    state_letters.penup()

    # Find the x and y values for the state
    x_pos = int(data[data['state'] == user_guess]['x'])
    y_pos = int(data[data['state'] == user_guess]['y'])

    # Write the state to screen
    state_letters.goto(x_pos-20, y_pos)
    state_letters.write(user_guess)


# MAIN LOOP
while is_playing:

    # Get user input, display current correct answers in window title bar
    answer = screen.textinput(title=f"{len(correct_answers)}/50 Correct", prompt="What's a state name?")

    # Convert user's guess to title case
    answer = answer.title()

    # If user types 'exit', escape loop and write all the states they missed to csv file
    if answer == 'Exit':
        is_playing = False
        # Find all the states that user didn't guess correctly, write them to csv
        for answer in correct_answers:
            states[states['state'] != answer]['state'].to_csv("correct_answers.csv")
        break

    # If answer exists in dataframe, write to screen
    if answer in states['state'].unique():
        correct_answers.append(answer)
        write_states(user_guess=answer, data=states)


turtle.mainloop()
