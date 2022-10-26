# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:22:03 2022

@author: oneti
"""

#que pasaria si el ahora el problema
# muestre en formato titulo, para eso hemos utilizado
#una libreria llama camelcase


#importamos la libreria
import camelcase

nombre = "milagros katherine soto obregon"
print(nombre.upper()) #en mayusculas
print(nombre.title()) #en formato titulo

#Creammos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase...")

#Imprimimos el nombre en formato titulo
#utilizamos camelcase
print(cam.hump(nombre))

#Para resolver el problema, creamos otro objeto, incluimos los argumentos
# 'milagros' y 'soto'

cam2 = camelcase.CamelCase('milagros', 'soto')
#esto hara que lo que yo indico no se muestra en formato titulo
print(cam2.hump(nombre))

