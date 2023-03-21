'''
Author: your name
Date: 2023-02-21 20:30:28
LastEditTime: 2023-03-21 13:27:03
LastEditors: LAPTOP-IMEC0GP4
Description: In User Settings Edit
FilePath: \python_schedule\e2.1DrawPython.py
'''
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("blue")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40*2/3)
