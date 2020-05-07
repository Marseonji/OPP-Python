# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:54:03 2020

@author: Marseonji
"""


import cv2
from matplotlib import pyplot as plt

class ShowImages:
    
    @staticmethod 
    def mostrar_imagen(formato,imagen_mostrar):
        '''Muestra la imagen en pantalla'''
        cv2.imshow("IMAGEN." + formato.lower(), imagen_mostrar) 
        print("*****CERRAR LA IMAGEN PARA CONTINUAR*****")
        cv2.waitKey(0)
       
    @staticmethod 
    def mostrar_imagen_comparar(imagen_orig, imagen_borde):
        '''Muestra 2 imagens en consola que quieras comparar'''
        plt.subplot(121),plt.imshow(imagen_orig,cmap = 'gray')
        plt.title('IMAGEN ORIGINAL'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(imagen_borde,cmap = 'gray')
        plt.title('IMAGEN DE BORDES'), plt.xticks([]), plt.yticks([])
        plt.show()