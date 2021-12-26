import turtle
from turtle import Screen
import random
import pygame
from tkinter import*
from tkinter import font
from tkinter.messagebox import*

str = ['总有些惊奇的际遇','比方说当我遇见你','我知道你也在向我靠近','星河万顷都是我的见面礼','接下来是我赠予你的星河万里','关闭窗口获得惊喜']
def drawPetal(n):
    # 指定颜色模式为 rgb 模式
    turtle.colormode(255)
    # 随机生成 rgb 色值
    r = random.randint(100, 255)
    g = random.randint(8, 158)
    b = random.randint(8, 158)

    # 画圆并填充颜色
    turtle.begin_fill()
    turtle.fillcolor(r, g, b)
    turtle.pencolor(r, g, b)
    turtle.circle(n)
    turtle.end_fill()

def music():
    pygame.mixer.init()
    track=pygame.mixer.music.load("star.wav")
    pygame.mixer.music.play()


def reply():#定义函数，用于多次生成弹窗
    for i in range(6):#循环语句，循环次数为5
        showinfo(title="love you forever",message=str[i])#显示弹窗
        
def window_init():
    root=Tk()#调用Tk()函数建立根窗口
    root.title("点我有惊喜")#设置根窗口标题
    root.geometry("400x400")#设置根窗口大小
    root.resizable(False,False)#禁止更改根窗口的大小
    ziti=font.Font(family='微软雅黑',size=10,weight=font.BOLD)#设置字体的属性
    mylabel=Label(root,text="请点击按钮有惊喜等着你",font=ziti)#建立文本标签
    mylabel.place(x=1,y=1,anchor=CENTER)#设置文本标签的摆放位置
    create=Button(root,text='惊喜按钮',command=reply,bg="green")#创建按钮组件，点击按钮出现弹窗
    create.place(relx=0.5,rely=0.6,anchor=CENTER,width=100)#设置按钮组件的摆放位置
    mylabel.pack()#将Label添加到窗口
    root.mainloop()#让根窗口持续展示

def draw_init():
    turtle.screensize(800,600, "white")#设置画布大小
    turtle.title("给伶伶的圣诞惊喜")
    turtle.setup(0.5,0.75)
    turtle.pensize(5)
    turtle.speed(8)
    turtle.bgcolor("white")
    turtle.bgpic("snow.gif")
    turtle.getscreen().colormode(255)
    turtle.up()
    turtle.goto(100,-100)
    turtle.down()
    turtle.color("red","green")

def draw_tree():
    turtle.begin_fill()
    for i in range(5):      
        turtle.forward(90 - i * 10)
        turtle.left(145)
        turtle.forward(130 - i * 10)
        turtle.right(145)
    turtle.right(145)
    #print(turtle.pos())
    for j in range(5):
        turtle.forward(90 + j * 10)
        turtle.left(145)
        turtle.forward(50 + j * 10)
        turtle.right(145)

    turtle.left(145)  
    turtle.forward(65)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(65)
    turtle.end_fill()

#画雪花
def draw_snow(num):
    for a in range(num):
        x = random.randint(-400,400)
        y = random.randint(-300,300)
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.dot(10,"white")


def snow(snow_count):
    turtle.hideturtle()
    turtle.speed(300)
    turtle.pensize(3)
    for i in range(snow_count):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        turtle.pencolor(r, g, b)
        turtle.pu()
        turtle.goto(random.randint(-350, 350), random.randint(-300, 300))
        turtle.pd()
        dens = random.randint(6, 12)
        snowsize = random.randint(4, 12)
        for _ in range(dens):
            turtle.forward(snowsize)  # 向当前画笔方向移动snowsize像素长度
            turtle.backward(snowsize)  # 向当前画笔相反方向移动snowsize像素长度
            turtle.right(360 / dens)  # 顺时针移动360 / dens度
 


def draw_star():
    turtle.up()
    turtle.goto(-25.53,240.47)
    turtle.down()
    turtle.color("yellow","yellow") #颜色填充函数
    turtle.begin_fill()
    for c in range(5):
        turtle.forward(50)
        turtle.right(144)
        if abs(turtle.pos()) < 1:#看画笔是否回到原点，回到原点为真
            break
    turtle.end_fill()


def write_str():
    turtle.up()
    turtle.goto(-173.53,-240.47)
    turtle.down()
    turtle.color(255,255,0)
    turtle.write("Merry Christmas to my dear LING",font=("Arial", 20, "normal"))
    turtle.up()
    turtle.goto(-178.53,-240.47)
    turtle.down()
    turtle.color(0,20,250)
    turtle.write("Merry Christmas to my dear LING",font=("Arial", 20, "normal"))




music()
window_init()
draw_init()
draw_tree()
draw_snow(100)
snow(50)
draw_star()
write_str()
screen = Screen()
screen.mainloop()










        
    
