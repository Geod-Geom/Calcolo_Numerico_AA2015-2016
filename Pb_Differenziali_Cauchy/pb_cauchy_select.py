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
l = 2.0
t0 = 0

y0 = 2
n = 10
h = l/n

# Inizializzazione vettori
T = [0]*(n+1)
Y = [0]*(n+1)
G = [0]*(n+1)

# Copia delle condizioni iniziali nei rispettivi vettori
T[0] = t0
Y[0] = y0
G[0] = g(t0)

#Scelta del metodo da utilizzare 
print "Scegliere il metodo 1:Eulero 2:Heun 3:Runge-Kutta"
metodo = input("Inserire il metodo: ")

#Definizione della lista dei metodo 
methods = ['Eulero', 'Heun', 'Runge-Kutta']

if metodo == 1:
    print "E' stato selezionato il metodo di "+methods[0]
elif metodo == 2:
    print "E' stato selezionato il metodo di "+methods[1]
elif metodo == 3:
    print "E' stato selezionato il metodo di "+methods[2]
else:
    print "Il metodo selezionato non è valido" 
    sys.exit()

raw_input("Press any key per continuare...")

#Ciclo per l'implementazione degli algoritmi
for i in xrange(n):
    #Incremento della discretizzazione temporale
    T[i+1] = t0 +h*(i+1)
    #construtto if per la selezione del metodo da utilizzare
    if  metodo    ==1:
        Y[i+1] = Y[i] + h*f(T[i], Y[i])
    elif metodo ==2:
        Y[i+1] = Y[i] + 0.5*h*(f(T[i], Y[i]) + f(T[i]+h,Y[i]+h*f(T[i], Y[i])))
    elif metodo == 3:    
        k1 = f(T[i],Y[i]);
	k2 = f(T[i] + 0.5*h, Y[i] + 0.5*h*k1);
	k3 = f(T[i] + 0.5*h, Y[i] + 0.5*h*k2);
	k4 = f(T[i] + h, Y[i] + h*k3);  
        Y[i+1] = Y[i] + h*(k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    
    G[i+1] = g(T[i+1])
    print (T[i+1], Y[i+1], g(T[i+1]))

plt.plot(T,Y, label = methods[metodo-1])
plt.plot(T,G, label = "g(t)")
plt.legend(loc=2)
plt.show()