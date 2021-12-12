import matplotlib.pyplot as plt
import numpy as np

from scipy import interpolate
from scipy import integrate

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
time = np.linspace(0, 11, num = 12)
print('Масив часу:')
for times in time:
    print(times, end='8')
print()

fig = plt.figure()
ax = fig.add_subplot(111)
plt.grid(True)
ax.set_xlim([0, 11])
ax.set_ylim([0, 130])
plt.scatter(time, speed, c='b', s=50)

fig = plt.figure()
f = interpolate.interp1d(time, speed, kind='cubic')
plt.plot(time, f(time))

v, err = integrate.quad(f, 0, 11, limit=10000)
print('Кубічний інтеграл: ')
print(v)

fig = plt.figure()
f = interpolate.interp1d(time, speed, kind='quadratic')
plt.plot(time, f(time))

v, err = integrate.quad(f, 0, 11, limit=10000)
print('Квадратичний інтеграл: ')
print(v)

plt.show()