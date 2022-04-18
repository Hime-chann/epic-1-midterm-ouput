#CCS221-Midterm
#Princes Rose Manuel BSCS-1B

import turtle
turtle.Screen().bgcolor("pink") 
turtle.speed(0)




# 1 SPIRAL:

turtle.tracer(10,1)

for i in range(340):

 colors = [ "pink" , "red", "white", "violet", "black", "orange", "blue", "green", "yellow"]

 turtle.pendown ()
 turtle.pensize (5)
 turtle.circle(i,20)
 turtle.color(colors[i%9])

turtle.update()





# 2 Drawing

def drawTurtle(n):

  for i in range(n):
     
      turtle.penup ()
      turtle.pendown()
      turtle.goto (0,0)
      turtle.pencolor ("#800000") #red
      turtle.forward (60)
      turtle.left(90)
      turtle.pencolor("#4B0082") #purple
      turtle.forward (100)
      turtle.right (50)
      turtle.pencolor("#191970") #blue
      turtle.forward (70)
      turtle.pensize(10)
      turtle.left (60)
      turtle.pensize(6)
      turtle.pencolor("#C71585") #pink
      turtle.forward (65)
      turtle.left (45)
      turtle.pencolor("black") #black
      turtle.forward (120)
      turtle.penup ()

drawTurtle (100)


# 3 WRITINGS

turtle.penup ()
turtle.goto(400, -250)
turtle.pendown ()
turtle.write('This circle is the wholeness of spirit. \n \n The spiral start with \n red: STRENGTH, \n and end with \n yellow: HAPPINESS. \n', font=("Robert Leuschke", 10))
turtle.penup ()
turtle.goto(350, 320)
turtle.pendown ()
turtle.write('MANDALA - MIDTERM', font=("Arial", 20))
turtle.up ()
turtle.penup ()
turtle.goto(300, -310)
turtle.pendown ()
turtle.write('Princes Rose Manuel', font=("Bradley Hand ITC", 30, "bold"))
turtle.penup ()
turtle.goto (300, -330)
turtle.write('    BSCS 1B', font=("Monotype cursiva", 10, "bold"))



# 4 EXIT
window = turtle.Screen()
window.exitonclick()