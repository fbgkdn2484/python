# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:53:28 2021

@author: Mac_1
"""

import turtle as t
import random as r

t.shape("turtle")

for i in range(3000):
    length = r.randint(1, 100)
    t.forward(length)
    angle = r.randint(-180, 180)
    t.left(angle)
    
t.done()
    