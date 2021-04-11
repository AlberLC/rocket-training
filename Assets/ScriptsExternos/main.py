import json
import traceback

from cuerpos_celestes import EsferaCeleste
from juego import Juego
from nave import Nave

juego = Juego()

n = 0
try:
    while True:
        # with open('datos_recibidos.json') as archivo:
        #     datos = tuple(json.load(archivo).values())
        a=input()
        datos = list(json.loads(a).values())
        g = datos[0]
        nave = Nave(g, *datos[1].values())
        cuerpos_celestes = [EsferaCeleste(g, *d.values()) for d in datos[2]]
        juego.run(nave, cuerpos_celestes)
except Exception as e:
    with open(r'C:\Users\FlanaPC\Documents\Unity\Pruebas\Assets\ScriptsExternos\error.log', 'w') as f:
        f.write(traceback.format_exc())
    print(f'{e} - Línea {e.__traceback__.tb_lineno}')
