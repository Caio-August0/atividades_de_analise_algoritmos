import math


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = []

    def adicionar_aresta(self, origem, destino, peso):
        self.arestas.append((origem, destino, peso))

    def bellman_ford(self, origem):
        distancia = {}
        predecessor = {}

        for vertice in self.vertices:
            distancia[vertice] = math.inf
            predecessor[vertice] = None

        distancia[origem] = 0

        print("Tabela inicial:")
        self.imprimir_tabela(distancia, predecessor)

        # Relaxamento das arestas
        for iteracao in range(1, len(self.vertices)):
            print(f"\nIteração {iteracao}:")

            houve_atualizacao = False

            for u, v, peso in self.arestas:
                if distancia[u] != math.inf and distancia[u] + peso < distancia[v]:
                    valor_antigo = distancia[v]
                    distancia[v] = distancia[u] + peso
                    predecessor[v] = u
                    houve_atualizacao = True

                    print(
                        f"Relaxando {u} -> {v}: "
                        f"{valor_antigo} foi atualizado para {distancia[v]}"
                    )

            self.imprimir_tabela(distancia, predecessor)

            if not houve_atualizacao:
                print("Nenhuma atualização realizada. Algoritmo encerrado antecipadamente.")
                break

        # Detecção de ciclo negativo
        print("\nVerificando ciclo negativo...")

        for u, v, peso in self.arestas:
            if distancia[u] != math.inf and distancia[u] + peso < distancia[v]:
                print("\nCiclo negativo detectado!")
                print(f"A aresta {u} -> {v} ainda pode ser relaxada.")
                print(
                    f"Distância atual de {v}: {distancia[v]} | "
                    f"Nova distância possível: {distancia[u] + peso}"
                )
                return distancia, predecessor, True

        print("\nNenhum ciclo negativo detectado.")
        return distancia, predecessor, False

    def imprimir_tabela(self, distancia, predecessor):
        print("-" * 55)
        print(f"{'Vértice':<10} {'Distância':<15} {'Predecessor':<15}")
        print("-" * 55)

        for vertice in self.vertices:
            dist = distancia[vertice]

            if dist == math.inf:
                dist = "∞"

            pred = predecessor[vertice]

            if pred is None:
                pred = "-"

            print(f"{vertice:<10} {dist:<15} {pred:<15}")

        print("-" * 55)


# Programa principal
vertices = ["A", "B", "C", "D", "E"]

grafo = Grafo(vertices)

grafo.adicionar_aresta("A", "B", 1)
grafo.adicionar_aresta("A", "C", 4)
grafo.adicionar_aresta("B", "C", 2)
grafo.adicionar_aresta("B", "D", 5)
grafo.adicionar_aresta("C", "D", 1)
grafo.adicionar_aresta("C", "E", 3)
grafo.adicionar_aresta("D", "C", -3)
grafo.adicionar_aresta("D", "E", 2)
grafo.adicionar_aresta("E", "D", 1)

origem = "A"

distancias, predecessores, ciclo_negativo = grafo.bellman_ford(origem)

print("\nResultado final:")

if ciclo_negativo:
    print("O grafo possui ciclo negativo alcançável a partir da origem.")
    print("Por isso, não existe menor caminho definitivo para todos os vértices.")
else:
    print("Menores distâncias a partir da origem:")
    for vertice in vertices:
        print(f"{origem} -> {vertice}: {distancias[vertice]}")

