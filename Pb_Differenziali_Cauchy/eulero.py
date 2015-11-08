#Programma Eulero

import math

import matplotlib.pyplot as plt

def g(t):
    return math.exp(t)+t+1
    
def f(t,y):
    return y-t

# Dati di Input
t0 = 0
h =  0.1
y0 = 2
n = 20

# Inizializzazione vettori
T = [0]*(n+1)
Y = [0]*(n+1)
G = [0]*(n+1)

# Eulero Algoritmo
T[0] = t0
Y[0] = y0
G[0] = g(t0)

for i in xrange(n):
    T[i+1] = t0 +h*(i+1)
    Y[i+1] = Y[i] + h*f(T[i], Y[i])
    G[i+1] = g(T[i+1])
    print (T[i], Y[i], g(T[i]))

plt.plot(T,Y, label = "Eulero")
plt.plot(T,G, label = "g(t)")
plt.legend(loc=2)
plt.show()

