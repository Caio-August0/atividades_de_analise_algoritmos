INF = 9999


def transformar_hamiltoniano_para_tsp(vertices, arestas):
    matriz = {}

    for origem in vertices:
        matriz[origem] = {}

        for destino in vertices:
            if origem == destino:
                matriz[origem][destino] = 0
            elif (origem, destino) in arestas or (destino, origem) in arestas:
                matriz[origem][destino] = 1
            else:
                matriz[origem][destino] = INF

    return matriz


def verificar_ciclo_hamiltoniano_com_tsp(vertices, custo_tsp):
    n = len(vertices)

    if custo_tsp == n:
        return True
    else:
        return False


vertices = ["A", "B", "C", "D"]

arestas = {
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "A")
}

matriz_tsp = transformar_hamiltoniano_para_tsp(vertices, arestas)

print("Matriz gerada para o Caixeiro Viajante:")

for origem in vertices:
    for destino in vertices:
        print(f"{origem} -> {destino}: {matriz_tsp[origem][destino]}")
    print()

# Simulação do resultado do software do Caixeiro Viajante
custo_retornado_pelo_tsp = 4

existe_ciclo = verificar_ciclo_hamiltoniano_com_tsp(
    vertices,
    custo_retornado_pelo_tsp
)

if existe_ciclo:
    print("Existe Ciclo Hamiltoniano.")
else:
    print("Não existe Ciclo Hamiltoniano.")