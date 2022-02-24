#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
numeroentero=float(input('Introduce el año que quieras combrobar si es bisiesto:'))
def esbisiesto():
    if numeroentero % 4 != 0: #no divisible entre 4
        print("No es bisiesto")
    elif numeroentero % 4 == 0 and numeroentero % 100 != 0: #divisible entre 4 y no entre 100 o 400
        print("Es bisiesto")
    elif numeroentero % 4 == 0 and numeroentero % 100 == 0 and numeroentero % 400 != 0: #divisible entre 4 y 10 y no entre 400
        print("No es bisiesto")
    elif numeroentero % 4 == 0 and numeroentero % 100 == 0 and numeroentero % 400 == 0: #divisible entre 4, 100 y 400
        print("Es bisiesto")

esbisiesto()