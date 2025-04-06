#bisiesto.by
# Este programa calcula si un año ingresado por el usuairio
# es o no es bisiesto, tomando en ucenta que el año bisiesto
# puede ser divisible entre 4, pero no es divisible entre 100 a menos que lo sea en 400

# Mensaje de entrada
print ('Calcular si el año ingresado es Bisiesto')
print()
# Variable donde se guarda el año ingresado
year = int (input('Escribe el año que quieres verificar '))
print()
# condicion if para verificar si es bisiesto o no, muestra el resultado
if year % 4  == 0 or year % 100 != 0 and year == 0:
    print ('El año ingresado si es bisiesto')
else:
    print('El año ingrsado no es bisiesto')