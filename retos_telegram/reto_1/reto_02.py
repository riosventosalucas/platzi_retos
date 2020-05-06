# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #2 “Hola… nombre y apellido:”
Instrucciones: Ahora que sabemos incluir nombres, podemos agregar más datos. 
Intentemos con un apellido para tener algo así: ``Hola, [nombre] [apellido]```
"""


def main():
	name    = str(raw_input("Ingrese su nombre y presione ENTER: "))
	surname = str(raw_input("Ingrese su apellido y presione ENTER: "))

	print("Hola, {} {}".format(name, surname))

if __name__ == '__main__':
	main()