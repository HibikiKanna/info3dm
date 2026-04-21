import numpy as np

#1
a = np.ones((5,1))
print(a)

#2
a[2,0] =3.14
print(a)

#3
b = a.T
print(b)

#4
c = np.dot(b,a)
print(c)

#5
d = np.random.rand(10, 1)
print(d)

#6
e = np.random.normal(10, 2, (2,5))
print(e)

#7
f = e[:,1]
print(f)

#8
g = e[:,2:4]
print(g)

#9
h = np.random.rand(5,2)
i = e @ h
print(i)