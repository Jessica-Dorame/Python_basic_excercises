# pizza.py
#
# Este programa determina el costo de una pizza
# dependiendo de su tamanho y su numero de ingredientes.
# 
# Este programa ilustra el uso de la sentencia if y
# del operador condicional.

print('Este programa determina el costo de una pizza')
print('dependiendo de su tamanho y su numero de ingredientes')
print()

# Lee el tamanho de la pizza
tamanho = input('Tamanho de la pizza: I)ndividual/F)amiliar? ')

# Lee el numero de ingredientes
nIngredientes = int(input('Numero de ingredientes? '))
print()

# Calcula el costo del pizza
if tamanho == 'I' or tamanho == 'i':
    costo = 100.0 if nIngredientes <= 1 else 100.0 + 25.0 * (nIngredientes - 1)
   
    # Escribe el costo del pizza
    print(f'Costo del pizza: {costo:.2f}')
elif tamanho == 'F' or tamanho == 'f':
    costo = 200.0 if nIngredientes <= 1 else 200.0 + 40.0 * (nIngredientes - 1)

    # Escribe el costo de la pizza
    print(f'Costo de la pizza: {costo:.2f}')
else:
    print('Tamanho de pizza desconocido')


