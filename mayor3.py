
print('Este programa encuentra el mayor de 3 numeros entero')
print()

# Lee los tres números enteros
a = int(input('Primer numero entero? '))
b = int(input('Segundo numero entero? '))
c = int(input('Tercer numero entero? '))
print()

# Encuentra el mayor de los dos primeros
if a > b:
    mayor = a
else:
  mayor = b

# Encuentra el mayor del mayor anterior y el tercero
if c > mayor:
    mayor = c

# Escribe el mayor de los tres numeros
print(f'El mayor de {a:d}, {b:d} y {c:d}, es {mayor:d}')


