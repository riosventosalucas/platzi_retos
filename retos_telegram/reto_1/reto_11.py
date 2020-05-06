# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #11 “Cuantas veces un número en otro”
Instrucciones: pide al usuario ingresar un número mayor a 1000 y otro menor a 100. 
Indica de una forma sencilla de entender al usuario cuantas veces cabe el número menor a 100 en el número mayor a 1000
"""


def main():
	more_than_1000 = float(raw_input("Ingrese un numero mayor a 1000 y presione ENTER: "))
	while more_than_1000 <= 1000:
		more_than_1000 = float(raw_input("Ingrese un numero MAYOR a 1000 y presione ENTER: "))

	less_than_100 = float(raw_input("Ingrese un numero menor a 100 y presione ENTER: "))
	while less_than_100 >= 100:
		less_than_100 = float(raw_input("Ingrese un numero MENOR a 100 y presione ENTER: "))

	total = more_than_1000 / less_than_100
	
	print("El numero {} cabe {:.5f} en {}".format(less_than_100, total, more_than_1000))


if __name__ == '__main__':
	main()