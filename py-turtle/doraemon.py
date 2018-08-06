import turtle



turtle.setup(width=500, height=600)
pen = turtle.Pen()
pen.shape('turtle')

def set_pos_up_pen(x=0, y=0):
    pen.up()
    pen.setpos(x, y)
    pen.down()


def goto_offset(offset_x, offset_y):
    pen.up()
    pos = pen.pos()
    x = pos[0] + offset_x
    y = pos[1] + offset_y
    pen.goto(x, y)
    pen.down()



def head(x, y):
    pen.up()
    pen.circle(150, 40)
    pen.down()
    pen.fillcolor('#00a0de')
    pen.begin_fill()
    pen.circle(150, 280)
    pen.end_fill()

def weubo():
    set_pos_up_pen(0, 40)
    pen.seth(0)
    pen.backward(105)
    pen.fillcolor('red')
    pen.begin_fill()
    for _ in range(2):
        pen.forward(210)
        pen.circle(-5, 90)
        pen.forward(10)
        pen.circle(-5, 90)
    pen.end_fill()


def face():
    set_pos_up_pen(86, 40)
    pen.seth(0)
    pen.fillcolor('#ffffff')
    pen.begin_fill()
    pen.left(45)
    pen.circle(120, 270)
    pen.end_fill()

    pen.up()
    pen.home()
    pen.seth(90)
    pen.forward(240)
    pen.down()
    pen.begin_fill()
    pen.circle(-30)
    pen.circle(30)
    pen.end_fill()
    #黑眼
    pen.seth(220)
    pen.up()
    pen.forward(10)
    pen.seth(90)
    pen.down()
    pen.color('#000')
    pen.begin_fill()
    pen.circle(15)
    pen.end_fill()
    #眼白
    goto_offset(-10, 0)
    pen.seth(90)
    pen.dot(10, 'white')

    #眨眼
    goto_offset(35, -5)
    pen.pensize(5)
    color_circle(r=-10, angle=180, seth=90, is_fill=False)
    pen.pensize(1)
    #鼻子
    goto_offset(-52, -30)
    color_circle(r=15, color='red', seth=-90)
    #嘴巴
    goto_offset(15, -20)
    pen.seth(-90)
    pen.forward(120)
    color_circle(r=100, angle=40, color='red', seth=0, is_fill=False)
    pen.left(180)
    pen.circle(-100, 80)
    #左胡须
    goto_offset(-10, 10)
    pen.seth(20)
    pen.forward(50)
    goto_offset(0, 10)
    pen.seth(180)
    pen.forward(50)
    goto_offset(0, 30)
    pen.seth(-20)
    pen.forward(50)
    #右胡须
    goto_offset(50, 0)
    pen.seth(20)
    pen.forward(50)
    goto_offset(0, -30)
    pen.seth(180)
    pen.forward(50)
    goto_offset(0, -10)
    pen.seth(-20)
    pen.forward(50)


def lingdang():
    #铃铛
    r = 25
    pen.up()
    pen.setpos(0, -r)
    pen.down()
    pen.seth(-90)
    color_circle(r=r, seth=0, color='yellow')
    set_pos_up_pen()
    pen.dot(10)
    pen.seth(-90)
    pen.forward(r)
    pen.seth(180)
    pen.circle(-r, 130)
    pen.seth(0)
    pen.forward(40)
    goto_offset(-2, 2)
    pen.backward(40)

def line_by_seth(l, seth=0, use_seth=True):
    if use_seth:
        pen.seth(seth)
    pen.forward(l)


def body():
    start_angle = -135
    set_pos_up_pen(-90, 20)
    pen.fillcolor('#00a0de')
    pen.begin_fill()
    line_by_seth(l=100, seth=start_angle)
    pen.circle(15, 180)
    pen.forward(50)
    line_by_seth(l=150, seth=-90)
    line_by_seth(l=50, seth=0)
    pen.seth(90)
    pen.circle(-50, 180)
    line_by_seth(l=50, seth=0)
    line_by_seth(l=150, seth=90)
    line_by_seth(l=100, seth=45)
    pen.circle(15, 220)
    line_by_seth(l=50, seth=-150)
    pen.end_fill()


def belly():
    #肚皮
    set_pos_up_pen(0, 40)
    color_circle(r=80, color='#fff', seth=180)
    #口袋
    l = 40
    set_pos_up_pen(0, -60)
    line_by_seth(l, seth=180)
    color_circle(r=l, angle=180 ,seth=-90, is_fill=False)
    line_by_seth(l, seth=180)

def footers():
    def foot():
        pen.fillcolor('#fff')
        pen.begin_fill()
        pen.seth(0)
        for _ in range(2):
            pen.forward(40)
            pen.circle(-20, 90)
            pen.forward(10)
            pen.circle(-20, 90)
        pen.end_fill()
    set_pos_up_pen(-100, -180)
    foot()
    pen.up()
    pen.forward(150)
    pen.down()
    foot()

def hands():
    set_pos_up_pen(-150, -80)
    color_circle(20, color='#fff')
    set_pos_up_pen(160, 30)
    color_circle(20, color='#fff')


def color_circle(r, angle=360, color='black', seth=0, is_fill=True):
    pen.seth(seth)
    pen.fillcolor(color)
    if is_fill:
        pen.begin_fill()
    pen.circle(r, angle)
    if is_fill:
        pen.end_fill()




if __name__ == '__main__':
    pen.speed(0)
    head(0, 0)
    face()
    body()
    belly()
    weubo()
    lingdang()
    hands()
    footers()
    pen.up()
    pen.setpos(1000, 1000)
    turtle.mainloop()


