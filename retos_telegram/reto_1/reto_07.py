# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #7 “Edad futura y pasada”
Instrucciones: pide al usuario que indique su nombre y su edad. 
Como mensaje de salida le indicarás que edad tuvo el año pasado y cuantos años tendrá el siguiente año.
Ejemplo: [nombre] el año pasado tenías X años y el próximo año cumplirás Y años.
"""


def main():
	name      = str(raw_input("Ingrese su nombre y presione ENTER: "))
	years_old = int(raw_input("Ingrese su edad y presione ENTER: "))
	last_year = years_old -1
	next_year = years_old +1
	print("{} el año pasado tenías {} y el próximo año cumplirás {}.".format(name, last_year, next_year))

if __name__ == '__main__':
	main()