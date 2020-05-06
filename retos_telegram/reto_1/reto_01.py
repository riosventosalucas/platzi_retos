# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #1 “Hola Mundo”
Instrucciones: este es un clásico de clásicos, pero haremos un pequeño cambio. 
En lugar de solo imprimir un mensaje en pantalla, pedirás al usuario que digite un nombre y mostrarás en pantalla lo siguiente: 
Hola, [nombre]
"""


def main():
	name = str(raw_input("Ingrese su nombre y presione ENTER: "))

	print("Hola, {}".format(name))

if __name__ == '__main__':
	main()