# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:08:19 2020

@author: Marseonji
"""
import cv2
import numpy as np
from LeerGuardar import ImageStorage
from Mostar import ShowImages

class Fotografia:
    
    def __init__(self, nombre, fecha_creacion, formato):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.formato = formato
        
    def __str__(self):
        return "Nombre : {} \nFue tomada el : {}" \
            "\nFormato : {}".format(self.nombre, self.fecha_creacion, self.formato)
       
    def volver_gris(self,img_orig):
        img_gris = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)  #volver la imagen en gris con opencv
        return img_gris
    
    def buscar_la_carita(self, imagen_orig, imagen_buscar, imagen_gris):
        '''buscar un objeto en una imagen y ver 
        encontrar si hay mas de uno en la imagen utilizando la coincidencia de
        plantillas de opencv'''
        w, h = imagen_buscar.shape[::-1]  # sacando el tamaño de la imagen
        res = cv2.matchTemplate(imagen_gris,imagen_buscar,cv2.TM_CCOEFF_NORMED)
        limite = 0.8
        loc = np.where( res >= limite)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(imagen_orig, pt, (pt[0] + w, pt[1] + h), (100,45,100), 1)
        return imagen_orig
           
    def detectando_bordes(self,imagen_org):
        bordes = cv2.Canny(imagen_org,100,500)  # usamos CANNY de opencv para obtener los bordes
        return bordes
    

if __name__ == '__main__':
    #*****INSTANCIANDO LOS OBJETOS FOTOGRAFIA*****    
    fotoOrig = Fotografia("Tortu", "05-05-2020", "jpg")
    fotoBuscar = Fotografia("Tortu peque", "06-05-2020", "jpg")
    #*****IMPRIMIENDO LOS OBJETOS*****
    print("*****MOSTRANDO DATOS DE LA PRIMERA FOTOGRAFIA*****")
    print(fotoOrig,"\n")
    print("*****MOSTRANDO DATOS DE LA SEGUNDA FOTOGRAFIA*****")
    print(fotoBuscar,"\n")
    img_original = ImageStorage.leer_imagen("images\imagesM.jpg")
    img_gris = fotoOrig.volver_gris(img_original)
    img_buscar = ImageStorage.leer_imagen_a('images\imagesCh.jpg')
    img_bordes = fotoOrig.detectando_bordes(img_original)
    #*****MOSTRANDO IMAGENES EN CONSOLA*****
    ShowImages.mostrar_imagen_comparar(img_original,img_bordes)
    img_rep = fotoOrig.buscar_la_carita(img_original, img_buscar, img_gris)
    #*****MOSTRANDO LAS IMAGENES EN PANTALLA*****
    ShowImages.mostrar_imagen(fotoBuscar.formato, img_buscar)
    ShowImages.mostrar_imagen(fotoOrig.formato,img_rep)
    ShowImages.mostrar_imagen(fotoOrig.formato,img_gris)
    ShowImages.mostrar_imagen(fotoOrig.formato,img_bordes)
    #*****GUARDANDO LAS IMAGENES*****
    ImageStorage.guardar_imagen("BORDE", fotoOrig.formato, img_bordes) 
    ImageStorage.guardar_imagen("BUSCADO", fotoOrig.formato, img_rep)    
    ImageStorage.guardar_imagen("GRIS", fotoOrig.formato, img_gris)  
    print("EXITO")


    
 

