# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:11:20 2021

@author: Mac_1
"""

import turtle as t
import random as r

t.shape("turtle")
screen = t.Screen()
image1 = "front.gif"
image2 = "back.gif"
screen.addshape(image1) 
screen.addshape(image2) 

while True:
    t.delay(500)
    coin = r.randint(0, 1)
    
    if coin == 0:
        t.shape(image1)
        t.stamp()
    else:
        t.shape(image2)
        t.stamp()
        
        
t.exitonclick()