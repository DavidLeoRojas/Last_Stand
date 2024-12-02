
import riManage

class CaminataHV():
    def __init__(self):
        self.datos = []
        self.resultado = None
        self.manejoRi = riManage.riManage()

    def obtener_direccion(self, umbral=0.25):
        indato = self.manejoRi.obtenerRandom(100000) # dato de entrada a validacion
        for indato in self.datos:
            if indato <= umbral:
                self.resultado = (-1, 0)  # Izquierda
            elif indato > umbral and indato <= umbral * 2:
                self.resultado = (1, 0)  # Derecha
            elif indato > umbral * 2 and indato <= umbral * 3:
                self.resultado = (0, 1)  # Arriba
            else:
                self.resultado = (0, -1)  # Abajo
        return self.resultado


