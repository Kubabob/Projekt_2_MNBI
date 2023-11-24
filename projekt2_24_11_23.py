#projekt 2

#zad 1

import numpy as np
import matplotlib.pyplot as plt

data = np.array([[1.0, 3.0], [2.0, 1.0], [3.5,4.], [5., 0.], [6., 0.5], [9., -2.], [9.5, -3.0]])


def h(i):
    return data[i+1][0] - data[i][0]

def b(i):
    return (6/h(i)) * (data[i+1][1] - data[i][1])

def u(i):
    if i == 1:
        return 2*(h(i-1) + h(i))
    return 2*(h(i-1) + h(i)) - (h(i-1)**2)/u(i-1)

def v(i):
    if i == 1:
        return b(i) - b(i-1)
    return b(i) - b(i-1) - h(i-1) * (v(i-1)/u(i-1))

def z(i):
    if i == 0 or i == len(data)-1:
        return 0
    else:
        return (v(i) - h(i)*z(i+1))/u(i)
    
def A(i):
    return (z(i+1) - z(i))/(6*h(i))

def B(i):
    return z(i)/2

def C(i):
    return (-h(i)/6) * (z(i+1)+2*z(i)) + (data[i+1][1] - data[i][1])/h(i)

def S(i, x):
    return data[i][1] + (x - data[i][0]) * (C(i) + (x-data[i][0]) * (B(i) + (x-data[i][0])*A(i)))

lista = []
IKSY = []


for i in range(data.shape[0]-1):
    if i == 0:
        iksy = np.linspace(0, data[i+1][0], 20)
    elif i == data.shape[0]-2:
        iksy = np.linspace(data[i][0], 10.5, 20)
    else:
        iksy = np.linspace(data[i][0], data[i + 1][0], 20)

    IKSY.extend(iksy)
    interpolated = S(i, iksy)
    lista.extend(interpolated)
else:
    plt.scatter(data[:,0], data[:,1])
    plt.plot(IKSY, lista)
    plt.show()