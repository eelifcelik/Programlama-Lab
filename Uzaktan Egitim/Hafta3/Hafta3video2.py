# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 

blm202_week_3_lesson_2 Integral 

@author: Elif
"""

from sympy import Symbol, exp, sqrt, pi, Integral 


x = Symbol('x') 
p = exp(-(x - 10)**2/2)/sqrt(2*pi)

Integral(p, (x, 11, 12)).doit().evalf() 

