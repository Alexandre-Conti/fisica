N = int(input("Digite um número para calcular o fatorial: "))

# Inicializa a variável fatorial em 1
fatorial = 1

if 0 < N < 13:
    for i in range(1, N + 1):
        fatorial *= i  # Multiplica fatorial pelo valor atual de i

    print("Fatorial de", N, "é", fatorial)
else:
    print("Digite um número entre 1 e 12.")