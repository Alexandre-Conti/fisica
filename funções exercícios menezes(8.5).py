#função de pesquisa em uma lista

#8.5

def pesquise(lista,valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x #posição que o número está na lista
    return None
L=[10,20,25,30]

print(pesquise(L,27))
print(pesquise(L,25))