from algoritmo_kruskal import Graph

def main():
    # creamos un grafo con 6 nodos (a=0, b=1, c=2, d=3, e=4, f=5)
    g = Graph(6)

    # agregamos las aristas con sus pesos calculados como la suma de los valores de los nodos
    g.addedge(0, 5, 7)  # a-f: 1+6=7
    g.addedge(0, 1, 3)  # a-b: 1+2=3
    g.addedge(0, 2, 4)  # a-c: 1+3=4
    g.addedge(5, 2, 9)  # f-c: 6+3=9
    g.addedge(5, 1, 8)  # f-b: 6+2=8
    g.addedge(1, 4, 7)  # b-e: 2+5=7
    g.addedge(4, 2, 8)  # e-c: 5+3=8
    g.addedge(4, 3, 9)  # e-d: 5+4=9
    g.addedge(2, 3, 7)  # c-d: 3+4=7

    # llamamos al metodo kruskalmst para obtener el arbol de expansion minima
    g.kruskalmst()

if __name__ == "__main__":
    main()