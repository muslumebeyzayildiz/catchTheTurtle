import random
import time
import turtle

screen= turtle.Screen()
screen.bgcolor("light blue")
FONT=("Times New Roman",15,"bold") #büyük harfle yazılınca yazılım jargonunda sabit gibi bir daha bunu değiştirmeyeceğim anlamında
gridSize=10
score=0
gameOver=False
#turtle list
turtle_list=[]
#score turtle
scoreTurtle = turtle.Turtle()
#countDown Turtle
countDownTurtle= turtle.Turtle()
x_coordinates=[-20,-10,0,10,20]
y_coordinates=[20,10,0,-10]

def setupScoreTurtle(): #score u tutmak için turtle
    scoreTurtle.hideturtle()
    scoreTurtle.color("dark blue")
    scoreTurtle.penup()

    top_height=screen.window_height()/2
    y=top_height*0.9
    scoreTurtle.setpos(0,y)
    scoreTurtle.write(arg="score: 0",move=False, align="center", font=(FONT))

def make_turtle(x,y):
    t=turtle.Turtle()#20 tane faln trtle var bazen biri açılıyor bazen biri gibi bir yapı olacak

    def handleClick(x,y):
        print(x,y)
        global score
        score+= 1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"score: {score}", move=False, align="center", font=FONT)

    t.onclick(handleClick)
    t.penup()
    t.shape("turtle")
    #SHAPED=ŞEKİLLENDİRİLMİŞ
    t.shapesize(2,2)
    t.color("dark blue")
    t.goto(x*gridSize,y*gridSize)
    turtle_list.append(t) #her bir olşturulan turtle i bir dizide saklıyoruum

def setupTurtle():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hideTurtles():
    for t in turtle_list:
        t.hideturtle()

def showTurtlesRandomly():
    if not gameOver:
        hideTurtles()
        random.choice(turtle_list).showturtle() # turtle listen rastgele birini seç ve bunu göster
        screen.ontimer(showTurtlesRandomly,500)#fonksiyonn içinde kendisini çağırmak recursive

def countDown(time):
    global gameOver
    countDownTurtle.hideturtle()
    countDownTurtle.penup()
    top_height = screen.window_height()/2
    y=top_height*0.9
    countDownTurtle.setposition(0,y-30)
    countDownTurtle.clear()

    if time > 0:
        countDownTurtle.clear()
        countDownTurtle.write(arg=f"score: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countDown(time-1),1000)#saniye10 aniyede bir ise 9 dan başlasın gibi

    else:
        gameOver=True
        countDownTurtle.clear()
        hideTurtles()
        countDownTurtle.write(arg=f"Oyun Bitti", move=False, align="center", font=FONT)

def startGameUp():
    turtle.tracer(0) # takip edici izleyici. O animasyonları vesaire sıfırladı.
    setupScoreTurtle()
    setupTurtle()
    hideTurtles()
    showTurtlesRandomly()
    countDown(10)
    turtle.tracer(1)

startGameUp()
turtle.mainloop()