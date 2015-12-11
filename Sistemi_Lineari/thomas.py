import math
import sys
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA

def THOMAS(d, s, a, B):
    N = A_diag.size
    alfa = np.zeros(N)  # Vettore alfa matrice L 
    u = np.zeros(N) 
    v = np.zeros(N) #Vettori U e V matrice U
    y = np.zeros(N) #Vettore soluzione Y=UX
    X = np.zeros(N)
	
    # Troviamo i componenti delle due matrici L e U
    # che vogliamo utilizzare per fattorizzare la matrice A
    # come A = LU
	 
    u[0] = d[0]
    for i in xrange(N-1):
	v[i] = s[i];
	
    for i in xrange(1,N):	
	alfa[i] = a[i]/u[i-1];
	u[i] = d[i] - alfa[i] * v[i-1]
    
    # Soluzione del sistema triangolare inferiore LY = B (dove Y = UX) con 
    # il metodo della sostituzione in avanti */
	
    y[0] = B[0];
    for i in xrange(1,N):
        y[i] = B[i] - alfa[i] * y[i-1]
	

    # Soluzione del sistema triangolare superiore UX = Y con
    # il metodo della sostituzione all'indietro */
    
    X[N-1] = y[N-1] / u[N-1]
    for i in xrange(2,N+1):
        X[N-i] = (y[N-i] - v[N-i] * X[N-i+1]) / u[N-i]
        
    print X



N = 5
A_diag = np.random.rand(N)
A_sup = np.random.rand(N)
A_inf = np.random.rand(N)
B = np.random.rand(N)

THOMAS(A_diag,A_sup,A_inf,B)