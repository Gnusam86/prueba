import numpy as np
import matplotlib.pyplot as plt

tiempo = np.linspace(0,10,50)

def mru(t,v):
    return [v * x for x in t]

pos_mru = mru(tiempo,2)

plt.plot(tiempo, pos_mru, 'b--o', label='MRU v=2 m/s')
plt.title("Movimiento Rectilíneo Uniforme (MRU)")   
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")  
plt.grid(True)
plt.legend()    
plt.show()