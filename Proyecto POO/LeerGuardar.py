# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:50:49 2020

@author: Marseonji
"""


import cv2


class ImageStorage:
   
    @staticmethod    
    def leer_imagen(dir_img):  # mandar la direccion donde se encuentra la imagen
        if isinstance(dir_img, str):
            try:
                img_color = cv2.imread(dir_img, cv2.IMREAD_COLOR) 
                return img_color
            except:
                print("Error de path")
        else: 
            print("formato no valido")
            return None
    
    @staticmethod
    def guardar_imagen(nombre, formato, imagen_guar):
        cv2.imwrite('images\imagenNew{}.{}'.format(nombre,formato.lower()),imagen_guar)
        print("Se guardo la imagen en la carpeta IMAGES")    
        
      