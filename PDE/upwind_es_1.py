import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def F_t0(x):
    if((x <= 3.0/2.0) & (x >= 1.0/2.0)):
	return (1.0/2.0 - x)*(x - 3.0/2.0)
    else:
        return 0;

#Input del programma upwind

# Intervallo spaziale 
a = 0.0
b = 2.0
# Intervallo temporale 
c = 0.0
d = 1.0
# Discretizzazione spaziale e temporale
h = 0.04
k = 0.02
#Numero di Courant 
alpha = 0.5
	
N = int((b-a)/h) # Numero di nodi 
M = int((d-c)/k) # Numero di passi temporali 

print (N,M)
		
#Phi[N+1][2];
Phi = np.zeros((N+1,2),dtype=np.float)
						
# Costruzione della condizione iniziale	
for i in xrange(N+1):
    Phi[i][0] = a
    Phi[i][1] = F_t0(Phi[i][0])
    a += h
    print(Phi[i][0], Phi[i][1])
	
U = np.zeros((N+1,M+1))
	
# Copia della Condizione iniziale 
for i in xrange(N+1):
    U[i][0] = Phi[i][1]
		
# Condizione al bordo	
for j in xrange(M+1):
    U[0][j] = 0.0


# Algoritmo di upwind
    ... Parte Mancanti 
    ...
    ...
    ...

        