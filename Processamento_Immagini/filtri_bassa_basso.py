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

img_n = np_from_img("lena_noisy_bn.bmp")

#Definizione del kernel di smoothing 
smooth = np.ones((15,15))

#Smoothing dell'immagine 
Img_Smooth = norm(sg.convolve(img_n,smooth))
save_as_img(Img_Smooth,'lena-smooth.bmp')
img_from_np(Img_Smooth).show()

# Definizione della funzione per la generazione del kernel Gaussiano
def gkern(kernlen=21, nsig=3):
    interval = (2*nsig+1.)/(kernlen)
    x = np.linspace(-nsig-interval/2., nsig+interval/2., kernlen+1)
    kern1d = np.diff(st.norm.cdf(x))
    kernel_raw = np.sqrt(np.outer(kern1d, kern1d))
    kernel = kernel_raw/kernel_raw.sum()
    return kernel

#Calcolo e visualizzazione del kernel Gaussiano
gaussian_kernel = gkern(15)
plt.imshow(gaussian_kernel, interpolation='none')
plt.show()

#Smoothing gaussiano dell'immagine 
Img_G_Smooth = norm(sg.convolve(img_n,gaussian_kernel))
save_as_img(Img_G_Smooth,'lena-g_smooth.bmp')
img_from_np(Img_G_Smooth).show()