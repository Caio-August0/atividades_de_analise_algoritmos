import time

class Grafo:
    def __init__(self, vertices):
        self.v = vertices
        self.grafo = []

    # Função para adicionar uma aresta (cidade1, cidade2, custo)
    def adicionar_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    # Função FIND (com Compressão de Caminho)
    def buscar_raiz(self, pai, i):
        if pai[i] == i:
            return i
        pai[i] = self.buscar_raiz(pai, pai[i])
        return pai[i]

    # Função UNION (com União por Rank)
    def unir_redes(self, pai, rank, x, y):
        raiz_x = self.buscar_raiz(pai, x)
        raiz_y = self.buscar_raiz(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    # O Algoritmo de Kruskal Modificado (Árvore Geradora Máxima)
    def executar_kruskal_maximo(self):
        resultado = []
        i = 0 # Índice para arestas ordenadas
        e = 0 # Contagem de arestas na MST final
        custo_total = 0

        # MUDANÇA PRINCIPAL: Ordenar todas as arestas do MAIOR para o MENOR peso
        self.grafo = sorted(self.grafo, key=lambda item: item[2], reverse=True)

        pai = []
        rank = []

        # Criar os nós independentes (cada um é sua própria rede no início)
        for no in range(self.v):
            pai.append(no)
            rank.append(0)

        # Passo 2 e 3: Selecionar e Validar
        # Adicionei i < len(self.grafo) como precaução caso o grafo seja desconexo
        while e < self.v - 1 and i < len(self.grafo):
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.buscar_raiz(pai, u)
            y = self.buscar_raiz(pai, v)

            # Se as raízes (redes) forem diferentes, não forma ciclo. Pode incluir!
            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                custo_total += w
                self.unir_redes(pai, rank, x, y)

        return resultado, custo_total

# --- EXECUÇÃO DO CASO DE TESTE (MAPA DA DINÂMICA) ---
g = Grafo(8)

g.adicionar_aresta(4, 7, 1)
g.adicionar_aresta(5, 6, 2)
g.adicionar_aresta(4, 5, 3)
g.adicionar_aresta(6, 7, 4)
g.adicionar_aresta(0, 1, 5)
g.adicionar_aresta(3, 7, 6)
g.adicionar_aresta(2, 5, 7)
g.adicionar_aresta(2, 6, 8)
g.adicionar_aresta(1, 2, 9)
g.adicionar_aresta(1, 6, 10)
g.adicionar_aresta(1, 5, 11)
g.adicionar_aresta(1, 7, 13)
g.adicionar_aresta(1, 4, 14)
g.adicionar_aresta(0, 4, 15)
g.adicionar_aresta(0, 3, 16)
g.adicionar_aresta(3, 6, 17)
g.adicionar_aresta(0, 7, 18)

inicio = time.perf_counter()

# Chamando a nova função e desempacotando os retornos
arvore_maxima, custo_total_maximo = g.executar_kruskal_maximo()

fim = time.perf_counter()

print("--- Árvore Geradora Máxima (Sem Ciclos) ---")
for u, v, w in arvore_maxima:
    print(f"Aresta: {u} - {v} \t| Custo: {w}")
    
print("-" * 43)
print(f"Custo Total Máximo:\t{custo_total_maximo}")
print(f"Tempo de execução:\t{(fim - inicio):.6f} segundos")