# Almacenamiento de números en listas
#se debe usar el tipo float. Para crear un valor float, escriba el número con la posición decimal y asígnelo a una variable:
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

# El código siguiente crea una lista en la que se muestran las fuerzas de los ocho planetas del sistema solar, en G:
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

# En el ejemplo siguiente, puede averiguar el peso de un autobús de dos pisos en diferentes planetas obteniendo el valor de la lista:
bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg


#Uso de min() y max() con listas
# La función max() devuelve el número más grande y min() devuelve el más pequeño.
# El código siguiente calcula los pesos mínimo y máximo en el sistema solar mediante esas funciones:
bus_weight = 12650 # in kilograms, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

# Output
# On Earth, a double-decker bus weighs 12650 kg
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg









