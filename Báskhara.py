a, b, c = map(float, input().split())

# Cálculo do discriminante (delta)
delta = b ** 2 - 4 * a * c

# Verificação de possibilidade de cálculo
if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    R1 = (-b + (delta ** 0.5)) / (2 * a)
    R2 = (-b - (delta ** 0.5)) / (2 * a)

    # Exibindo R1 e R2 com cinco casas decimais
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")