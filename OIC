#40行代码画国旗 By:Atuer
import turtle as t
t.speed(1000000000000)
ss = [3,1,1,1,1],[5,10,12,12,10],[5,2,4,7,9]
def fl4g(wight,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.color('red')
    t.fillcolor('red')
    hzl=wight/3*2
    t.begin_fill()
    for i in range(2):
        t.fd(wight)
        t.right(90)
        t.fd(hzl)
        t.right(90)
    t.end_fill()
    t.color('yellow')
    t.fillcolor('yellow')
    for i in range(5):
        star(wight/2/15 * ss[0][i],0, x + wight/2/15 * ss[1][i], y - hzl/2/10 * ss[2][i])
    t.hideturtle()
    t.down()
def star(size,du,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.left(18+du)
    for i in range(5):
        t.begin_fill()
        for j in range(1,-2,-2):
            t.fd(size)
            t.right(j*(180-18))
            t.fd(size)
            t.goto(x,y)
            t.left(j*(180-18))  
        t.end_fill()
        t.right(72)
    t.right(18+du)
#国旗宽度 坐标x,y
fl4g(25,-100,375)
fl4g(50,-100,350)
fl4g(100,-100,300)
fl4g(200,-100,200)
fl4g(400,-100,0)
