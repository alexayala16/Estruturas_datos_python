# EJERCICIOS TUPLAS

# Ejercicios 

# En el siguiente ejercicio vamos a ver cómo definir una tupla y cómo acceder a sus elementos. El código fuente es el siguiente:

tupla = ('Casa', '2',345, 'Perro',99) 

print("Elementos de la tupla: ", tupla)
print("Elemento de la posición 0: ", tupla[0])
print("Elemento de la posición 1: ", tupla[1])
print("Elemento de la posición 2: ", tupla [2])
print("Elemento de la posición 3: ", tupla [3])
print("Elemento de la posición 4: ", tupla[4])

# Método propios

# Función count: cuenta el número de veces que aparece el elemento indicado como parámetro dentro de la tupla.

print("Número de elementos 99: ", tupla.count(99))

tupla = ('Casa', '2', 99, 345, 'Perro', 99)
print ("Elementos de la tupla: ", tupla)
print("Número de elementos 99: ", tupla.count(99))

# Función index: devuelve la posición de la primera ocurrecia de izquierda a derecha en la tupla del elemento pasado como parámetro.

print("Posición que ocupa el elemento Perro: ", tupla.index("Perro"))