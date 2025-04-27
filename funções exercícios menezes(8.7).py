#funções recursívas
#8.7 MENEZES

#Defina uma função recursiva que calcule o maior divisor comum
#(M.D.C.) entre dois números a e b, onde a > b.

def mdc(a, b):
    # Caso base: se b é zero, retornamos a como o MDC
    if b == 0:
        return a
    # Caso recursivo: aplicamos a função com os novos valores (b, a % b)
    else:
        return mdc(b, a % b)

# Exemplo de teste
a = 48
b = 18
print(f"O MDC de {a} e {b} é: {mdc(a, b)}")