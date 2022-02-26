import turtle
answer = turtle.Turtle()
screen=turtle.Screen()
screen.reset()
screen.setworldcoordinates(-1000,-1000,1000,1000)
x=-1000
turtle.bgcolor('white')

answer.penup()
answer.goto(-1000,0)
answer.pendown()


def letterA():
    answer.right(300)
    answer.forward(100)
    answer.right(120)
    answer.forward(100)
    answer.right(180)
    answer.forward(50)
    answer.right(300)
    answer.forward(50)
    answer.penup()
    answer.goto(x,0)
    answer.right(180)
    answer.pendown()
def letterB():
    answer.left(90)
    answer.forward(100)
    answer.left(90)
    answer.circle(25, -180)
    answer.left(180)
    answer.circle(25, -180)
    
    answer.penup()
    answer.goto(x,0)
    
    answer.pendown()
def letterC():
    answer.circle(50, -180)
    answer.left(90)
    answer.penup()
    answer.goto(x,0)
    answer.left(90)
    answer.pendown()
def letterD():
    answer.left(90)
    answer.forward(100)
    answer.left(90)
    answer.circle(50, -180)
    answer.penup()
    answer.goto(x,0)
    
    answer.pendown()

def letterE():
    answer.forward(50)
    answer.right(180)
    answer.forward(50)
    answer.right(90)
    answer.forward(50)
    answer.right(90)
    answer.forward(50)
    answer.right(180)
    answer.forward(50)
    answer.right(90)
    answer.forward(50)
    answer.right(90)
    answer.forward(50)
    answer.penup()
    answer.goto(x,0)
    
    answer.pendown()
def letterF():
    answer.right(270)
    answer.forward(50)
    answer.right(90)
    answer.forward(50)
    answer.right(180)
    answer.forward(50)
    answer.right(90)
    answer.forward(50)
    answer.right(90)
    answer.forward(50)
    answer.penup()
    answer.goto(x,0)
    
    answer.pendown()
def letterG():
    answer.circle(50, -180)
    answer.circle(50, 180)
    answer.left(90)
    answer.forward(50)
    answer.left(90)
    answer.forward(30)
    answer.penup()
    answer.goto(x,0)
    answer.right(180)
    answer.pendown()

def letterH():
    answer.right(270)
    answer.forward(100)
    answer.right(180)
    answer.forward(50)
    answer.right(270)
    answer.forward(50)
    answer.right(270)
    answer.forward(50)
    answer.backward(100)
    
    
    answer.penup()
    answer.goto(x,0)
    
    
    answer.right(90)
    answer.pendown()
    

def letterI():
    answer.forward(50)
    answer.right(180)
    answer.forward(25)
    answer.right(90)
    answer.forward(100)
    answer.right(90)
    answer.forward(25)
    answer.right(180)
    answer.forward(50)
    answer.penup()
    answer.goto(x,0)
    answer.right(180)
    answer.pendown()

def letterJ():
    answer.left(90)
    answer.forward(100)
    answer.left(90)
    answer.forward(10)
    answer.backward(20)
    answer.forward(10)
    answer.left(90)
    answer.forward(100)
    answer.circle(-25,180)
    answer.right(180)
    answer.penup()
    answer.goto(x-40,0)
    answer.right(270)
    answer.pendown()
    
    

    

def letterK():
    answer.left(90)
    answer.forward(100)
    answer.backward(50)
    answer.right(45)
    answer.forward(50)
    answer.backward(50)
    answer.left(270)
    answer.forward(50)
    answer.penup()
    answer.goto(x,0)
    answer.right(315)
    answer.pendown()
    
    
def letterL():
    answer.forward(100)
    answer.backward(100)
    answer.left(90)
    answer.forward(100)
    answer.penup()
    answer.goto(x,0)
    answer.penup()
    answer.goto(x,0)
    answer.right(90)
    answer.pendown()
    
    

    answer.pendown()
    
def letterM():
    answer.left(90)
    answer.forward(100)
    answer.right(160)
    answer.forward(100)
    answer.left(150)
    answer.forward(100)
    answer.right(160)
    answer.forward(100)
    answer.penup()
    answer.goto(x,0)
    answer.penup()
    answer.goto(x,0)
    answer.left(80)
    answer.pendown()
    
    

    answer.pendown()
    
def letterN():
    answer.left(90)
    answer.forward(100)
    answer.right(150)
    answer.forward(110)
    answer.left(150)
    answer.forward(100)
    answer.penup()
    answer.goto(x,0)
    answer.right(90)
    answer.pendown()
    
def letterO():
    answer.circle(50, 360)
    answer.penup()
    answer.goto(x,0)
    
    answer.pendown()
    
def letterP():
    answer.left(90)
    answer.forward(100)
    answer.backward(50)
    answer.right(90)
    answer.circle(25, 180)
    answer.penup()
    answer.goto(x,0)
    answer.right(180)
    answer.pendown()
    
