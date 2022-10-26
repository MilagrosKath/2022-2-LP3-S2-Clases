# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 08:57:16 2022

@author: oneti
"""

"""
Spyder Editor

This is a temporary script file.
"""

igv = 0.18

def obtenerIGVconSubtotal(subtotal):
    return subtotal*igv

def obtenerTotalconSubtotal(subtotal):
    # subtotal+ igv * subtotal
    # subtotal * (1 + 0.18)
    return subtotal*(1+igv)

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal (total):
    return total - obtenerSubtotalconTotal(total)