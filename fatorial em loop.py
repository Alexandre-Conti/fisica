#calculo do fatorial
N=int(input())
i=0
fat_N=1

for i in range(1,N+1):
    fat_N*=i

print(fat_N)