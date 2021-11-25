from scipy.interpolate import lagrange
from numpy import *
import matplotlib.pyplot as plt
def jop(x):
return 2*x**3-15*x+5
x = array([-3, -2, -1, 0],dtype =float)
y = array([4, 4, 0, -2], dtype = float)
U = array([-4, -3.5, -0.5, 1])
def L(x, y, k):
summa=0
for g in range (len(y)):
p1=1
p2=1
for i in range (len(y)):
if i==g:
p1 *= 1
p2 *= 1
else:
p1*=(k-x[i])
p2*=(x[g]-x[i])
summa += y[g]*p1/p2
return summa
xnew = linspace (min(x), max(x))
ynew = [L(x,y,i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.title('LB_7 Anton Shyshka')
plt.legend(loc='upper left')
plt.xlabel('x')

