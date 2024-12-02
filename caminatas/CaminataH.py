
import riManage

class CaminataH ():
    def __init__(self):
        self.datos = []
        self.resultado = None
        self.manejoRi = riManage.riManage()
        self.manejoRi.generarNumerosHastaPasarPruebas(100000)

    def obtener_direccion(self, umbral=0.5):
        if self.manejoRi.obtenerRandom(100000) <= umbral:
            self.resultado = (-1, 0)  # Izquierda
        else:
            self.resultado = (1, 0)  # derecha
        return self.resultado
    
   
    