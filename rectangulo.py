from figura_geometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica):
    """Clase que representa un rectángulo. Hereda de FiguraGeometrica."""

    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    def area(self):
        return self._ancho * self._alto

    def perimetro(self):
        return 2 * (self._ancho + self._alto)

    def __str__(self):
        return (
            f"Rectángulo | Ancho: {self._ancho} | Alto: {self._alto} | "
            f"Área: {self.area()} | Perímetro: {self.perimetro()}"
        )