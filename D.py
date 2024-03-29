import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt("Datos.dat")

plt.figure(figsize=(14,4))

plt.subplot(1,3,1)
s = np.shape(data)
Nx = s[1]
Nt = s[0]
plt.title("Nx = 30 , Nt")
plt.xlabel("Posicion")
plt.ylabel("Tiempo")
plt.imshow(data, extent=[-1,1,1,0], aspect=2.0)
plt.colorbar(label="$\psi$")

plt.subplot(1,3,2)
x = np.linspace(-1, 1,Nx)
dt = 1.0/Nt
for i in range(Nt):
    if i%(Nt//9) == 0:
        plt.plot(x, data[i,:], alpha=(i+1)/Nt, color='black', label="t={:.02f}".format(i*dt))
plt.legend(loc=1)
plt.xlabel("Posicion")
plt.ylabel("$\psi$")

plt.subplot(1,3,3)
t = np.linspace(0, 1,Nt)
plt.plot(t, data[:,Nx//2], alpha=i/Nt, color='black')
plt.xlabel("Tiempo")
plt.ylabel("$\psi$(x=0)")

plt.savefig("evolve_A.png")