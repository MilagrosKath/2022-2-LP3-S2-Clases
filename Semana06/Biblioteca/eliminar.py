# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:37:33 2022

@author: Danee Jhajaira
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()
consulta = """ DELETE FROM EDITORIAL
                WHERE
                    IDEDITORIAL=5
        """
        
cursor=conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()
