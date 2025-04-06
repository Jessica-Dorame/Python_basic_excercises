# comision.py
# programa para calcular la comision a partir de una venta mensual dada por el usuario

# metodo donde estan las condiciones segun la venta mensual, calcula comision
def calcular_comision(venta):
    if venta < 1000:
        comision = 0 
    elif venta >= 1000 and venta <4999:
        comision = round (venta * 0.025, 2 )
    elif venta >= 5000 and venta < 9999:
        comision = round(venta * 0.05, 2 )
    elif venta >= 10000 and venta < 49999:
        comision = round(venta * 0.075, 2 )
    elif venta >= 50000:
        comision = round(venta * 0.1 , 2 )
    return f"Venta mensual; ${venta}, Comision ganada; ${comision}"

# Variable que recibe la venta mensual
venta = input('Ingrese la Venta mensual; ')
# Resultado regresado de la llamada al metodo calcular comision
resultado = calcular_comision(float(venta))
print(resultado)
