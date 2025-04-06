
import math

# Constantes
COSTO_LAMINA = {0: 60.00, 1: 45.00}  # Costo de la lámina por m2
COSTO_BASE = {'S': 600.00, 'R': 900.00}  # Costo de la base para esférico

# Funciones para cálculo de superficie y volumen

def superficieSiloCilindrico(radio, altura):
    """Calcula la superficie de un silo cilíndrico (2 * pi * r * (r + h))"""
    return 2 * math.pi * radio * (radio + altura)

def superficieSiloEsférico(radio):
    """Calcula la superficie de un silo esférico (4 * pi * r^2)"""
    return 4 * math.pi * radio**2

def volumenSiloCilindrico(radio, altura):
    """Calcula el volumen de un silo cilíndrico (pi * r^2 * h)"""
    return math.pi * radio**2 * altura

def volumenSiloEsférico(radio):
    """Calcula el volumen de un silo esférico (4/3 * pi * r^3)"""
    return (4/3) * math.pi * radio**3

# Funciones para cálculo de costo

def costoSiloCilindrico(radio, calibreLamina):
    """Calcula el costo de un silo cilíndrico"""
    superficie = superficieSiloCilindrico(radio, altura)
    costoLamina = COSTO_LAMINA[calibreLamina]
    return superficie * costoLamina

def costoSiloEsférico(superficie, calibreLamina, tipoBase):
    """Calcula el costo de un silo esférico"""
    costoLamina = COSTO_LAMINA[calibreLamina]
    costoBase = COSTO_BASE[tipoBase]
    return superficie * costoLamina + costoBase

# Este bloque de código solo se ejecuta si este módulo se ejecuta directamente
if __name__ == "__main__":
    # Ejemplo de uso de las funciones
    tipo = input("Introduce el tipo de silo (C para Cilíndrico, E para Esférico): ").strip().upper()
    
    if tipo == "C":
        radio = float(input("Introduce el radio del silo cilíndrico: "))
        altura = float(input("Introduce la altura del silo cilíndrico: "))
        calibre = int(input("Introduce el calibre de la lámina (0 o 1): "))
        
        superficie = superficieSiloCilindrico(radio, altura)
        volumen = volumenSiloCilindrico(radio, altura)
        costo = costoSiloCilindrico(radio, calibre)
        
        print(f"Superficie: {superficie:.2f} m²")
        print(f"Volumen: {volumen:.2f} m³")
        print(f"Costo: ${costo:.2f}")

    elif tipo == "E":
        radio = float(input("Introduce el radio del silo esférico: "))
        calibre = int(input("Introduce el calibre de la lámina (0 o 1): "))
        tipoBase = input("Introduce el tipo de base ('S' para Simple, 'R' para Reforzada): ").strip().upper()
        
        superficie = superficieSiloEsférico(radio)
        volumen = volumenSiloEsférico(radio)
        costo = costoSiloEsférico(superficie, calibre, tipoBase)
        
        print(f"Superficie: {superficie:.2f} m²")
        print(f"Volumen: {volumen:.2f} m³")
        print(f"Costo: ${costo:.2f}")
