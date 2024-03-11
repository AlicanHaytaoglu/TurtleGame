import turtle
import random
#Turtle List
turtle_list=[]
#Screen
drawing_board=turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turtle Game ")
FONT=('Arial',30,'normal')
score=0
score_turtle=turtle.Turtle()
def Setup_Score_Turtle():
    #score Turtle

    score_turtle.hideturtle()  # imleci gizledi
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = drawing_board.window_height() / 2  # ekranın yarasından ölçecez çünkü yarısında başlatıyor
    y = top_height * 0.8  # burada y  açılan ekranın aşağıdan yukarıya doğru yüzde 80 ninde dursun diyoruz
    score_turtle.setposition(0, y)  # burada yazının kordinat veriyoruz
    score_turtle.write(arg="Score 0 :", move=False, align='Center', font=FONT)

grid_size=10
def makeTurtle(x,y):
    t=turtle.Turtle()
    def handle_click(x,y):
        global score # globaldaki değişkeni fonksiyon içne atıyor
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score :  {score}", move=False, align='Center', font=FONT)





    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(3,3)
    t.color("red")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)#oluşturulan turtle yi diziye atadık


x_cordinat=[-20,-10,0,10,20]
y_cordinat=[-20,-10,0,10,20]

def setup_turtles():
    for x in x_cordinat:
        for y in y_cordinat:
            makeTurtle(x,y)

def turtle_hide():
    for t in turtle_list:
        t.hideturtle()
def show_turtle_random():
    random.choice(turtle_list).showturtle()#random turtle listen birini seç ve göster

turtle.tracer(0)#animasyonları iptal ettik
Setup_Score_Turtle()
setup_turtles()
turtle_hide()
turtle.tracer(1)#animasyonları aktif ettik
show_turtle_random()
turtle.mainloop()
