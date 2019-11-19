import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt("Datos.dat")
x = np.linspace(-1, 1,30)
t = np.linspace(0, 1,30)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Nx = 30 , Nt")
plt.xlabel("Posicion")
plt.ylabel("Tiempo")
plt.imshow(data, aspect = 0.1)

plt.subplot(1,3,2)
plt.title("Nx = 30 , Nt")
plt.xlabel("Posicion")
plt.ylabel("Psi")





plt.subplot(1,3,3)
plt.title("Nx = 30 , Nt")
plt.xlabel("Tiempo")
plt.ylabel("Psi(x=0)")

plt.savefig("evolve_A.png")
