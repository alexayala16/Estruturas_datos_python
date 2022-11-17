# EJERCICIOS DICCIONARIO

# Ejercicios

# Manipulación:

# El primer ejercicio que vamos a realizar referente a los diccionarios sera crear uno y mmostra elementos del mismo. Para accerder a los elementos del diccionario deberas utilizar la clave del elemento. el codigo fuente es el siguiente:

DiasSemanaIngles = {"Lunes" : "Monday", 
                    "Martes" : "Tuesday", 
                    "Miercoles" : "Wednesday",
                     "Jueves" : "Thursday", 
                     "Viernes" : "Friday"}
print(DiasSemanaIngles["Lunes"])
print(DiasSemanaIngles["Miercoles"])
print(DiasSemanaIngles["Viernes"])

DiasSemanaIngles = {"Lunes" : "Monday", "Martes" : "Tuesday", "Miercoles" : "Wednesday", "Jueves" : "Thursday", "Viernes" : "Friday"}
print(DiasSemanaIngles)
DiasSemanaIngles["Sabado"] = "Saturday"
print(DiasSemanaIngles)
DiasSemanaIngles["Domingo"] = "Sunday"
print(DiasSemanaIngles)
DiasSemanaIngles["Lunes"] = "MondayBORRAR"
print(DiasSemanaIngles)
DiasSemanaIngles["Lunes"] = "Lunes"
print(DiasSemanaIngles)

DiasSemanaIngles = {"Lunes" : "Monday", 
                    "Martes" : "Tuesday", 
                    "Miercoles" : "Wednesday", 
                    "Jueves" : "Thursday",
                     "Viernes" : "Friday"}
print("Numero de elementos del diccionario: ", len(DiasSemanaIngles))
print("Numero de elementos del diccionario: ", max(DiasSemanaIngles))
print("Numero de elementos del diccionario: ", min(DiasSemanaIngles))

# Métodos propios: 

# El tipo de datos diccionarios en Python posee una serie de funciones que nos permiten manipular los diccionarios realizado operacionea complejas de forma sencilla complejas de forma sencilla y con una simple instrucción. El formato de uso de la gran mayoria de las funciones es el siguiente:

DiasSemanaIngles = {"Lunes" : "Monday",
                    "Martes" : "Tuesday", 
                    "Miercoles" : "Wednesday", 
                    "Jueves" : "Thursday", 
                    "Viernes" : "Friday"}
print("Diccionario  original: ", DiasSemanaIngles)
diccionariocopia = DiasSemanaIngles.copy()
print("Disccionario copy: ", diccionariocopia)
print("Valor del Lunes (pop): ", DiasSemanaIngles.pop ("Lunes") )