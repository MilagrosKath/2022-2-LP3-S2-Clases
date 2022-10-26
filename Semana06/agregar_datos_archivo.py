# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:20:12 2022

@author: oneti
"""

archivo = open("noticia.txt", "at")
contenido = "\nFuente:RPP"

archivo.write(contenido)

archivo.close()