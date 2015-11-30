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
import sys
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as LA

N = 3 

A = np.random.rand(N,N)
A_diag = np.diag(np.random.rand(N))*10
A = A+A_diag

B = np.random.rand(N)

# Scomposizione della matrice A
D = np.diag(A.diagonal())
L = np.tril(A, k=-1)
U = np.triu(A, k=1)

# Costruzione delle Matrici Cj e Qj
Cj = -LA.inv(D).dot(L+U)
Qj = LA.inv(D).dot(B)


# Verifica della condizione di convergenza 
Raggio_Spettrale = LA.norm(LA.eigvals(Cj))
if(Raggio_Spettrale > 1):
    print "Il metodo iterativo non converge"
    sys.exit()
        
X = np.zeros(N, dtype='float64')
X0 = np.zeros(N, dtype='float64')

err_K = 1000
eps = 0.0001
num_iter = 0

while (err_K > eps and num_iter < 100):
    num_iter=num_iter+1
    X = Cj.dot(X0)+Qj
    
    # Calcolo dell'errore K
    err_K = LA.norm(X-X0)
    
    # Aggiornamento delle variabili 
    X0 = X.copy()

print "Sono state effettuate ", num_iter, " iterazioni"
print X   
print "La soluzione con il metodo diretto"
print LA.solve(A,B)	