from cuadrado import Cuadrado
from rectangulo import Rectangulo


def sumar_areas(figuras: list) -> float:
    """Suma el área de todas las figuras en la lista."""
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras: list) -> float:
    """Suma el perímetro de todas las figuras en la lista."""
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


def main():
    print("=" * 55)
    print("   TALLER POO - FIGURAS GEOMÉTRICAS")
    print("=" * 55)

    # --- Cuadrados ---
    print("\n--- Creación de Cuadrados ---")
    c1 = Cuadrado(5)
    c2 = Cuadrado(3)
    print(c1)
    print(c2)

    print("\n--- Área y Perímetro ---")
    print(f"Cuadrado 1 -> Área: {c1.area()} | Perímetro: {c1.perimetro()}")
    print(f"Cuadrado 2 -> Área: {c2.area()} | Perímetro: {c2.perimetro()}")

    print("\n--- Modificación de valores (setter) ---")
    c1.ancho = 10
    print(f"Cuadrado 1 tras cambiar lado a 10: {c1}")

    # --- Rectángulos ---
    print("\n--- Creación de Rectángulos ---")
    r1 = Rectangulo(4, 7)
    r2 = Rectangulo(6, 2)
    print(r1)
    print(r2)

    print("\n--- Área y Perímetro ---")
    print(f"Rectángulo 1 -> Área: {r1.area()} | Perímetro: {r1.perimetro()}")
    print(f"Rectángulo 2 -> Área: {r2.area()} | Perímetro: {r2.perimetro()}")

    print("\n--- Modificación de valores (setter) ---")
    r1.alto = 12
    print(f"Rectángulo 1 tras cambiar alto a 12: {r1}")

    # --- Polimorfismo con funciones ---
    figuras = [c1, c2, r1, r2]
    print("\n--- Suma de Áreas (polimorfismo) ---")
    print(f"Suma total de áreas: {sumar_areas(figuras)}")

    print("\n--- Suma de Perímetros (polimorfismo) ---")
    print(f"Suma total de perímetros: {sumar_perimetros(figuras)}")

    # --- Demostración de validaciones (ValueError) ---
    print("\n--- Validación de errores ---")

    print("Intentando crear Cuadrado con lado = 0 ...")
    try:
        c_invalido = Cuadrado(0)
    except ValueError as e:
        print(f"  ValueError capturado: {e}")

    print("Intentando crear Cuadrado con lado = -5 ...")
    try:
        c_invalido = Cuadrado(-5)
    except ValueError as e:
        print(f"  ValueError capturado: {e}")

    print("Intentando crear Rectángulo con ancho válido y alto = -1 ...")
    try:
        r_invalido = Rectangulo(4, -1)
    except ValueError as e:
        print(f"  ValueError capturado: {e}")

    print("Intentando asignar ancho = -3 a un rectángulo existente ...")
    try:
        r2.ancho = -3
    except ValueError as e:
        print(f"  ValueError capturado: {e}")

    print("\n" + "=" * 55)
    print("   FIN DEL PROGRAMA")
    print("=" * 55)


if __name__ == "__main__":
    main()