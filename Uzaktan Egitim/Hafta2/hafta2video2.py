import sympy as sym
from sympy import Symbol
from sympy import pprint

import sympy.plotting as syp

sigma= Symbol('sigma')
mu = Symbol('mu')
x = Symbol('x')

sym.sqrt(2*sym.pi*sigma)
pprint(1/(sym.sqrt(2*sym.pi*sigma*sigma)))

part1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gaussfunction = part1*part2
pprint(my_gaussfunction)

syp.plot(my_gaussfunction.subs({mu:10, sigma:30}), (x, -100, 100), title='gauss distribution')



x_values = []
y_values = []

for value in range (-5, 5):
    y = my_gaussfunction.subs({mu:10, sigma:30, x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)

import matplotlib.pyplot as plt

plt.plot(x_values,y_values)
plt.show()



