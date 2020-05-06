# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #4 “Suma de enteros”
Instrucciones: otro clásico conocido, donde pedirás al usuario que ingrese 2 números y muestre en pantalla el resultado. 
Si quieres añadir más dificultad puedes utilizar números con punto decimal y especificar el número de decimales después del punto.
Ejemplo: 2.5633 + 5.6883 = 8.25
"""


def main():
	number_one = float(raw_input("Ingrese un numero: "))
	number_two = float(raw_input("Ingrese un numero: "))

	result     = float(number_one + number_two)

	print("{} + {} = {:.2f}".format(number_one, number_two, result))

if __name__ == '__main__':
	main()