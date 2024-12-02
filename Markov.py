#import riManage
#import Montecarlo as MC

class MarkovClass():
    """
    Clase que representa un proceso de Markov. Utiliza Montecarlo para simular transiciones
    entre estados en función de las probabilidades dadas. Se puede utilizar para gestionar
    secuencias de eventos donde el siguiente evento depende solo del estado actual.
    """

    def __init__(self, dict_nombre_estados, montecarlosProbabilidades):
        """
        Inicializa el modelo de Markov con un conjunto de estados y las probabilidades asociadas
        a cada estado para determinar las transiciones.

        :param dict_nombre_estados: Diccionario que mapea números de estado a sus nombres.
        :param montecarlosProbabilidades: Diccionario que mapea cada estado a una simulación de Montecarlo,
                                          la cual determina las probabilidades de transición.
        """
        self.estado_actual = 1  # El estado inicial se establece como 1 (primer estado)
        self.probs = montecarlosProbabilidades  # Diccionario con las simulaciones de Montecarlo
        self.diccionario_estados = dict_nombre_estados  # Diccionario con los nombres de los estados
        self.montecarloActual = None  # Variable para almacenar el objeto Montecarlo actual utilizado

    def obtenerSiguienteEstado(self):
        """
        Calcula el siguiente estado utilizando el modelo de Montecarlo. El estado actual
        se usa como clave en el diccionario `self.probs` para obtener la simulación de Montecarlo,
        que luego se utiliza para calcular el siguiente estado.

        :return: El número del siguiente estado calculado.
        """
        # Obtiene el Montecarlo correspondiente al estado actual
        self.montecarloActual = self.probs[self.estado_actual]

        # Calcula el resultado usando el Montecarlo
        resultado = self.montecarloActual.calcularResultado()

        # El siguiente estado se convierte en el resultado obtenido del Montecarlo
        self.estado_actual = resultado

        # Retorna el estado calculado
        return resultado

    def obtenerNombreEstado(self):
        """
        Obtiene el nombre del estado actual a partir del diccionario de estados.

        :return: El nombre del estado actual.
        """
        return self.diccionario_estados[self.estado_actual]

"""
El siguiente bloque muestra cómo usar la clase:

# Definir las probabilidades para las simulaciones de Montecarlo

valores = {
    60 : 1,  # 60% de probabilidad de pasar al estado 1
    40 : 2   # 40% de probabilidad de pasar al estado 2
}
# Ejecuta la simulación de Montecarlo para las probabilidades anteriores
mimonte = MC.run(valores, 100000)

valores2 = {
    20 : 2,  # 20% de probabilidad de pasar al estado 2
    80 : 1   # 80% de probabilidad de pasar al estado 1
}
# Ejecuta la simulación de Montecarlo para las probabilidades anteriores
mimonte2 = MC.run(valores2, 100000)

# Define los nombres de los estados
estados_nombres = {
    1 : "Frio",  # Estado 1 es 'Frio'
    2 : "Calor"  # Estado 2 es 'Calor'
}

# Crea un diccionario con los Montecarlo correspondientes a cada estado
montecarlosProbs = {
    1 : mimonte,  # El estado 1 usa mimonte
    2 : mimonte2  # El estado 2 usa mimonte2
}
"""

def run(estados_nombres, montecarlosProbs):
    """
    Función que crea una instancia del proceso de Markov y la retorna.

    :param estados_nombres: Diccionario con los nombres de los estados.
    :param montecarlosProbs: Diccionario con las simulaciones de Montecarlo para cada estado.
    :return: Instancia de la clase MarkovClass.
    """
    markov = MarkovClass(estados_nombres, montecarlosProbs)
    return markov
