from PIL import Image
from PIL import ImageFilter

import os

#Inserire la working directory 
os.chdir('/Users/andreanascetti/Desktop/Python_Images')

#Operazioni di base della libreria PIL 

#Apertura dell'immagine
img = Image.open("lena.png")

#Stampa dimensioni in pixel dell'immagine 
print "Dimensione dell'immagine = " , img.size

#Visualizzazione del file immagine
img.show()

#Stampa dei filtri disponibile nel modulo ImageFilter
print dir(ImageFilter)

#Applicazione dei filtri 
img_contour = img.filter(ImageFilter.CONTOUR)
img_contour.show()

img_blur = img.filter(ImageFilter.BLUR)
img_blur.show()

#Salvataggio delle immagini filtrate
img_contour.save("lena_contour.bmp")
img_contour.save("lena_blur.bmp")


