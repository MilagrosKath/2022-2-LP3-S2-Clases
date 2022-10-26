# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:04:05 2022

@author: oneti
"""


import financieros
total = 1000.49

print(f"Subtotal:{financieros.obtenerSubtotalconTotal(total): .2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total:{total}")