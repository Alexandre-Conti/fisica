#capítulo 8 menezes - introdução ao python

#definição de função

def soma(x,y):
    print(x+y)
soma(10,11)

#outra forma
def soma(x,y):
    return(x+y)
print(soma(2,3))

#retornando se o valor é par ou não
def épar(x):
    return(x%2==0)
print(épar(2))
print(épar(11))