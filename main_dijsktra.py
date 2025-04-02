from algortimo_dijkstra import Graph

if __name__ == "__main__":
   
    g = Graph(8) # crear un grafo no dirigido de 8 nodos (A-H)
    
    # inicializar la matriz de adyacencia con todas las conexiones
    # los nodos se indexan como A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7
    
    # matriz de adyacencia inicializada con ceros
    g.graph = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    # agregar todas las conexiones del grafo no dirigido:
    # A a C = 5
    g.graph[0][2] = 5
    g.graph[2][0] = 5
    
    # A a B = 3
    g.graph[0][1] = 3
    g.graph[1][0] = 3
    
    # A a H = 10
    g.graph[0][7] = 10
    g.graph[7][0] = 10
    
    # B a C = 5
    g.graph[1][2] = 5
    g.graph[2][1] = 5
    
    # B a E = 6
    g.graph[1][4] = 6
    g.graph[4][1] = 6
    
    # B a G = 6
    g.graph[1][6] = 6
    g.graph[6][1] = 6
    
    # B a H = 9
    g.graph[1][7] = 9
    g.graph[7][1] = 9
    
    # C a F = 7
    g.graph[2][5] = 7
    g.graph[5][2] = 7
    
    # C a E = 4
    g.graph[2][4] = 4
    g.graph[4][2] = 4
    
    # D a H = 2 (tomando el valor más pequeño de los dos proporcionados: 14 y 2)
    g.graph[3][7] = 2
    g.graph[7][3] = 2
    
    # D a G = 8
    g.graph[3][6] = 8
    g.graph[6][3] = 8
    
    # D a B = 6
    g.graph[3][1] = 6
    g.graph[1][3] = 6
    
    # D a E = 12
    g.graph[3][4] = 12
    g.graph[4][3] = 12
    
    # E a G = 9
    g.graph[4][6] = 9
    g.graph[6][4] = 9
    
    # E a F = 1
    g.graph[4][5] = 1
    g.graph[5][4] = 1
    
    # E a H = 4
    g.graph[4][7] = 4
    g.graph[7][4] = 4
    
    # G a H = 15
    g.graph[6][7] = 15
    g.graph[7][6] = 15
    
    # ejecutar el algoritmo de Dijkstra desde el nodo A (índice 0)
    print("Resultados del algoritmo de Dijkstra desde el nodo A:")
    g.dijkstra(0)
    
    # para verificar, también ejecutar desde otros nodos
    print("\nResultados del algoritmo de Dijkstra desde el nodo D:")
    g.dijkstra(3)