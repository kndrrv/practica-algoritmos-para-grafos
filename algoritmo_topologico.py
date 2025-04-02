from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # diccionario para la lista de adyacencia
        self.V = vertices              # número de vértices

    def addEdge(self, u, v):
        self.graph[u].append(v)        # añadir arista dirigida u → v

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True              # marcar el nodo como visitado

        # recorrer todos los nodos adyacentes
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.topologicalSortUtil(neighbor, visited, stack)

        stack.append(v)  # añadir el nodo al stack (su orden final)

    def topologicalSort(self):
        visited = [False] * self.V     # inicializar todos los nodos como no visitados
        stack = []                     # stack para guardar el orden

        # llamar a la función auxiliar para cada nodo no visitado
        for node in range(self.V):
            if not visited[node]:
                self.topologicalSortUtil(node, visited, stack)

        # el orden topológico es el reverso del stack
        return stack[::-1]

