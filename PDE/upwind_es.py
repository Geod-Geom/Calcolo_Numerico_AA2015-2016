def F_t0(x):
    ... Parte Mancanti 
    ...
    ...
    ...
# Intervallo spaziale e temporale
a = 0.0  b = 2.0  c = 0.0   d = 1.0
# Discretizzazione spaziale e temporale
h = 0.04    k = 0.02   alpha = 0.5
	
N = int((b-a)/h) # Numero di nodi 
M = int((d-c)/k) # Numero di passi temporali 
		
#Phi[N+1][2];
Phi = np.zeros((N+1,2),dtype=np.float)
						
# Costruzione della condizione iniziale	
for i in xrange(N+1):
    ... Parte Mancanti 
    ...
    ...
    ...

U = np.zeros((N+1,M+1))
# Copia della Condizione iniziale 
for i in xrange(N+1):
    ... Parte Mancanti 
    ...
    ...
    ...
		
# Condizione al bordo	
for j in xrange(M+1):
    ... Parte Mancanti 
    ...
    ...
    ...


# Algoritmo di upwind
    ... Parte Mancanti 
    ...
    ...
    ...

        