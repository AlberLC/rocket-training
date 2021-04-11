import json
import logging
from typing import List

from enum import Enum
from cuerpos_celestes import CuerpoCeleste
from nave import Nave

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(r'C:\Users\FlanaPC\Documents\Unity\Pruebas\Assets\ScriptsExternos\debug.log')
handler.setLevel(logging.INFO)
logger.addHandler(handler)

estado = 1


def enviar_datos(angulo, potencia):
    print(json.dumps({'angulo': angulo, 'potencia': potencia, 'estado': estado}))


class EstadoNave(Enum):
    DESPEGANDO = 1
    VIAJANDO = 2
    ATERRIZANDO = 3
    ATERRIZADO = 4


class Juego:
    def __init__(self):
        self.datos_nave_anteriores: List[Nave] = []
        self.estado_nave = EstadoNave.DESPEGANDO

    def run(self, nave: Nave, cuerpos_celestes):
        tierra = CuerpoCeleste.buscar_por_nombre(cuerpos_celestes, 'tierra')
        marte = CuerpoCeleste.buscar_por_nombre(cuerpos_celestes, 'marte')

        if nave.fuerza_atraccion_con(tierra).module > 0.2 or not self.datos_nave_anteriores:
            self.estado_nave = EstadoNave.DESPEGANDO
            nave.despegar_de(tierra)
        elif nave.velocidad.module > 1:
            nave.frenar()
        else:
            self.estado_nave = EstadoNave.VIAJANDO
            distancia = nave.distancia_a(marte) - marte.radio
            if self.estado_nave == EstadoNave.VIAJANDO:
                if distancia < 30:
                    self.estado_nave = EstadoNave.ATERRIZANDO
                    enviar_datos(nave.angulo, 1)
                else:
                    nave.ir_a_cuerpo_celeste(marte)
            else:
                if self.estado_nave == EstadoNave.ATERRIZANDO:
                    if distancia < 0.05:
                        self.estado_nave = EstadoNave.ATERRIZADO
                        enviar_datos(nave.angulo, 0)
                    if distancia < 30:
                        nave.aterrizar_en(marte)
                    else:
                        self.estado_nave = EstadoNave.VIAJANDO
                        enviar_datos(nave.angulo, 0)
                else:
                    enviar_datos(nave.angulo, 0)

        # logger.info(self.estado_nave)
        global estado
        estado = float(self.estado_nave.value)
        self.datos_nave_anteriores.append(nave)
        self.datos_nave_anteriores = self.datos_nave_anteriores[-10:]
