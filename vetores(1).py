X = float(input())

# Inicialize o vetor com o valor inicial
N = [X]

# Preencha o vetor com 100 valores, onde cada valor é a metade do anterior
for i in range(1, 100):
    N.append(N[i - 1] / 2)

# Exiba os valores no formato solicitado
for i in range(100):
    print(f"N[{i}] = {N[i]:.4f}")