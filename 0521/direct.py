# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:40:01 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")
t.width(3)
t.shapesize(3, 3)

while True:
    command = t.textinput("방향 결정", "l이나 r입력")
    if command == "l":
        t.left(90)
        t.forward(100)
        
    if command == "r":
        t.right(90)
        t.forward(100)
        
t.exitonclick()
       