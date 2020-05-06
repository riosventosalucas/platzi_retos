# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #5 “Suma y multiplicación”
Instrucciones: añadiendo un extra al reto anterior ahora el usuario ingresará 3 números, 
sumarás los 2 primeros y el resultado será multiplicado por el tercero. 
Añade las consideraciones del punto decimal del reto anterior.
Ejemplo:
Datos de entrada:2, 3, 4
Resultado:20
"""


def main():
	number_one   = float(raw_input("Ingrese un numero: "))
	number_two   = float(raw_input("Ingrese un numero: "))
	number_three = float(raw_input("Ingrese un numero: "))
	result       = (number_one + number_two) * number_three

	print("({} + {}) * {} = {:.2f}".format(number_one, number_two, number_three, result))

if __name__ == '__main__':
	main()