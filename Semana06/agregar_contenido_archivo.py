# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:06:30 2022

@author: oneti
"""

#Usare el mismo archivo noticia ya que es diferente 
#al del ejemplo trabajado en clase

archivo = open("noticia.txt","at")

contenido ="\nFuente:Milagros Soto - Estudiante de Untels"
archivo.write(contenido)
archivo.close()