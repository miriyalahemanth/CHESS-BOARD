import turtle  
scr = turtle.Screen()  
a = turtle.Turtle()  
def draw():  
     for i in range(4):  
        a.forward(35)  
        a.left(90)  
  
     a.forward(35)  
if __name__ == "__main__":  
    scr.setup(500, 600)  
    a.speed(100)  
    for i in range(8):  
        a.up()  
        a.setpos(-150, 35 * i)
        a.down()  
        for j in range(8):  
            if (i+j) % 2 == 0:  
                color = 'black'  
  
            else:  
                color = 'white'  
  
            a.fillcolor(color)  
            a.begin_fill()  
            draw()  
            a.end_fill()  
  
    a.hideturtle()  
    turtle.done()
