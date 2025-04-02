import sys

class Graph():

    def __init__(self, vertices):
        # inicializa el grafo con el número de vértices
        self.V = vertices
        # crea una matriz de adyacencia llena de ceros
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        # imprime la distancia desde el origen hasta cada vértice
        print("vértice \tdistancia desde el origen")
        for node in range(self.V):
            print(node, "   \t", dist[node])

    # función auxiliar para encontrar el vértice con
    # la distancia mínima, del conjunto de vértices
    # que aún no están en el árbol de caminos más cortos
    def minDistance(self, dist, sptSet):

        # inicializa la distancia mínima para el siguiente nodo
        min = sys.maxsize

        # busca el vértice más cercano que no esté
        # en el árbol de caminos más cortos
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    # función que implementa el algoritmo de dijkstra
    # para encontrar los caminos más cortos desde un origen
    # usando representación de matriz de adyacencia
    def dijkstra(self, src):

        # inicializa todas las distancias como infinito
        dist = [sys.maxsize] * self.V
        # la distancia al origen es 0
        dist[src] = 0
        # sptset (shortest path tree set) guarda los nodos ya procesados
        sptSet = [False] * self.V

        for cout in range(self.V):

            # elige el vértice con la distancia mínima
            # del conjunto de vértices no procesados
            # en la primera iteración, x siempre es el origen
            x = self.minDistance(dist, sptSet)

            # marca el vértice como procesado
            sptSet[x] = True

            # actualiza las distancias de los vértices adyacentes
            # solo si la distancia actual es mayor que la nueva distancia
            # y el vértice no está en el árbol de caminos más cortos
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)