
import numpy as np
import matplotlib.pyplot as plt

# Model Y = ax+c
def model(x):
    a  = 1.156
    c  = 10.1234
    return a*x+c

t  = np.zeros(100)
S  = np.zeros(100)

S_noise = np.random.randn(100)

for i in xrange(100):
    t[i] = i 
    S[i] = model(i) + S_noise[i]*100
    
plt.figure("Grafico rumore")
plt.plot(t,S,'o')
plt.show()

A  = np.vstack([t,np.ones(len(t))]).T

print A
#
m_lq ,c_lq = np.linalg.lstsq(A, S)[0]

print m_lq, c_lq
