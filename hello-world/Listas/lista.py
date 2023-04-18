#Crear una lista
# Para crear una lista, asigne una secuencia de valores a una variable.
# Cada valor está separado por una coma y están entre corchetes ([]).
# En el ejemplo siguiente se almacena la lista de todos los planetas de la variable planets:

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

#Acceso a elementos de lista por índice
# Los índices comienzan a partir de 0, por lo que en el código siguiente,
# planets[0] es el primer elemento de la lista planets:

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

#Podría cambiar el nombre de Marte en la lista para usar su alias:
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

# Output
# Mars is also known as Red Planet


#Determinación de la longitud de una lista
# Para obtener la longitud de una lista, use la función integrada len().
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Output:
# There are 8 planets in the solar system


#Incorporación de valores a listas
# Para agregar un elemento a una lista, use el método .append(value).
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Output:
# There are actually 9 planets in the solar system.



#Eliminación de valores de listas
# Puede quitar el último elemento de una lista llamando al método .pop() en la variable de lista:
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")


#Uso de índices negativos
# Los índices negativos comienzan al final de la lista y van hacia atrás.
# En el ejemplo siguiente, un índice de -1 devuelve el último elemento de una lista. Un índice de -2 devuelve el penúltimo.

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Output
# The last planet is Neptune
# The penultimate planet is Uranus



#Búsqueda de un valor en una lista
# use el método index de la lista.
# En el ejemplo siguiente se muestra el uso de "Jupiter" como el valor del índice:
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Output
# Jupiter is the 5 planet from the sun




