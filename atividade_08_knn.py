from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd


# 1. Carregar o dataset Breast Cancer Wisconsin
dados = load_breast_cancer()

X = dados.data
y = dados.target

# 2. Separar treino e teste na proporção 80/20
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. Normalizar os dados
normalizador = StandardScaler()

X_treino_normalizado = normalizador.fit_transform(X_treino)
X_teste_normalizado = normalizador.transform(X_teste)

# 4. Valores de K e métricas de distância
valores_k = [1, 3, 5]
metricas_distancia = ["euclidean", "manhattan"]

resultados = []

# 5. Treinar e testar os modelos KNN
for k in valores_k:
    for metrica in metricas_distancia:
        modelo = KNeighborsClassifier(
            n_neighbors=k,
            metric=metrica
        )

        modelo.fit(X_treino_normalizado, y_treino)

        previsoes = modelo.predict(X_teste_normalizado)

        acuracia = accuracy_score(y_teste, previsoes)
        precisao = precision_score(y_teste, previsoes)
        recall = recall_score(y_teste, previsoes)
        f1 = f1_score(y_teste, previsoes)
        matriz = confusion_matrix(y_teste, previsoes)

        resultados.append({
            "K": k,
            "Distância": metrica,
            "Acurácia": acuracia,
            "Precisão": precisao,
            "Recall": recall,
            "F1-Score": f1,
            "Matriz de Confusão": matriz
        })


# 6. Exibir os resultados
tabela_resultados = pd.DataFrame(resultados)

print("Resultados dos testes com KNN:\n")

for resultado in resultados:
    print(f"K = {resultado['K']}")
    print(f"Distância = {resultado['Distância']}")
    print(f"Acurácia = {resultado['Acurácia']:.4f}")
    print(f"Precisão = {resultado['Precisão']:.4f}")
    print(f"Recall = {resultado['Recall']:.4f}")
    print(f"F1-Score = {resultado['F1-Score']:.4f}")
    print("Matriz de Confusão:")
    print(resultado["Matriz de Confusão"])
    print("-" * 50)


# 7. Mostrar a melhor combinação com base na acurácia
melhor_resultado = max(resultados, key=lambda x: x["Acurácia"])

print("\nMelhor resultado encontrado:")
print(f"K = {melhor_resultado['K']}")
print(f"Distância = {melhor_resultado['Distância']}")
print(f"Acurácia = {melhor_resultado['Acurácia']:.4f}")