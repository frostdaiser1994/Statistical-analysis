import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

r = float(input()) # время течения раствора в секундах

#c = [0.1, 0.066, 0.05, 0.04] # концентрация альгината в растворе в процентах

#ds = [218.38, 170.43, 149.72, 137.81] # время течения образца альгината в секундах (в зависимости от его концентрации)

c = []

n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
    ele = float(input())

    c.append(ele)  # adding the element

ds = []

v = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, v):
    k = float(input())

    ds.append(k)  # adding the element

prop = ((np.array(ds)/r) - 1)/np.array(c) # нахождение пропорциональных точек вязкости
logarithmic = (np.log(np.array(ds)/r))/np.array(c) # нахождение логарифмических точек вязкости

#print(prop)
#print(logarithmic)



x = np.array(c)
y1 = np.array(prop)
y2 = np.array(logarithmic)
x2 = np.arange(-0.8, 0.4, 0.05)

plt.scatter(x, y1)
plt.scatter(x, y2)

z1 = np.polyfit(x, y1, 1)
p1 = np.poly1d(z1)

z2 = np.polyfit(x, y2, 1)
p2 = np.poly1d(z2)

np.polyval(np.polyfit(x, y1, 1), x)

plt.plot(x2, p1(x2)) # построение линии тренда по пропорциональным точкам вязкости
plt.plot(x2, p2(x2)) # построение линии тренда по логарифмическим точкам вязкости

plt.xticks(np.arange(0, 0.2, step=0.05))
plt.yticks(np.arange(0, 20, step=1))
#plt.show()

#plt.savefig('MW.png', format='png', dpi=300)

#print(a)


idx = np.argwhere(np.diff(np.sign(p1(x2) - p2(x2)))).flatten()
plt.plot(x2[idx], p1(x2)[idx], 'ro')
plt.text(x2[idx]+0.1, p1(x2)[idx], "S", horizontalalignment="center")
p_cross = (p1(x2)[idx])
plt.show()

print(p_cross)
b = p_cross/7.3/(10**-5)
print(b**(1/0.92))
