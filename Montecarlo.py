import riManage

class MontecarloClass:
    """
    Clase que implementa un modelo de Montecarlo para simular resultados
    basados en probabilidades definidas.

    Atributos:
    - dict_probs_valores: Diccionario donde las claves son porcentajes (probabilidades)
      y los valores son los resultados asociados.
    - cantidadRi: Cantidad de números aleatorios (RIs) que se generarán. 
      Nota: Al menos un 40% de estos pueden descartarse durante pruebas.
    """

    def __init__(self, dict_probs_valores, cantRi):
        """
        Constructor de la clase.
        Inicializa el diccionario de probabilidades, los porcentajes acumulados,
        y el gestor de números aleatorios.

        :param dict_probs_valores: Diccionario de probabilidades y valores asociados.
        :param cantRi: Cantidad de números aleatorios reservados.
        """
        self.montecarloProbabilidades = dict_probs_valores  # Probabilidades iniciales
        self.porcentajes_acumulados = []  # Lista para los porcentajes acumulados
        self.valores_ord = []  # Diccionario ordenado por probabilidad
        self.cantidadRi = cantRi  # Cantidad de números aleatorios
        self.manejoRi = riManage.riManage()  # Objeto que maneja los números aleatorios

    def calcularEnteroDeRi(self):
        """
        Obtiene un número aleatorio en el rango [0, 100) en forma de entero.
        Usa el gestor de números aleatorios para obtener un valor entre 0 y 1,
        y lo escala al rango deseado.
        """
        return int(100 * self.manejoRi.obtenerRandom(self.cantidadRi))

    def construirMontecarlo(self):
        """
        Construye el modelo Montecarlo.
        - Ordena el diccionario de probabilidades.
        - Calcula los porcentajes acumulados para determinar los rangos.
        - Verifica que la suma de las probabilidades sea 100%.

        :return: True si el modelo es válido, False en caso contrario.
        """
        # Ordenar las probabilidades por clave (porcentajes)
        self.valores_ord = dict(sorted(self.montecarloProbabilidades.items()))

        # Obtener las claves (porcentajes) ordenadas
        porcentajes = list(self.valores_ord.keys())

        # Reiniciar la lista de porcentajes acumulados
        self.porcentajes_acumulados = []

        # Inicializar con 0 y el primer porcentaje
        self.porcentajes_acumulados.append(0)
        self.porcentajes_acumulados.append(porcentajes[0])

        # Calcular los porcentajes acumulados
        for i in range(len(porcentajes) - 1):
            self.porcentajes_acumulados.append(self.porcentajes_acumulados[i+1] + porcentajes[i+1])

        # Validar si la suma total de porcentajes es 100
        if self.porcentajes_acumulados[-1] != 100:
            return False
        else:
            return True

    def cambiarProbabilidades(self, probs):
        """
        Permite cambiar el diccionario de probabilidades y reconstruir el modelo.

        :param probs: Nuevo diccionario de probabilidades.
        :return: Instancia actualizada si es válida, None en caso contrario.
        """
        self.montecarloProbabilidades = probs
        if self.construirMontecarlo():
            return self
        else:
            return None

    def calcularResultado(self):
        """
        Calcula el resultado del "lanzamiento" Montecarlo.
        Determina en qué rango cae el número aleatorio generado.

        :return: Valor asociado al rango en el que cayó el número.
        """
        # Generar un número aleatorio en el rango [0, 100)
        tiro_aleatorio = self.calcularEnteroDeRi()

        # Verificar en qué rango acumulado cae el número
        for i in range(len(self.porcentajes_acumulados) - 1):
            if self.porcentajes_acumulados[i] <= tiro_aleatorio <= self.porcentajes_acumulados[i + 1]:
                return list(self.valores_ord.values())[i]

def run(valores, m):
    """
    Función externa para inicializar y ejecutar un modelo Montecarlo.

    :param valores: Diccionario de probabilidades y valores asociados.
    :param m: Cantidad de números aleatorios reservados.
    :return: Instancia de MontecarloClass si el modelo es válido, None en caso contrario.
    """
    montecarlo = MontecarloClass(valores, m)

    # Construir el modelo y verificar que sea válido
    if montecarlo.construirMontecarlo():
        print("Generando Numeros...")
        
        # Generar números aleatorios suficientes para la simulación
        montecarlo.manejoRi.generarNumerosHastaPasarPruebas(montecarlo.cantidadRi)

        return montecarlo
    else:
        print("Montecarlo mal formulado! - Debe sumar 100 porciento")
        return None

"""
Ejemplo de uso:

valores = {
    60: 1,   # 60% de probabilidad de obtener 1
    20: 2,   # 20% de probabilidad de obtener 2
    15: 3,   # 15% de probabilidad de obtener 3
    5: 6     # 5% de probabilidad de obtener 6
}

# Crear el modelo Montecarlo con 100,000 números aleatorios
mimonte = run(valores, 100000)

if mimonte:
    # Realizar 1,000 simulaciones y mostrar los resultados
    for i in range(1000):
        print(mimonte.calcularResultado())
"""
