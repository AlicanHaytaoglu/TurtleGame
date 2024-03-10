import turtle

#Screen
drawing_board=turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turtle Game ")
FONT=('Arial',30,'normal')

#score Turtle
score_turtle=turtle.Turtle()
score_turtle.hideturtle()# imleci gizledi
score_turtle.color("dark blue")
score_turtle.penup()
top_height=drawing_board.window_height()/2#ekranın yarasından ölçecez çünkü yarısında başlatıyor
y=top_height*0.8#  burada y  açılan ekranın aşağıdan yukarıya doğru yüzde 80 ninde dursun diyoruz
score_turtle.setposition(0,y) # burada yazının kordinat veriyoruz
score_turtle.write(arg="Score 0 :",move=False,align='Center',font=FONT)




turtle.mainloop()