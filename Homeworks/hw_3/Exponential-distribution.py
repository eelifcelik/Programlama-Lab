# -*- coding: utf-8 -*-
"""
Exponential Distribution

Sabit ortalama değişme haddinde ortaya çıkan bağımsız olaylar arasındaki
zaman aralığını modelleştirirken bir üstel dağılım doğal olarak ortaya çıkar.


@author: Elif CELIK-180401055
"""
#Gerekli kütüphaneleri ekledik
import sympy as sym                 
from sympy import Symbol
from sympy import pprint
import matplotlib.pyplot as plt

#x ve lambda'yı sembol şeklinde tanımladık
x = Symbol('x')
lamda = Symbol('lambda')


part1 = lamda * x # Exponential Distribution formulundeki e sayısının üssünü ayrı olarak tanımladık.
part2 = sym.exp(- part1) # Sympy kütüphanesindeki exp() fonksiyonunu kullanarak daha önceden tanımladığımız part1 i e'nin üssü olarak tanımladık.

expdis = lamda * part2 #part2 yi lambda ile çarparak Exponential Distribution PDF(Probability Density Function)yi elde ettik.

print(" Exponential distribution formula:")
pprint(expdis) #pprint fonksiyonu ile daha güzel bir şekilde Exponential Distribution formulunu yazdırdık.

sym.plot(expdis.subs({lamda:1}),(x,0,5),title="Exponential Disturbiton")  #lambdayı 1 kabul ettik, x değerleri (0,5) aralığındayken grafiğimizi çizdirdik.
plt.show()

#x ve y eksenindeki değerleri tutması için iki boş dizi tanımladık.
xaxis = []
yaxis = [] 


for value in range(6): # x değerlerini y değerlerine eşleştirmek için bir for döngüsü yazdık            

    y = expdis.subs({lamda: 1, x: value}).evalf() # x değerine göre lambda 1 olacak biçimde expdis kullanarak y sayıları elde ettik 
    yaxis.append(y)  # Bu y sayılarını oluşturdugumuz bos listeye ekledik.
    xaxis.append(value) #value değerlerini xaxis bos dizimize ekledik.

    print(value, y) #değerleri yazdırdık.

plt.plot(xaxis, yaxis)#matplotlib ile grafiğimizi çizdirdik.
