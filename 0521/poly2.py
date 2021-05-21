# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:31:22 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")

while True:

    s = t.textinput("", "도형을 입력하시오: ")
    t.reset()
    if s == "사각형" :
        s1 = t.textinput("", "가로: ")
        w = int(s1)
        s2 = t.textinput("", "세로: ")
        h = int(s2)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        
    
    elif s == "삼각형" :
        s3 = t.textinput("", "길이: ")
        w = int(s3)
        t.forward(w)
        t.left(120)
        t.forward(w)
        t.left(120)
        t.forward(w)
        
        
    elif s == "원":
        s4 = t.textinput("", "반지름")
        r = int(s4)
        t.circle(r)
        
    else:
        t.write("사각형, 삼각형, 원중에 하나를 입력하세요 !!!")
        
t.exitonclick()
    
