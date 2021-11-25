import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import*
x = [0.3, 0.5, 0.8, 1.2, 1.7]
y = [2.38, 2.94, 1.46, 1.28, 2.15]
spl = UnivariateSpline(x, y)
xs = linspace(0, 4.5, 1000)
plt.plot(x, y, 'ro', xs, spl(xs), 'g')
plt.title('Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(x)
plt.grid()
plt.show()