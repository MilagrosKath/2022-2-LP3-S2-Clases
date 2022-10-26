# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:53:51 2022

@author: oneti
"""

import os
import sys

from gestion_archivos import crear_archivo
from gestion_archivos import eliminar_archivo
from gestion_archivos import leer_archivo
from gestion_archivos import agregar_archivo_contenido

def crear():
    contenido = input("\nIngrese la noticia: ")
    crear_archivo("noticia.txt", contenido)

def eliminar():
    eliminar_archivo("noticia.txt")

def listar():
    leer_archivo("noticia.txt")

def agregar():
    contenido = input("\nIngrese lo que desee agregar: ")
    agregar_archivo_contenido("noticia.txt", contenido)
    
def salir():
    sys.exit()
    
def menu():
    opcion = input(" 1. Crear archivo \n2. Eliminar archivo \n3. Agregar contenido \n4. Mostrar contenido de archivo \n5. Salir \nIngrese su opcion:")  
    if opcion == "1":
        crear()
    elif opcion == "2":
        eliminar()
    elif opcion == "3":
        agregar()
    elif opcion == "4":
        listar()
    elif opcion == "5":
        salir()
        
menu()