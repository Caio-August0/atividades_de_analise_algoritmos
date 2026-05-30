class HeapMin:
    def __init__(self):
        self.heap = []

    def adicionar(self, item):
        self.heap.append(item)
        self._subir(len(self.heap) - 1)

    def remover_menor(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        menor = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)

        return menor

    def _subir(self, indice_filho):
        while indice_filho > 0:
            indice_pai = (indice_filho - 1) // 2

            if self.heap[indice_pai][0] <= self.heap[indice_filho][0]:
                break

            self.heap[indice_pai], self.heap[indice_filho] = (
                self.heap[indice_filho],
                self.heap[indice_pai]
            )

            indice_filho = indice_pai

    def _descer(self, indice_pai):
        tamanho = len(self.heap)

        while True:
            indice_menor = indice_pai
            indice_filho_esquerda = 2 * indice_pai + 1
            indice_filho_direita = 2 * indice_pai + 2

            if (
                indice_filho_esquerda < tamanho and
                self.heap[indice_filho_esquerda][0] < self.heap[indice_menor][0]
            ):
                indice_menor = indice_filho_esquerda

            if (
                indice_filho_direita < tamanho and
                self.heap[indice_filho_direita][0] < self.heap[indice_menor][0]
            ):
                indice_menor = indice_filho_direita

            if indice_menor == indice_pai:
                break

            self.heap[indice_pai], self.heap[indice_menor] = (
                self.heap[indice_menor],
                self.heap[indice_pai]
            )

            indice_pai = indice_menor

    def esta_vazio(self):
        return len(self.heap) == 0


def prim(grafo, inicio):
    visitados = set()
    fila = HeapMin()
    arvore_minima = []
    custo_total = 0

    visitados.add(inicio)

    for vizinho, custo in grafo[inicio]:
        fila.adicionar((custo, inicio, vizinho))

    while not fila.esta_vazio() and len(visitados) < len(grafo):
        custo, origem, destino = fila.remover_menor()

        if destino not in visitados:
            visitados.add(destino)
            arvore_minima.append((origem, destino, custo))
            custo_total += custo

            for proximo, novo_custo in grafo[destino]:
                if proximo not in visitados:
                    fila.adicionar((novo_custo, destino, proximo))

    return arvore_minima, custo_total


grafo = {
    "A": [("B", 4), ("C", 4)],
    "B": [("A", 4), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 5), ("E", 6)],
    "D": [("B", 5), ("C", 5), ("E", 3), ("F", 4)],
    "E": [("C", 6), ("D", 3), ("F", 2)],
    "F": [("D", 4), ("E", 2)]
}


rota, custo_total = prim(grafo, "A")

print("Rota dos cabos a serem instalados:")

for origem, destino, custo in rota:
    print(f"{origem} -> {destino}: {custo} km")

print(f"\nQuantidade total mínima de cabos utilizados: {custo_total} km")