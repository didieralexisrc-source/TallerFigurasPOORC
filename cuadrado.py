from figura_geometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):
    """Clase que representa un cuadrado. Hereda de FiguraGeometrica.

    Recibe un solo parámetro (lado) y asigna el mismo valor a ancho y alto.
    """

    def __init__(self, lado):
        super().__init__(lado, lado)

    def area(self):
        return self._ancho ** 2

    def perimetro(self):
        return 4 * self._ancho

    def __str__(self):
        return (
            f"Cuadrado | Lado: {self._ancho} | "
            f"Área: {self.area()} | Perímetro: {self.perimetro()}"
        )