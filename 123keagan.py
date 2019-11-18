#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50



#new code 
screen_width = 400
screen_height = 400
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"
"S","T","U","V","W","X","Y","Z"]





wn = trtl.Screen()
wn.addshape(apple_image) # Make the screen aware of the new file
wn.setup(width=1.0, height=1.0)

wn.pgpic("tree.gif")
apple = trtl_turtle()
apple.penup()
wn.tracer(false)


apple = trtl.Turtle()

#new code
def reset_apple(active_apple):
  length_of_list = len(letter_list)
if (length_of_list != 0)
  index = rand.randint(0, length_of_list)
  active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2, rand.randint(-(screen_height)/2,) (screen_height)/2))


# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(active_apple, letter)
  wn.update()


def drop_apple():
  wn.tracer(true)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(false)

#new
draw_apple(apple)
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("tree.gif")
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

drawer = trtl.Turtle()

# This function takes care of font and color.
def draw_an_A():
  drawer.color("blue")
  drawer.write("A", font=("Arial", 74, "bold")) 

# This call to the onkeypress function sets draw_an_A as the function
# that will be called when the "a" key is pressed.



draw_apple(apple)
wn.onkeypress(draw_an_A, "a")


wn.listen()
trtl.mainloop()