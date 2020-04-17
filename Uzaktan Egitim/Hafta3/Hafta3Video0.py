# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 2020

blm202_week_3_lesson_0 Binomial Distribution

@author: Elif Celik
"""

import sympy as sym
from sympy import Symbol
from sympy import pprint
from sympy import matplotlib


p=Symbol('p')
x=Symbol('x')
n=Symbol('n')

my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
print(my_f_3_part_0)

pprint(my_f_3_part_0)


my_f_3_part_1=p**x
print(my_f_3_part_1)

pprint(my_f_3_part_1)


my_f_3_part_2=(1-p)**(n-x)
print(my_f_3_part_2)

pprint(my_f_3_part_2)


my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2
print(my_f_3)

pprint(my_f_3)


sym.plot(my_f_3.subs({p:0.5,n:50}), (x, 0, 50), title='Binomial Distribution Plot for n=50')


