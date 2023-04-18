# Segmentación de listas
# use una segmentación a fin de obtener los elementos que empiezan en 0 y terminan en 2:
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

# Output: ['Mercury', 'Venus']


# Para obtener todos los planetas después de la Tierra, comience en el tercero y vaya hasta el octavo:
planets_after_earth = planets[3:8]
print(planets_after_earth)

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


#Si no coloca el índice de detención en la segmentación, Python asume que quiere ir al final de la lista:
planets_after_earth = planets[3:]
print(planets_after_earth)

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']



# Combinación de listas
# Cree dos listas. Rellene la primera lista con las cuatro lunas de Amaltea y la segunda lista con las cuatro lunas galileanas. Únalas mediante + para crear una lista:
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']



# Ordenación de listas
# Para ordenar una lista, use el método .sort() de la lista. Python ordenará una lista de cadenas en orden alfabético y una lista de números en orden numérico:
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']


# Para ordenar una lista en orden inverso, llame a .sort(reverse=True) en la lista:
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Importante El uso de sort modifica la lista actual.
# Output
# The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']











