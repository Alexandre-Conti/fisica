import matplotlib.pyplot as plt

N=100
a=1664525
c=1013904223
m=429497296
x=1
results=[]

for i in range(N):
    x=(a*x+c)%m
    results.append(x)
plt.plot(results,'o')
plt.show()