# For this is project we are using images in turtle graphics
import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Of America")
image = "States_Of_America_Quiz\\blank_states_img.gif"
# def get_mouse_click_coor(x,y):
#    print (x,y)
# screen.onscreenclick(get_mouse_click_coor)
# now we are fine to use image as shape value for this screen
screen.addshape(image)
turtle.shape(image)
# main logic begins
Title="Guess the state"
is_loop_on=True
already_guessed=[]
data = pandas.read_csv("States_Of_America_Quiz\\50_states.csv")
list_of_states =data.state.to_list()
x_cor_of_states =data.x.to_list()
y_cor_of_states =data.y.to_list()
correct_guess=0
while is_loop_on:
    guess = screen.textinput(title= Title, prompt="Which State is coming in your mind, NOW ?")
    index=0
    for state in list_of_states:
        if guess.lower() == state.lower():
            # list_of_states.remove(state)
            # x_cor_of_states.remove(x_cor_of_states[index])
            # y_cor_of_states.remove(y_cor_of_states[index])
            x_cor_to_move =x_cor_of_states[index]
            y_cor_to_move =y_cor_of_states[index]
            state_turtle = turtle.Turtle()
            state_turtle.penup()
            state_turtle.hideturtle()
            state_turtle.goto(x_cor_to_move,y_cor_to_move)
            state_turtle.write(state,False,font=("Aerial",9,"normal" ))
            c=0
            for item in already_guessed:
                if item.lower()==state.lower():
                    c+=1
            if c==0:
                already_guessed.append(state)
                correct_guess+=1
            Title=f"{correct_guess}/50"
        if correct_guess==50:
            is_loop_on=False
        index+=1
            

screen.mainloop() 
# alternative way to keep screen on, better to use this here to avoid screen exit on lcik
# screen.exitonclick()
