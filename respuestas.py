from algoritmo_topologico import Graph

'''Respuesta 1 y 2: Para los algortimos 1 y 2 no se puede aplicar el 
algoritmo topológico ya que el grafo 1 es no dirigido y el grafo 2 tiene ciclos'''

# Respuesta 3: en el grafo 3 sí se puede aplicar el algortimo topológico
def main():
    g = Graph(7)  # 7 nodos: A(0), B(1), M(2), T(3), K(4), G(5), S(6)

    # añadir las aristas según el grafo descrito
    g.addEdge(1, 2)  # B → M
    g.addEdge(1, 3)  # B → T
    g.addEdge(3, 4)  # T → K
    g.addEdge(3, 5)  # T → G
    g.addEdge(5, 6)  # G → S
    g.addEdge(0, 6)  # A → S
    g.addEdge(0, 1)  # A → B

    print("Orden topológico del grafo:")
    top_order = g.topologicalSort()

    # mapear los índices a los nombres originales para mejor legibilidad
    index_to_node = {0: 'A', 1: 'B', 2: 'M', 3: 'T', 4: 'K', 5: 'G', 6: 'S'}
    readable_order = [index_to_node[i] for i in top_order]

    print(readable_order)

if __name__ == "__main__":
    main()