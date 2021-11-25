import math
from scipy import optimize
x0 = 0.5
y0 = 0.4
def f1(y):
    return -1.2 + math.sin(y+1)
def f2(x):
    return 1 - math.cos(x)/f2
def iter (x, y, e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1 
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn)>=e):
        xn = xn1
        yn = yn1 
        xn1 = f2(yn)
        yn1 = f1(xn1)
        n = 1 
    print ('Simple interation:')
    print ('x1=', xn, '\ny1=', yn, '\nThe amount of interation =', n)
iter (x0, y0, 0.0001)
def f(x):
    return -1.2 + math.sin(x[1]+1)-x[0], 2 * x[1] + math.cos(x[0])-2
s = optimize.root(f, [0, 0], method = 'hybr')
print ('examination', x)