import Montecarlo as MC
import Markov as MK

class PowerUpMarkovClass:
    """
    Clase que gestiona el cálculo de los power-ups usando el modelo de Markov
    y el método de Montecarlo para simular probabilidades de eventos. Cada power-up
    (como munición, vida, doble poder, puntos extra) tiene su propia probabilidad
    de ocurrir y se modela con Montecarlo. El modelo de Markov se utiliza para determinar
    el siguiente estado o tipo de power-up basado en las probabilidades.
    """

    def __init__(self):
        """
        Inicializa las probabilidades de los distintos power-ups y crea las instancias
        necesarias de Montecarlo para simular los eventos, luego usa el modelo de Markov
        para determinar el siguiente estado de los power-ups.
        """

        # Definición de probabilidades para cada tipo de power-up (cada power-up tiene su propio diccionario)
        
        # Probabilidades para obtener Munición
        probsMunicion = {
            39 : 1,  # 39% de probabilidad de obtener munición
            50 : 2,  # 50% de probabilidad de obtener vida
            10 : 3,  # 10% de probabilidad de obtener doble poder
            1  : 4   # 1% de probabilidad de obtener puntos extra
        }
        # Ejecuta la simulación de Montecarlo para "Munición"
        municion = MC.run(probsMunicion, 100000)

        # Probabilidades para obtener Vida
        probsVida = {
            60 : 1,  # 60% de probabilidad de obtener munición
            30 : 2,  # 30% de probabilidad de obtener vida
            9  : 3,  # 9% de probabilidad de obtener doble poder
            1  : 4   # 1% de probabilidad de obtener puntos extra
        }
        # Ejecuta la simulación de Montecarlo para "Vida"
        vida = MC.run(probsVida, 100000)

        # Probabilidades para obtener Doble Poder
        probsdoble_poder = {
            44 : 1,  # 44% de probabilidad de obtener munición
            5  : 2,  # 5% de probabilidad de obtener vida
            1  : 3,  # 1% de probabilidad de obtener doble poder
            50 : 4   # 50% de probabilidad de obtener puntos extra
        }
        # Ejecuta la simulación de Montecarlo para "Doble Poder"
        doble_poder = MC.run(probsdoble_poder, 100000)

        # Probabilidades para obtener Puntos Extra
        probspuntos_extra = {
            80 : 1,  # 80% de probabilidad de obtener munición
            15 : 2,  # 15% de probabilidad de obtener vida
            4  : 3,  # 4% de probabilidad de obtener doble poder
            1  : 4   # 1% de probabilidad de obtener puntos extra
        }
        # Ejecuta la simulación de Montecarlo para "Puntos Extra"
        puntos_extra = MC.run(probspuntos_extra, 100000)

        # Diccionario con los nombres de los estados (representa los diferentes power-ups)
        estados_nombres = {
            1 : "bullet_refill",  # Estado de recarga de munición
            2 : "health",         # Estado de obtener vida
            3 : "double_refill",  # Estado de obtener doble poder
            4 : "extra_points"    # Estado de obtener puntos extra
        }

        # Diccionario que mapea cada estado (número) a su respectiva simulación de Montecarlo
        montecarlosProbs = {
            1 : municion,    # Munición
            2 : vida,        # Vida
            3 : doble_poder, # Doble poder
            4 : puntos_extra # Puntos extra
        }

        # Ejecuta el modelo de Markov utilizando los estados y las simulaciones Montecarlo
        # 'run' crea un objeto Markov con la información de los estados y las probabilidades
        self.markov = MK.run(estados_nombres, montecarlosProbs)

    def obtenerSiguientePoder(self):
        """
        Obtiene el siguiente power-up basado en el modelo de Markov.
        Llama al método de Markov para obtener el siguiente estado
        y retorna el nombre del estado correspondiente.

        :return: Nombre del siguiente power-up.
        """
        # Llama al modelo de Markov para obtener el siguiente estado
        self.markov.obtenerSiguienteEstado()

        # Retorna el nombre del estado actual
        return self.markov.obtenerNombreEstado()

"""
Ejemplo de uso de la clase PowerUpMarkovClass:
Cada vez que se llama la función obtenerSiguientePoder(), se calcula y obtiene el siguiente power-up
en función de las probabilidades simuladas.

# Crear una instancia de la clase
powerUps = PowerUpMarkovClass()

# Realizar 1000 simulaciones para obtener el siguiente power-up
for i in range(1000):
    print(powerUps.obtenerSiguientePoder())
"""
