from PIL import Image
from scipy import signal as sg

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

import os

#Inserire la working directory 
os.chdir('/Users/andreanascetti/Desktop/Python_Images')

#Funzione per convertire le immagini in matrici numpy

def np_from_img(fname):
    return np.asarray(Image.open(fname), dtype=np.float32)

def save_as_img(ar, fname):
    Image.fromarray(ar.round().astype(np.uint8)).save(fname)

def img_from_np(ar):
    return Image.fromarray(ar.round().astype(np.uint8))

def norm(ar):
    return 255.*np.absolute(ar)/np.max(ar)
    
#Apertura del file immagine e trasformazione in matrice numpy    
img = np_from_img("lena.png")

#Definizione del kernel del filtro di Sobel
sobel_K = np.matrix([[-1.,0,1.],[-2.,0,2.],[-1.,0,1.]])

#Calcolo delle derivate in X e Y 
Gx_Conv = sg.convolve(img, sobel_K)
Gy_Conv = sg.convolve(img, sobel_K.T)

#Calcolo della derivata risultante
G = norm(np.hypot(Gx_Conv, Gy_Conv))

#Salvataggio dell'immagine filtrata
save_as_img(G,'lena-sobel.bmp')

#Apertura del risultato 
img_from_np(G).show()