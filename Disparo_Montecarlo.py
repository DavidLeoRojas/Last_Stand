import Montecarlo as MC

# probabilities and damage
class DisparoMontecarloClass():
    """
    Clase que simula un disparo con diferentes probabilidades de causar distintos tipos de daño.
    Utiliza una simulación de Montecarlo para determinar el daño basado en las probabilidades
    dadas para cada tipo de impacto (cuerpo, piernas, brazos, cabeza).
    """

    def __init__(self):
        """
        Constructor de la clase. Inicializa las probabilidades de los diferentes tipos de daño.
        Se crea una simulación de Montecarlo para determinar el daño basado en esas probabilidades.
        """
        # Probabilidades de daño según la zona impactada
        self.valores_probabilidad_disparo = {
            60 : 3,  # 60% de probabilidad de hacer 10 de daño - impacto al cuerpo
            20 : 5,  # 20% de probabilidad de hacer 20 de daño - impacto a piernas
            15 : 8,  # 15% de probabilidad de hacer 30 de daño - impacto a brazos
            5 : 16   # 5% de probabilidad de hacer 60 de daño - impacto a cabeza
        }
        
        # Crea una simulación de Montecarlo con las probabilidades y los resultados posibles
        # El número 100000 indica la cantidad de iteraciones de la simulación para mayor precisión
        self.mimonte = MC.run(self.valores_probabilidad_disparo, 100000)

    def obtenerDisparo(self):
        """
        Calcula el resultado del disparo utilizando la simulación de Montecarlo.

        :return: El daño causado por el disparo, basado en la simulación Montecarlo.
        """
        # Si la simulación ha sido correctamente inicializada, calcula el resultado
        if self.mimonte != None: 
            return self.mimonte.calcularResultado()
        else:
            # Si la simulación no está inicializada, retorna 0 (ningún daño)
            return 0

    def cambiar_probabilidades(self, probs):
        """
        Permite cambiar las probabilidades de daño y recalcular la simulación de Montecarlo.

        :param probs: Un diccionario con las nuevas probabilidades y los daños correspondientes.
        """
        # Actualiza las probabilidades de daño
        self.valores_probabilidad_disparo = probs
        
        # Crea una nueva simulación de Montecarlo con las nuevas probabilidades
        self.mimonte = self.mimonte.cambiarProbabilidades(self.valores_probabilidad_disparo)
