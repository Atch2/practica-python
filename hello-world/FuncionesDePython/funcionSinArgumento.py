# Para crear una función, use la palabra clave def, seguida de un nombre, paréntesis y, después, del cuerpo con el código de función:
def rocket_parts():
    print("payload, propellant, structure")

# Para usar la función, debe llamarla por su nombre usando paréntesis:
rocket_parts()
'payload, propellant, structure'

# Si necesita usar un valor que devuelve una función, puede asignar la salida de la función a una variable:
output = rocket_parts()
# resultado en consola= payload, propellant, structure
output is None
# resultado en consola= True


# En Python, si una función no devuelve explícitamente un valor, devuelve implícitamenteNone.
# Actualizar la función para devolver la cadena en lugar de imprimirla hace que la variable output tenga un valor distinto:
>>> def rocket_parts():
    ...     return "payload, propellant, structure"
...
>>> output = rocket_parts()
>>> output
'payload, propellant, structure'



# Argumentos opcionales y requeridos
# Un ejemplo de una función integrada que requiere un argumento es any(). Esta función toma un objeto iterable (por ejemplo, una lista) y devuelve True si algún elemento del objeto iterable es True. De lo contrario, devuelve False.
>>> any([True, False, False])
True
>>> any([False, False, False])
False


# Si llama a any() sin ningún argumento, se genera una excepción útil. El mensaje de error explica que necesita al menos un argumento:
>>> any()
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: any() takes exactly one argument (0 given)


# Puede comprobar que algunas funciones permiten el uso de argumentos opcionales mediante otra función integrada denominada str(). Esta función crea una cadena a partir de un argumento. Si no se pasa ningún argumento, devuelve una cadena vacía:
>>> str()
''
>>> str(15)
'15'












