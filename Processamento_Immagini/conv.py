from PIL import Image
from scipy import signal as sg

import numpy as np

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

#Definizione del kernel derivata 
kernel = np.matrix([-1.,1])

#Convoluzione per il calcolo della derivata nella direzione X
img_derivata_x = sg.convolve(img, kernel)
img_derivata_x_norm = norm(img_derivata_x)
save_as_img(img_derivata_x_norm,'lena-derivata_x.bmp')


#Convoluzione per il calcolo della derivata nella direzione Y
img_derivata_y = sg.convolve(img, kernel.T)
img_derivata_y_norm = norm(img_derivata_y)
save_as_img(img_derivata_y_norm,'lena-derivata_y.bmp')

#Apertura dei risultati 
img_from_np(img_derivata_x_norm).show()
img_from_np(img_derivata_y_norm).show()


