# Leia o valor de entrada
V = int(input())

# Inicialize o vetor N com 10 posições
N = [0] * 10

# Atribua o valor inicial à primeira posição
N[0] = V

# Preencha o vetor com o dobro do valor anterior
for i in range(1, 10):
    N[i] = N[i - 1] * 2

# Mostre o vetor
for i in range(10):
    print(f"N[{i}] = {N[i]}")