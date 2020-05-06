# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Reto:
"""
Reto #3 “Mensaje multilínea”
Instrucciones: seguro has visto que en Platzi hay más de 600 cursos 
¿puedes mostrar a que categorías corresponden en una sola línea de código?
Debe mostrarse así:
Platzi cuenta con cursos de:
[categoría1]
[categoría2]
[categoría3]
[categoría4]
[categoría5]
[categoría6]
"""


def main():
	print("Platzi cuenta con cursos de: \n[{}]\n[{}]\n[{}]\n[{}]\n[{}]\n[{}]".format("DESARROLLO E INGENIERIA", "DISENIO Y UX", "MARKETING", "NEGOCIOS Y ENPRENDIMIENTOS", "PRODUCCION AUDIOVISUAL", "CRECIMIENTO PROFESIONAL"))


if __name__ == '__main__':
	main()