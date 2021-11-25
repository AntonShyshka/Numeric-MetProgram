from numpy import *
linspace
import matplotlib.pyplot as plt
def sd(x):
    return cos(x**4)//x
x = linspace(0,3,51)
y = sd(x)
plt.plot(x,y,'g--', label='5sin(x)ln(x2)x')
plt.title('LB 7.0 Anton Shyshka')
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()