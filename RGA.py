import random
import math
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

'''

TÉCNICAS DE INTELIGENCIA ARTIFICIAL

ALGORITMO GENÉTICO BIDIMENSIONAL

DESARROLLADOR: DAMIÁN ELÍ GARCÍA CORTE 201750579

'''

class Cromosoma:
    def __init__(self, n, k):
        self.rv = []
        self.sv = []
        self.cv = []
        self.fitness = 0
        for i in range(k):
            self.rv.append(i+1)
        for j in range(n): #Con este For vamos a llenar el arreglo de genes, es decir, asignarle un color a cada nodo
                self.sv.append(j+1)
                self.cv.append((random.randint(1,k),j+1))

class AlgoritmoGenetico:
    def __init__(self, generaciones, noPoblacion, puntajePerfecto, cr, mr, n, k): #El constructor de esta clase recibe también el crossover rate, mutation rate, # nodos, # colores
        self.poblacion = [] #Este arreglo almacenará los cromosomas de tipo Cromosoma
        self.ruleta = []
        self.DosMejoresCromo = [None, None]
        self.noPoblacion = noPoblacion
        self.generaciones = generaciones
        self.puntajePerfecto = puntajePerfecto #Este valor es el que nos indicará cuando debemos de parar la ejecución del AG
        self.crossoverRate = cr
        self.mutationRate = mr
        self.terminado = False
        self.mejor = None
        self.peor = None
        self.edges = [(1,2),(2,3),(2,7),(2,11),(3,12),(3,4),(3,5),(3,6),(3,7),(5,6),(5,10),(6,7),(7,8),(8,9),(8,10),(9,10),(10,11),(10,12),(11,12)]
        self.n = n
        self.k = k
        self.grafo = nx.Graph()                                     #Creando grafo
        self.grafo.add_edges_from(self.edges)                       #Asignando nodos y aristas al nodo
        self.mapaDeColor = []

    def crearPoblacion(self):
        for i in range(self.noPoblacion): #Con este for vamos a crear la población con opbjetos de la clase Cromosoma
            individuo = Cromosoma(self.n, self.k) #Creando un nuevo cromosoma
            self.poblacion.append(individuo) #Agregamos un nuevo elemento a la población
    
    #La función calcula el fitness de todos los elementos de la población
    def calcularFitness(self):
        for cromosoma in self.poblacion:
            valorFitness = 0
            for edge in self.edges:
                n1, n2 = edge
                color1,nodo1 = cromosoma.cv[n1-1]
                color2,nodo2 = cromosoma.cv[n2-1]
                if(color1 != color2):
                    valorFitness += 1
            cromosoma.fitness = valorFitness/len(self.edges)

    #Esta funcion implementa crossover y mutación
    def operadores(self):
        flag = False
        porcentajeCr = int(((self.crossoverRate*100)*self.noPoblacion)/100)
        porcentajeMr = int(((self.mutationRate*100)*self.noPoblacion)/100)
        for i in range(porcentajeCr):
            while not flag:
                x1 = random.randint(0, (len(self.ruleta)-1))
                x2 = random.randint(0, (len(self.ruleta)-1))
                padre1 = self.ruleta[x1] #Padre 1
                padre2 = self.ruleta[x2] #Padre 2
                if(padre1.cv != padre2.cv):
                    flag = True
            hijo = self.crossover(padre1,padre2)
            self.poblacion[i] = hijo
        for _ in range(porcentajeMr):
            index = random.randint(0, (len(self.poblacion)-1))
            self.mutacion(self.poblacion[index])
        
        self.poblacion[self.noPoblacion-1] = self.DosMejoresCromo[0]
        self.poblacion[self.noPoblacion-2] = self.DosMejoresCromo[1]

        #Seleccionar a los mejores individuos ELISTISTA

    def crossover(self, padre1, padre2):
        puntoCruce = random.randint(1,self.n)
        hijo = Cromosoma(self.n, self.k) 
        for i in range(self.n):
            if( i>puntoCruce ):
                hijo.cv[i] = padre1.cv[i]
            else:
                hijo.cv[i] = padre2.cv[i]
        return hijo

    def mutacion(self, cromosoma):
        posicion = random.randint(0,(self.n-1))  #Generamos aleatoriamente la posición del gen que se va a modificar
        color = random.randint(1,self.k) #Generamos aleatoriamente el color nuevo que vamos a asignar
        cromosoma.cv[posicion] = (color,posicion+1)

    def evaluacion(self):
        maxfitness = 0
        minfitness = 1
        index = 0
        indexMin = 0
        i_aux = 0 #Solo puede tomar dos valores 1 o 0
        for i in range(len(self.poblacion)):
            if(self.poblacion[i].fitness > maxfitness):
                maxfitness = self.poblacion[i].fitness
                index = i
                self.DosMejoresCromo[i_aux] = self.poblacion[i]
                if(i_aux == 1):
                    i_aux = 0
                else:
                    i_aux = 1
            if(self.poblacion[i].fitness < minfitness):
                minfitness = self.poblacion[i].fitness
                indexMin = i
        self.mejor = self.poblacion[index]
        self.peor = self.poblacion[indexMin]
        if(maxfitness == self.puntajePerfecto):
            self.terminado = True
    
    def llegoFin(self):
        return self.terminado

    def seleccion(self):
        for i in range(len(self.poblacion)):
            n = math.floor(self.poblacion[i].fitness * 100)
            for j in range(n):
                self.ruleta.append(self.poblacion[i])

    def pintarGrafo(self):
        i=0
        self.mapaDeColor = []
        for nodo in self.grafo:
            for gen in self.mejor.cv:
                color,n = gen
                if(nodo == n):
                    if(color == 1):
                         self.mapaDeColor.append('Red')
                    if(color == 2):
                         self.mapaDeColor.append('Green')
                    if(color == 3):
                         self.mapaDeColor.append('Blue')
        nx.draw(self.grafo, node_color = self.mapaDeColor, with_labels=True, font_color='white')
        plt.show()
    
    def mostrarPoblacion(self):
        for cromosoma in self.poblacion:
            print(f"Genes (Color, Nodo): {cromosoma.cv}, Fitness: {cromosoma.fitness}")
    
    def iniciarEvolucion(self):
        cont = 1
        self.crearPoblacion()
        while cont <= self.generaciones and not self.llegoFin():
            self.calcularFitness()
            self.evaluacion()
            self.seleccion()
            self.operadores()
            print(f"Generacion: {cont}")
            print(f"Mejor puntaje (Color,Nodo): {self.mejor.cv} Puntaje: {self.mejor.fitness}")
            print(f"Peor puntaje (Color,Nodo): {self.peor.cv} Puntaje: {self.peor.fitness}")
            cont += 1
        print()    
        print("FIN DEL ALGORITMO")
        print(f"Mejor puntaje (Color,Nodo): {self.mejor.cv} Puntaje: {self.mejor.fitness}")
        self.pintarGrafo()

if __name__ == '__main__':
    ag = AlgoritmoGenetico(100, 10, 1, 0.8, 0.1, 12, 3)
    ag.iniciarEvolucion()