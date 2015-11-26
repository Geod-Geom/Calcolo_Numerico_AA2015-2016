# -*- coding: utf-8 -*-
#  Soluzione di un sistema lineare con il metodo di Jacobi
#
#  AX = B
# 
#  Input:
#  - n: dimensioni del sistema lineare
#  - A(n,n): matrice dei coefficienti viene fornita tramite un file "matriceA.dat"
#  - B(n): vettore dei termini noti viene fornito tramite un file "vettoreB.dat"
#  - e: accuratezza richiesta nell’approssimazione
#
#  Output:
#  - X(n,n): soluzione approssimata 
#  - num_iter: numero di iterazioni
#  - err_k: differenza tra le ultime due approssimazioni in norma 1  


import math
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA


A = np.genfromtxt("/Users/andreanascetti/Desktop/matriceA.dat")
B = np.genfromtxt("/Users/andreanascetti/Desktop/vettoreB.dat")

N = B.size

X = np.zeros(N)

X0 = np.zeros(N)

err_K = 1000
eps = 0.00001
num_iter = 0

while (err_K > eps and num_iter < 100):
    
    num_iter=num_iter+1
    
    # Calcolo della soluzione K
    for i in xrange(N):
        for j in xrange(i):
            X[i] = A[i][j]*X[j] + X[i]
        for j in xrange(i+1,N):
            X[i] += A[i][j]*X0[j]
			
	X[i]=(-X[i]+B[i])/A[i][i];
    
    # Calcolo dell'errore K
    err_K = LA.norm(X-X0)

    # Aggiornare variabili per la prossima iterazione
    for i in xrange(N):
        X0[i]=X[i]
        X[i]=0.0
	
    # Stampa risultato K 
    print X0  
   	