# importamos la libreria defaultdict para manejar diccionarios con valores por defecto
from collections import defaultdict

# definimos la clase graph para representar el grafo y aplicar el algoritmo de kruskal
class Graph:

    # metodo constructor de la clase, recibe el numero de vertices (v)
    def __init__(self, vertices):
        self.v = vertices  # numero de vertices
        self.graph = []  # lista para almacenar las aristas del grafo

    # metodo para agregar una arista al grafo
    # recibe los nodos u y v, y el peso w de la arista
    def addedge(self, u, v, w):
        self.graph.append([u, v, w])

    # metodo para encontrar el conjunto al que pertenece un nodo
    # utiliza la tecnica de compresion de ruta para optimizar
    def find(self, parent, i):
        if parent[i] == i:  # si el padre de i es i mismo, retorna i
            return i
        return self.find(parent, parent[i])  # recursivamente encuentra la raiz

    # metodo para unir dos conjuntos (union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)  # encuentra la raiz del conjunto de x
        yroot = self.find(parent, y)  # encuentra la raiz del conjunto de y

        # une el arbol de menor rango bajo la raiz del arbol de mayor rango
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            # si los rangos son iguales, elige uno como raiz y aumenta su rango
            parent[yroot] = xroot
            rank[xroot] += 1

    # metodo principal para construir el mst usando el algoritmo de kruskal
    def kruskalmst(self):
        result = []  # lista para almacenar las aristas del mst
        i = 0  # indice para recorrer las aristas ordenadas
        e = 0  # indice para contar las aristas incluidas en el mst

        # paso 1: ordenar todas las aristas en orden no decreciente de su peso
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []  # lista para almacenar los padres de los nodos
        rank = []  # lista para almacenar los rangos de los nodos

        # paso 2: crear v subconjuntos con un solo elemento (cada nodo es su propio padre)
        for node in range(self.v):
            parent.append(node)
            rank.append(0)

        # paso 3: seleccionar v-1 aristas sin formar ciclos
        while e < self.v - 1:
            # obtener la siguiente arista de menor peso
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)  # encontrar la raiz del conjunto de u
            y = self.find(parent, v)  # encontrar la raiz del conjunto de v

            # si las raices son diferentes, no hay ciclo
            if x != y:
                e += 1  # incrementar el contador de aristas del mst
                result.append([u, v, w])  # agregar la arista al mst
                self.union(parent, rank, x, y)  # unir los conjuntos

        # calcular e imprimir el costo total del mst
        minimumcost = 0
        print("aristas en el mst construido:")
        for u, v, weight in result:
            minimumcost += weight
            print(f"{u} -- {v} == {weight}")  # imprimir cada arista del mst
        print("costo total del arbol de expansion minima:", minimumcost)