def fatorial(n):
    i=0
    fat=1
    for i in range(1,n+1):
        fat*=i
    return(fat)
print(fatorial(5))

#outra forma

def fatorial(n):
    fat=1
    i=1
    while i<=n:
        i+=1
        fat*=i
    return(fat)