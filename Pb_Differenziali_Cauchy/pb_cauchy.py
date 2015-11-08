# -*- coding: utf-8 -*-
# Programma per la soluzione del problema di cauchy 

import math
import sys
import matplotlib.pyplot as plt

# Definizione della funzione Y'(t) del nostro problema

def f(t,y):
    return y-t

# Definizione della funzione esatta g(t) del nostro problema
def g(t):
    return math.exp(t)+t+1
    
# Dati di Input
t0 = 0
h = 0.2
y0 = 2
n = 10

# Inizializzazione vettori
T = [0]*(n+1)

G = [0]*(n+1)

Ye = [0]*(n+1)
Yh =[0]*(n+1)
Yk= [0]*(n+1)

Ee = [0]*(n+1)
Eh =[0]*(n+1)
Ek= [0]*(n+1)


# Copia delle condizioni iniziali nei rispettivi vettori
T[0] = t0
Ye[0] = y0
Yh[0] = y0
Yk[0] = y0
G[0] = g(t0)

#Definizione della lista dei metodo 
methods = ['Eulero', 'Heun', 'Runge-Kutta']


raw_input("Press any key per continuare...")

#Ciclo per l'implementazione degli algoritmi
for i in xrange(n):
    #Incremento della discretizzazione temporale
    T[i+1] = t0 +h*(i+1)
    #construtto if per la selezione del metodo da utilizzare
   
    Ye[i+1] = Ye[i] + h*f(T[i], Ye[i])
    
    Yh[i+1] = Yh[i] + 0.5*h*(f(T[i], Yh[i]) + f(T[i]+h,Yh[i]+h*f(T[i], Yh[i])))
        
    k1 = f(T[i],Yk[i]);
    k2 = f(T[i] + 0.5*h, Yk[i] + 0.5*h*k1);
    k3 = f(T[i] + 0.5*h, Yk[i] + 0.5*h*k2);
    k4 = f(T[i] + h, Yk[i] + h*k3);  
    Yk[i+1] = Yk[i] + h*(k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    
    G[i+1] = g(T[i+1])
    
    Ee[i+1]= G[i+1]-Ye[i+1]
    
    Eh[i+1]= G[i+1]-Yh[i+1]
    
    Ek[i+1]= G[i+1]-Yk[i+1]
    
    print (T[i+1], Ye[i+1], Yh[i+1], Yk[i+1], g(T[i+1]))

plt.figure("Grafici")
plt.plot(T,Ye, label = methods[0])
plt.plot(T,Yh, label = methods[1])
plt.plot(T,Yk, label = methods[2])
plt.plot(T,G, label = "g(t)")
plt.legend(loc=2)
plt.show()

plt.figure("Errori")
plt.plot(T,Ee, label = methods[0])
plt.plot(T,Eh, label = methods[1])
plt.plot(T,Ek, label = methods[2])
plt.legend(loc=2)
plt.show()

