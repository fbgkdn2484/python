# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:12:09 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")
t.clear()
colorList = ["yellow", "red", "blue", "green"]

for i in range(4):
    t.pendown()
    t.fillcolor(colorList[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()
    t.forward(50)
    
t.exitonclick()