from flana_math import Vector2
from typing import List


class CuerpoCeleste:
    @staticmethod
    def buscar_por_nombre(cuerpos_celestes: List['CuerpoCeleste'], nombre) -> (None, 'CuerpoCeleste'):
        for cuerpo_celeste in cuerpos_celestes:
            if cuerpo_celeste.nombre.lower() == nombre.lower():
                return cuerpo_celeste

    def __init__(self, g, nombre, posicion, velocidad, masa):
        CuerpoCeleste.G = g
        self.nombre = nombre
        self.posicion = Vector2(*posicion.values())
        self.velocidad = Vector2(*velocidad.values())
        self.masa = masa

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.__class__.__name__}({', '.join(map(str, vars(self).values()))})"

    def angulo_con(self, cuerpo_celeste:'CuerpoCeleste'):
        return self.direccion_a(cuerpo_celeste).rotation_deg()

    def direccion_a(self, other) -> Vector2:
        return self.posicion.direccion_a(other.posicion)

    def distancia_a(self, other) -> float:
        return self.posicion.distancia_a(other.posicion)

    def fuerza_atraccion_con(self, cuerpo_celeste) -> Vector2:
        modulo = cuerpo_celeste.masa * self.masa / self.distancia_a(cuerpo_celeste) ** 2 * self.G
        return self.posicion.direccion_a(cuerpo_celeste.posicion).normalized * modulo


class EsferaCeleste(CuerpoCeleste):
    def __init__(self, g, nombre, posicion, velocidad, masa, radio):
        super().__init__(g, nombre, posicion, velocidad, masa)
        self.radio = radio
