import juego
from cuerpos_celestes import CuerpoCeleste


class Nave(CuerpoCeleste):
    def __init__(self, g, nombre, posicion, velocidad, masa, altura, ancho, angulo, combustible):
        super().__init__(g, nombre, posicion, velocidad, masa)
        self.altura = altura
        self.ancho = ancho
        self.angulo = angulo
        self.combustiblew = combustible

    def aterrizar_en(self, cuerpo_celeste: CuerpoCeleste):
        angulo = self.velocidad.inverse.rotation_deg()
        velocidad = self.velocidad.module
        distancia = self.distancia_a(cuerpo_celeste) - cuerpo_celeste.radio

        if self.velocidad.validate_angle_deg_with(self.direccion_a(cuerpo_celeste), 135):
            if distancia > 1:
                potencia = velocidad * 10 / distancia
            else:
                # angulo = cuerpo_celeste.angulo_con(self)
                potencia = velocidad * 12
        else:
            angulo = cuerpo_celeste.angulo_con(self)
            potencia = 0

        potencia = self.__esperar_a_angulo(angulo, potencia)

        juego.enviar_datos(angulo, potencia)

    def frenar(self):
        angulo = self.velocidad.inverse.rotation_deg()
        potencia = 6
        potencia = self.__esperar_a_angulo(angulo, potencia)
        juego.enviar_datos(angulo, potencia)

    # def frenar_orbita(self, cuerpo_celeste: CuerpoCeleste, vel_orbital):
    #     if vel_orbital > 0:
    #         angulo = cuerpo_celeste.angulo_con(self) - 90
    #         potencia = 2
    #     elif vel_orbital < 0:
    #         angulo = cuerpo_celeste.angulo_con(self) + 90
    #         potencia = 2
    #     else:
    #         angulo = self.angulo
    #         potencia = 0
    #
    #     potencia = self.__esperar_a_angulo(angulo, potencia)
    #
    #     juego.enviar_datos(angulo, potencia)

    def velocidad_orbital_con(self, cuerpo_celeste: CuerpoCeleste, ult_ang) -> float:
        return cuerpo_celeste.angulo_con(self) - ult_ang

    def ir_a_cuerpo_celeste(self, cuerpo_celeste: CuerpoCeleste):
        angulo = self.angulo_con(cuerpo_celeste)
        if self.velocidad.module < 1 or self.velocidad.validate_angle_deg_with(self.direccion_a(cuerpo_celeste), 30):
            potencia = 1.5
        else:
            potencia = 1
        # potencia = self.__esperar_a_angulo(angulo, potencia)
        juego.enviar_datos(angulo, potencia)

    def despegar_de(self, cuerpo_celeste: CuerpoCeleste):
        angulo = cuerpo_celeste.angulo_con(self)
        if self.velocidad.module < 1 or self.velocidad.validate_angle_deg_with(self.direccion_a(cuerpo_celeste), 160):
            potencia = 6.5
        else:
            potencia = 1
        potencia = self.__esperar_a_angulo(angulo, potencia)
        juego.enviar_datos(angulo, potencia)

    def __esperar_a_angulo(self, angulo, potencia):
        return potencia if abs(self.angulo - angulo) < 10 else 0
