'''
Author: your name
Date: 2023-03-21 13:35:00
LastEditTime: 2023-03-21 13:38:10
LastEditors: LAPTOP-IMEC0GP4
Description: In User Settings Edit
FilePath: \python_schedule\etest1.8.py
'''
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()
