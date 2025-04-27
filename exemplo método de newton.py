#METODO DE NEWTON-RAPHSON

import numpy as np
import matplotlib.pyplot as plt
import math

#definir função
#def f(x):
    #return np.power(x,3) - 9*x + 3

def f(x):
    return x**3-9*x+3

#definir derivada
def df(x):
    return 3*x**2-9
#intervalo
x=np.arange(-5.0, 20.0, 1)

plt.figure()
plt.grid()
plt.plot(x, f(x), 'b-') #linha contínua no gráfico
plt.show()