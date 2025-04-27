import math

# Intervalo e erro
a = 2
b = 3
e = 0.01

# Função do problema
def f(x):
    return x**2 - 5

# Teorema de Bolzano
if f(a) * f(b) < 0:
    print("Teorema de Bolzano satisfeito. Há pelo menos uma raiz no intervalo.")
    while (b - a) / 2 > e:  # Critério de parada baseado no intervalo
        xi = (a + b) / 2  # Ponto médio
        if abs(f(xi)) < e:  # Raiz encontrada com tolerância
            print("A raiz aproximada é:", xi)
            break
        else:
            if f(a) * f(xi) < 0:  # Ajuste do intervalo
                b = xi
            else:
                a = xi
    print("A raiz aproximada é:", xi)
else:
    print("Teorema de Bolzano não satisfeito. Não há raiz garantida no intervalo.")