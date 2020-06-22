import pandas as pd
import numpy as np
import pylab as plt
import seaborn
import math

main_arr = np.arange(2, 32)

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i_one = []
k = []
l = []
m = []
n = []
o = []
p = []
r = []
s = []
for i in range(1,88):
    a.append(math.log(main_arr[i], 2))    
for i in range(1,88):
    b.append(math.sqrt(math.log(main_arr[i], 4)))
for i in range(1,88):
    c.append(math.log(main_arr[i], 3))
for i in range(1,88):
    d.append(math.log(main_arr[i], 2) ** 2)
for i in range(1,88):
    e.append(math.sqrt(main_arr[i]))
for i in range(1,88):
    f.append(i / math.log(main_arr[i], 5))
for i in range(1,88):
    g.append(math.log(math.factorial(main_arr[i]),2))
for i in range(1,88):
    h.append(3 ** math.log(main_arr[i], 2))
for i in range(1,88):
    i_one.append(main_arr[i] ** 2)
for i in range(1,88):
    k.append(7 ** (math.log(main_arr[i], 2)))
for i in range(1,88):
    l.append(math.log(main_arr[i], 2) ** (math.log(main_arr[i], 2)))
for i in range(1,88):
    m.append(i ** (math.sqrt(main_arr[i])))
for i in range(1,88):
    n.append(main_arr[i] ** (math.log(main_arr[i], 2)))
for i in range(1,88):
    o.append(2 ** main_arr[i])
for i in range(1,88):
    p.append(4 ** main_arr[i])
for i in range(1,88):
    r.append(2 ** (3 * main_arr[i]))
for i in range(1,88):
    s.append(math.factorial(main_arr[i]))

plt.rc('figure', figsize=(20, 15))
plt.plot(a, range(1,88), 'o-', label='1')
plt.plot(b, range(1,88), 'o-', label='2')
plt.plot(c, range(1,88), 'o-', label='3')
plt.plot(d, range(1,88), 'o-', label='4')
plt.plot(e, range(1,88), 'o-', label='5')
plt.plot(f, range(1,88), 'o-', label='6')
plt.plot(g, range(1,88), 'o-', label='7')
plt.plot(h, range(1,88), 'o-', label='8')
plt.plot(i_one, range(1,88), 'o-', label='9')
# plt.plot(k, range(1,88), 'o-', label='10')
# plt.plot(l, range(1,88), 'o-', label='11')
# plt.plot(m, range(1,88), 'o-', label='12')
# plt.plot(n, range(1,88), 'o-', label='13')
# plt.plot(o, range(1,88), 'o-', label='14')
# plt.plot(p, range(1,88), 'o-', label='15')
# plt.plot(r, range(1,88), 'o-', label='16')
# plt.plot(s, range(1,88), 'o-', label='17')


plt.show()
print (b)

#print(2 ** (2 ** n))