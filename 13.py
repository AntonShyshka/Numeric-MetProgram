from scipy import integrate
from numpy import *
from math import *


def rectangl(x):
    return x / (sqrt(x**2 + 2.3))


v, err = integrate.quad(rectangl, 0.32, 0.66)


def rt_fun(rectangl, a, b, n):
    h = (b - a) / n
    rt = h * ((rectangl(a)+h/2) + (rectangl(b - h)+h/2))
    for i in range(1, n - 1):
        rt += rectangl(a + i * h)/10
    return rt


def rtright_fun(rectangl, a, b, n):
    h = (b - a) / n
    rtr = h * (rectangl(a) + rectangl(b - h))
    for i in range(2, n):
        rtr += rectangl(a + i * h) / 10
    return rtr

def rtleft_fun(rectangl, a, b, n):
    h = (b - a) / n
    rtl = h * (rectangl(a) + rectangl(b - h))
    for i in range(1, n-1):
        rtl += rectangl(a + i * h) / 10
    return rtl

print("middle rectangle method = ", rt_fun(rectangl, 0.32, 0.66, 10))
print("left rectangle method = ", rtleft_fun(rectangl, 0.32, 0.66, 10))
print("right rectangle method = ", rtright_fun(rectangl, 0.32, 0.66, 10))

print('Check for the rectangle method = ', v)


def simpson(x):
    return x * (x / 2 * math.log10(x ** 2 // 2))


def sp_fun(simpson, a, b, n):
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, n // 2 + 1):
        k += 4 * simpson(x)
        x += 2 * h

    x = a + 2 * h
    for i in range(1, n // 2):
        k += 2 * simpson(x)
        x += 2 * h
    return (h / 3) * (simpson(a) + simpson(b) + k)


print("Simpson method= ", sp_fun(simpson, 1.6, 3.2, 8))
v, err = integrate.quad(simpson, 1.6, 3.2)
print('Check for simpson method= ', v)


def trapezoid(x):
    return x / (sqrt(2 * x ** 2 + 1))


def tr_fun(trapezoid, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (trapezoid(a) + trapezoid(b))
    for i in range(1, n):
        sum += trapezoid(a + i * h)
    return sum * h


v, err = integrate.quad(trapezoid, 0.8, 1.6)
print("Trapezoid method = ", tr_fun(trapezoid, 0.8, 1.6, 20))
print('Check for trapezoid method = ', v)



