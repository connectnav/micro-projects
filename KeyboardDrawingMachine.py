from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()
ans= screen.textinput('KEYBOARD DRAWING MACHINE','Please Read the Manual\n\n'
                                            'w:  move the pen Forward along the direction of arrow\n '
                                            's:  move the pen Backward against the direction of arrow\n'
                                            'd:  turn Right to the direction of arrow\n'
                                            'a:  turn Left to the direction of arrow\n'
                                            'z:  No ink\n'
                                            'x:  Black ink\n'
                                            'c:  Clear the drawing\n\n'
                 'Press y to continue \n\n ')
                                        
if ans=='y' or ans=='Y' :

    screen.title('Keyboard Drawing Machine')

    def move_forward():
        timmy.forward(20)

    def move_backward():
        timmy.backward(20)

    def turn_right():
        timmy.right(10)

    def turn_left():
        timmy.left(10)

    def clear():
        timmy.clear()
        timmy.penup()
        timmy.home()
        timmy.pendown()

    def penup():
        timmy.penup()

    def pendown():
        timmy.pendown()

    screen.listen()

    screen.onkey(move_forward,"w")
    screen.onkey(move_backward,'s')
    screen.onkey(turn_left,'a')
    screen.onkey(turn_right,'d')
    screen.onkey(clear,'c')
    screen.onkey(penup,'z')
    screen.onkey(pendown,'x')

    screen.exitonclick()

else:
    print('Please read the Manual! \n')

