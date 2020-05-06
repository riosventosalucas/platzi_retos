# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #10 “Conversor de millas”
Instrucciones: hay 1.609344 km en una milla (mi). 
Escribe un programa en el que el usuario indique una cantidad de millas y muestre en pantalla el resultado convertido a kilómetros.
"""


def main():
	miles = float(raw_input("Ingrese la cantidad de millas y presione ENTER: "))
	km    = miles * 1.609344

	print("{} millas son {:.5f} kilometros.".format(miles, km))

if __name__ == '__main__':
	main()