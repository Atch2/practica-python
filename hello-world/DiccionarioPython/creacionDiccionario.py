# Python usa llaves ({ }) y dos puntos (:) para indicar un diccionario. Puede crear un diccionario vacío y agregar valores más adelante, o bien rellenarlo en el momento de la creación.
# Ahora se creará un diccionario para almacenar el nombre del planeta Tierra y el número de lunas que tiene:
planet = {
    'name': 'Earth',
    'moons': 1
}


# Lectura de valores de diccionario
# Puede leer valores dentro de un diccionario.
# Los objetos de diccionario tienen un método get que puede usar para acceder a un valor mediante su clave.
# Si quiere imprimir name, puede usar el código siguiente:
print(planet.get('name'))

# Displays Earth


# También puede pasar la clave entre corchetes ([ ])
# planet['name'] is identical to using planet.get('name')
print(planet['name'])

# Displays Earth
# Si una clave no está disponible, get devuelve None y [ ] genera un error KeyError.
wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError




#Modificación de valores de diccionario
# También puede modificar valores dentro de un objeto de diccionario, con el método update.
planet.update({'name': 'Makemake'})

# name is now set to Makemake


# La principal diferencia en la sintaxis es que se usa = (a veces denominado operador de asignación) para proporcionar un nuevo valor. Para volver a escribir el ejemplo anterior y cambiar el nombre, puede usar lo siguiente:
planet['name'] = 'Makemake'

# name is now set to Makemake



# En el ejemplo siguiente se hacen las mismas modificaciones en la variable planet y se actualizan el nombre y las lunas. Tenga en cuenta que al usar update realiza una sola llamada a la función, mientras que el uso de corchetes implica dos llamadas.
# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79


# Adición y eliminación de claves
# No es necesario crear todas las claves al inicializar un diccionario. De hecho, no es necesario crear ninguna. Siempre que quiera crear una clave, asígnela como haría con una existente.
# Imagine que quiere actualizar planet para incluir el período orbital en días:
planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

# Importante
# Los nombres de clave, como todo lo demás en Python, distinguen mayúsculas de minúsculas. Como resultado, 'name' y 'Name' se consideran dos claves independientes en un diccionario de Python.



# Para quitar una clave, use pop. pop devuelve el valor y quita la clave del diccionario.
# Para quitar orbital period, puede usar el código siguiente:
planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }



# Tipos de data complejos
# Puede crear otro diccionario dentro de planet para almacenar esta información:
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }


# Para recuperar valores en un diccionario anidado, debe encadenar corchetes o llamadas a get.
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

# Output: Jupiter polar diameter: 133709


