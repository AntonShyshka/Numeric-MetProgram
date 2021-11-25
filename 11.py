from math import *
from numpy import *
import sympy as sp
from matplotlib import style

x = sp.symbols('x')

f = 5*sp.cos(x)
n = 1

def tyler(x):

    d1 = sp.diff(f, x)
    d = d1
    y = f

    i = 1
    while i <= n:
        y = y + d*((x-0)**i)/factorial(i)
        d = sp.diff(d, x)
        i += 1
    
    return y

tyler_x = tyler(x)

p1 = sp.plot(f, (x, -3, 3),
title = "Наближення функцій поліномом Тейлора",
ylabel = "y", label = "f(x)", line_color = "#8A2BE2",
show = False, legend = True)

p2 = sp.plot(tyler_x, (x, -3, 3), label = "Наближення до f(x)",
line_color = "#8B0000", show = False)

p3 = sp.plot(x, (x, -3, 3), show = False, line_color = "#0000FF")

p1.append(p2[0])
p1.append(p3[0])
p1.show()

