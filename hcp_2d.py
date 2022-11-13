import turtle



x = 40

g = 20

turtle.speed(100)

turtle.colormode(255)

def move(l, a):
                turtle.right(a)
                turtle.forward(l)

def hex():
        turtle.pendown()
        turtle.color( 0,0,0 )  
        for i in range(6):
                move(x,-60)       
                
                turtle.penup()
                turtle.right(90)
                turtle.forward(20)
                turtle.left(90)
                turtle.pendown()

                # circle
                turtle.circle(20)

                # move back
                turtle.penup()
                turtle.right(-90)
                turtle.forward(20)
                turtle.left(-90)
                turtle.pendown()
                

                
                move(x,120)
                turtle.penup()
                turtle.right(90)
                turtle.forward(20)
                turtle.left(90)
                turtle.pendown()

                # circle
                turtle.circle(20)

                # move back
                turtle.penup()
                turtle.right(-90)
                turtle.forward(20)
                turtle.left(-90)
                turtle.pendown()



turtle.penup()

for a in range (g):
        if a == 0:
                hex()
                move(x,-60)
                move(x,-60)
                move(x,-60)
                move(0,180)
        for i in range (6):
                move(0,60)
                for j in range (a+1):
                        hex()
                        move(x,-60)
                        move(x,60)
                move(-x,0)
        move(-x,60)
        move(x,-120)
        move(0,60)

turtle.exitoncli
