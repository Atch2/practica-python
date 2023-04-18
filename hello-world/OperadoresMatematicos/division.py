# El primer paso consiste en determinar el número de minutos que hay en 1042 segundos.
# Con 60 segundos en un minuto, puede dividir por 60 y obtener una respuesta de 17.3666667.
# El número que le interesa simplemente es 17. Se recomienda redondear hacia abajo, usando
# lo que se conoce como división de múltiplo inferior. Para realizar una división de este tipo
# en Python, debe utilizar //.

# seconds = 1042
# display_minutes = 1042 // 60
# print(display_minutes)
# Output: 17

# El paso siguiente es determinar el número de segundos.
# seconds = 1042
# display_minutes = 1042 // 60
# display_seconds = 1042 % 60
# print(display_minutes)
# print(display_seconds)
# Output:
# 17
# 22


#Orden de las operaciones
# Python respeta el orden de las operaciones en matemáticas.
# El orden de las operaciones determina que las expresiones se deben evaluar en este orden:
# 1.Paréntesis
# 2.Exponentes
# 3.Multiplicación y división
# 4.Suma y resta

result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
print(result_1)
print(result_2)
