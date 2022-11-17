# Diccionario

- En este apartado vamos a hablar sobre los tipos de datos diccionarios, que son un conjunto ordenado de elementos cuyos índices no son numéricos sino identificadores. Al igual que las listas y las tuplas, los diccionarios puede contener datos de cualquier tipo. En otras palabras, los diccionarios son colecciones de elementos compuestos por una clave y un valor asociado, con la características de que las claves no pueden repetirse.
- Los diccionarios en Python se delimitan por corchetes "{}", con los elementos separados por comas y la clave separada del valor mediante dos puntos. Veamos un ejemplo de diccionario:
- Ejemplos:
- `{"Clave1": "Valor1", "Clave2": "Valor2","Clave3": "Valor3}`.
- En este caso, esta compuesta por 6 elementos, 3 llaves y 3 elementos. las llaves son: "Clave", "Clave2, Clave3". Y los elementos son: "Valor1", "Valor2, "Valor3".
- Los elementos  y llaves en el diccionario ocupan posiciones concretas, y mediante esa posición que ocupan podemos acceder directamente a los elementos.
- El diccionario de ejemplo está compuesto por tres elementos, en la siguiente tabla te mostramos la relación entre la clave y el valor asociado:

|   Clave  |   Valor  | 
| -------- | -------- |
| "Clave1" | "Valor1" |
|  "Clave2"| "Valor3" |
| "Clave3" | "Valor3" |

- Las claves de los diccionarios pueden ser de diferentes tipos de datos, aunque siempre deberán de ser datos inmutables. Los tipos de datos soportados en Python para ser claves de los diccionarios son: