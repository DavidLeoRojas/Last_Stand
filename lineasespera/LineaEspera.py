import riManage

class LineasEspera():
    def __init__(self):
        self.resultado = None
        self.manejoRi = riManage.riManage()
        #generate the numbers that will be used
        self.manejoRi.generarNumerosHastaPasarPruebas(100000)

    def caminar(self,min,max):
        lista_inicial = self.manejoRi.ObtenerCantidadRi(10000)# numeros decimales -- numbers decimals
        lista_IAT = []# enteros en segundos -- integer in seconds
        lista_IAAT = []
        for i in range(len(lista_inicial)):
            valor = int((min + (max - min)) * lista_inicial[i])# genera numeros enteros uniformes-- generate numbers uniform 
            lista_IAT.append(valor)
         
        lista_IAAT.append(lista_IAT[0]) #primer valor de lista IAAT firts value of list IAAT
        #Accumulate the numbers of the list IAT in the list IAAT
        for i in range(len(lista_IAT) - 1):
            lista_IAAT.append(lista_IAAT[i] + lista_IAT[i + 1])
              
        return lista_IAAT
    

        

   
    