def letterQ():
    answer.circle(50, 360)
    answer.circle(50, 30)
    answer.left(120)
    answer.forward(25)
    answer.backward(50)
    answer.penup()
    answer.goto(x,0)
    answer.right(150)
    answer.pendown()
    

    
def letterR():
    answer.left(90)
    answer.forward(100)
    answer.backward(50)
    answer.right(90)
    answer.circle(25,180)
    answer.left(90)
    answer.forward(50)
    answer.left(37.5)
    answer.forward(60)
    answer.penup()
    answer.goto(x-40,0)
    answer.left(55)
    answer.pendown()
    
def letterS():
    answer.penup()
    answer.left(90)
    answer.forward(50)
    answer.right(90)
    answer.pendown()
    answer.circle(30, -180)
    answer.circle(30, 180)
    answer.circle(-30, 200)
    answer.penup()
    answer.goto(x,0)
    answer.right(160)
    answer.pendown()

def letterT():
    answer.color('white')
    answer.left(90)
    answer.forward(100)
    answer.left(90)
    answer.forward(50)
    answer.backward(100)
    answer.penup()
    answer.goto(x,0)
    answer.right(180)
    answer.pendown()
    
def letterU():
    answer.right(90)
    answer.circle(50, 180)
    answer.forward(50)
    answer.backward(50)
    answer.circle(50, -180)
    answer.backward(50)
    answer.penup()
    answer.goto(x,0)
    answer.right(275)
    answer.pendown()

def letterV():
    answer.left(60)
    answer.forward(100)
    answer.backward(100)
    answer.left(60)
    answer.forward(100)
    answer.penup()
    answer.goto(x,0)
    answer.right(125)
    
    answer.pendown()
    
def letterW():
    answer.left(90)
    answer.forward(100)
    answer.backward(100)
    answer.right(30)
    answer.forward(100)
    answer.right(120)
    answer.forward(100)
    answer.left(150)
    answer.forward(100)
    answer.penup()
    answer.goto(x,0)
    answer.right(90)
    answer.pendown()
    
def letterX():
    answer.left(45)
    answer.forward(50)
    answer.backward(100)
    answer.forward(50)
    answer.left(90)
    answer.forward(50)
    answer.backward(100)
    answer.penup()
    answer.goto(x,0)
    answer.right(135)
    answer.pendown()
    
def letterY():
    answer.left(60)
    answer.forward(50)
    answer.backward(50)
    answer.left(60)
    answer.forward(50)
    answer.backward(50)
    answer.left(150)
    answer.forward(60)
    answer.penup()
    answer.goto(x,0)
    answer.left(90)
    answer.pendown()
    
def letterZ():
    answer.forward(100)
    answer.backward(100)
    answer.left(45)
    answer.forward(100)
    answer.right(225)
    answer.forward(100)
    answer.penup()
    
    answer.goto(x,0)
    answer.right(180)
    answer.pendown()
    


    

    
    
    
    


answer2 = int(input('Enter the 1 to Countnue And 0 to quit'));


while answer2==1:
    
    answer2 = int(input('Enter the 1 to Countnue And 0 to quit'));
    answer1 = input(' Type the Letter  in Uppercase to Draw  ');
    color=input('In which color you want to print the ')
    x=x+110
    if color == "red":
        answer.color("red")
    elif color == "blue":
        answer.color("blue")
    elif color == "green":
        answer.color("green")
    elif color == "yellow":
        answer.color("yellow")
    
    if answer1 ==('A'):
            letterA()
    elif answer1 == ('B'):
            letterB()

    elif answer1 == ('C'):
            letterC()
    elif answer1 == ('D'):
            letterD()
    elif answer1 == ('E'):
            letterE()

    elif answer1 == ('F'):
            letterF()
    
    elif answer1 == ('G'):
            letterG()
    elif answer1 == ('H'):
            letterH()

    elif answer1 == ('I'):
            letterI()


    elif answer1 == ('J'):
            letterJ()
    elif answer1 == ('K'):
            letterK()

    elif answer1 == ('L'):
            letterL()

    elif answer1 == ('M'):
            letterM()
    elif answer1 == ('N'):
            letterN()

    elif answer1 == ('O'):
            letterO()

   
    elif answer1 == ('P'):
            letterP()
    
    elif answer1 == ('Q'):
            letterQ()
    elif answer1 == ('R'):
            letterR()

    elif answer1 == ('S'):
            letterS()

    elif answer1 == ('T'):
            letterT()
    elif answer1 == ('U'):
            letterU()

    elif answer1 == ('V'):
            letterV()

   
    elif answer1 == ('W'):
            letterW()
    elif answer1 == ('X'):
            letterX()
    elif answer1 == ('Y'):
            letterY()
    elif answer1 == ('Z'):
            letterZ()
    else:
         print ('Input is wrong')
