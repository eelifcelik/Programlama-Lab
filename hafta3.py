#ElifCelik Programlama Lab 3. Hafta Cuma
#Zar için olasilik hesabi 
from sympy import FiniteSet

t = FiniteSet(1,2,3)
s = FiniteSet(2,4,6)

t==s
t.union(s)
t.intersect(s)

t**2

#probability calculation
def probability(space, event):
  return len(event)/len(space)

#is it prime number 
def check_prime(number):
  if number!=1:
    for factor in range(2,number):
      if number % factor == 0:
        return False
  else:
    return False
  return True


space = FiniteSet(*range(1,21))
primes=[]
for num in space:
  if check_prime(num):
    primes.append(num)

event = FiniteSet(*primes)
p = probability(space, event)
print(p)    
