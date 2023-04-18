#El método .format() usa llaves ({}) como marcadores de posición dentro de una cadena y utiliza la asignación de variables para reemplazar texto.
mass_percentage = "1/6"
# print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
# print("""You are lighter on the {0}, because on the {0} 
#     you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
# print("""You are lighter on the {moon}, because on the {moon} 
#     you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))


#Acerca de las cadenas f-strings
#Las variables se incluyen entre llaves y la cadena debe usar el prefijo f.
# print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")

#Si quiere representar el valor 1/6 como un porcentaje con una posición decimal, puede usar directamente la función round():
# print(round(100/6, 1))

#Con f-strings, no es necesario asignar un valor a una variable de antemano:
# print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")

#La cadena podría aplicar un uso específico de mayúsculas y minúsculas para crear un título:
subject = "interesting facts about the moon"
print(f"{subject.title()}")









