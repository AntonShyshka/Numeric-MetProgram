import matplotlib.pyplot as plt
from scipy import interpolate

a = 0.5
b = 0.3
N = [1000000]
S = [990000]
I = [7000]
R = [3000]
t = [0.25]

i = 0
dif = 10
while dif >= 1:
    math = S[i] - S[i]*a
    S.append(math)
    dif = S[i] - S[i+1]
    t.append(t[i] + 0.25)

    math = I[-1] + S[i]*a - I[-1] * b
    I.append(math)

    math = N[-1] - S[-1] - I[-1]
    R.append(math)
    i += 1

Sf = interpolate.interp1d(t, S, kind='cubic')
If = interpolate.interp1d(t, I, kind='cubic')
Rf = interpolate.interp1d(t, R, kind='cubic')

fig = plt.figure()
plt.plot(t, Sf(t))
fig = plt.figure()
plt.plot(t, If(t))
fig = plt.figure()
plt.plot(t, Rf(t))

fig = plt.figure()
plt.plot(t, Sf(t))
plt.plot(t, If(t))
plt.plot(t, Rf(t))

print("S:")
print(S)
print("I:")
print(I)
print("R:")
print(R)
print("T:")
print(t)
plt.show()