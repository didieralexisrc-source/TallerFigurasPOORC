# Taller POO en Python: Figuras Geométricas

## Descripción del ejercicio

Implementación de un sistema de figuras geométricas usando Programación Orientada
a Objetos (POO) en Python. Se aplican los conceptos de:

- **Encapsulamiento** con atributos privados, `@property` y `@setter`.
- **Herencia** desde una clase base hacia clases hijas.
- **Polimorfismo** mediante la sobrescritura de métodos.
- **Validaciones internas** con `ValueError`.
- Estándar **PEP8**.

---

## Estructura del proyecto

```
TallerFigurasPOO/
│── figura_geometrica.py
│── cuadrado.py
│── rectangulo.py
│── main.py
└── README.md
```

---

## Descripción de cada clase

### `FiguraGeometrica` (figura_geometrica.py)
Clase base abstracta que define los atributos `_ancho` y `_alto` con sus
respectivas propiedades y setters. Valida que ambos valores sean mayores que 0.
Define `area()` (ancho × alto), `perimetro()` (sin implementar, `pass`) y
`__str__()`.

### `Cuadrado` (cuadrado.py)
Hereda de `FiguraGeometrica`. Recibe un solo parámetro `lado` y lo asigna
tanto a `ancho` como a `alto`. Sobrescribe `area()` (lado²),
`perimetro()` (4 × lado) y `__str__()`.

### `Rectangulo` (rectangulo.py)
Hereda de `FiguraGeometrica`. Recibe `ancho` y `alto` independientes.
Sobrescribe `area()` (ancho × alto), `perimetro()` (2 × (ancho + alto))
y `__str__()`.

### `main.py`
Programa principal que:
- Crea instancias de `Cuadrado` y `Rectangulo`.
- Muestra área, perímetro e impresión de cada objeto.
- Demuestra la modificación de valores vía setters.
- Demuestra el manejo de errores con valores inválidos.
- Usa `sumar_areas()` y `sumar_perimetros()` para demostrar polimorfismo.

---

## Ejecución

```bash
python main.py
```

---

## Captura de pantalla
![Ejecución parte 1](img/captura1.png)
![Ejecución parte 2](img/captura2.png)