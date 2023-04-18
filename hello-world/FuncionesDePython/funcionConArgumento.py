# Para requerir un argumento, póngalo entre paréntesis:
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"


# Intente llamar a la función distance_from_earth() sin ningún argumento:
# >>> distance_from_earth()
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: distance_from_earth() missing 1 required positional argument: 'destination'


# Use la Luna como entrada para obtener una respuesta:
distance_from_earth("Moon")
# Output: '238,855'

# Dado que hay una condición catch-all, intente usar cualquier otra cadena como destino para comprobar ese comportamiento:
>>> distance_from_earth("Saturn")
'Unable to compute to that destination'



# Varios argumentos necesarios
# Para usar varios argumentos, debe separarlos con una coma. Vamos a crear una función que pueda calcular cuántos días se tardarán en llegar a un destino, dadas la distancia y una velocidad constante:
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

# Ahora use la distancia entre la Tierra y la Luna para calcular cuántos días tardaría en llegar a la Luna con un límite de velocidad común de 120 kilómetros por hora:
>>> days_to_complete(238855, 75)
132.69722222222222



# Funciones como argumentos
# Puede usar el valor de la función days_to_complete() y asignarlo a una variable y, después, pasarlo a round() (una función integrada que redondea al número entero más cercano) para obtener un número entero:
>>> total_days = days_to_complete(238855, 75)
>>> round(total_days)
133


# Pero un patrón útil es pasar funciones a otras funciones en lugar de asignar el valor devuelto:
>>> round(days_to_complete(238855, 75))
133



