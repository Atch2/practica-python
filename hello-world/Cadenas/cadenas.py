# multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
# print (multiline)


# multiline = """Facts about the Moon:
#     There is no atmosphere.
#     There is no sound."""
# print(multiline)


# Métodos de cadena en Python

# print("temperatures and facts about the moon".title())

# heading = "temperatures and facts about the moon"
# print(heading.title())



# División de una cadena
# temperatures = """Daylight: 260 F
#     Nighttime: -280 F"""
# # print(temperatures.split())
# print(temperatures.split('\n'))



# Búsqueda de una cadena
# print("Moon" in "This text will describe facts and challenges with space travel")
# print("Moon" in "This text will describe facts about the Moon")
# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
#     while Mars has -28 Celsius."""
# print(temperatures.find("Moon"))#resultado: -1
# print(temperatures.find("Mars"))#resultado: 68 es la posicion de "Mars0"
# print(temperatures.count("Mars"))#resultado: 1 (el número total de repeticiones de una palabra)
# print(temperatures.count("Moon"))#resultado: 0 (el número total de repeticiones de una palabra)



#Comparación sin distinguir mayúsculas de minúsculas
# print("The Moon And The Earth".lower())
# print("The Moon And The Earth".upper())



#Comprobación del contenido

# temperatures = "Mars Average Temperature: -60 C"
# parts = temperatures.split(':')
# print(parts)#separa la temperatura despues de los dos puntos
# print(parts[-1])#solo imprime la temperatura


#Python tiene métodos que ayudan a comprobar el tipo de cadena:
# mars_temperature = "The highest temperature on Mars is about 30 C"
# for item in mars_temperature.split():
#     if item.isnumeric():
#         print(item)


#En el caso de los números negativos, el guion se agrega como prefijo al número y se puede detectar con el método .startswith()
# print("-60".startswith('-'))


#De forma similar, el método .endswith() ayuda a comprobar el último carácter de una cadena:
# if "30 C".endswith("C"):
#     print("This temperature is in Celsius")


#Puede usar el método .replace() para buscar y reemplazar repeticiones de un carácter o grupo de caracteres:
# print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))


#Como se ha mencionado antes, .lower() es una buena manera de normalizar el texto para realizar una búsqueda sin distinguir mayúsculas de minúsculas. Ahora se comprobará rápidamente si algún texto analiza las temperaturas:
# text = "Temperatures on the Moon can vary wildly."
# print("temperatures" in text)#analiza si esta en Mayuscula
# print("temperatures" in text.lower())#Analiza sin importar si esta en mayuscula o minuscula


#El método .join() necesita un elemento iterable (como una lista de Python) como argumento, por lo que su uso es diferente al de otros métodos de cadena:
# moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
# print('\n'.join(moon_facts))







