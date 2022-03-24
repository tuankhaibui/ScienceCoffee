import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start = -25, stop = 25, num=50)
y = np.linspace(start = -25, stop = 25, num=50)
xv, yv = np.meshgrid(x, x)
z1 = np.sqrt(xv**2 + (25-yv)**2) - np.sqrt(xv**2 + (25+yv)**2)
z2 = np.sqrt((25-xv)**2 + yv**2) - np.sqrt((25+xv)**2 + yv**2)

h = plt.contourf(x, y, z1)
plt.axis('scaled')
plt.xlabel("x axis [cm]")
plt.ylabel("y axis [cm]")
cbar = plt.colorbar()
cbar.set_label('time diff on X-Axis')
plt.savefig("PS_TOF_Xaxis.png")
plt.show()
plt.close()

h = plt.contourf(x, y, z2)
plt.axis('scaled')
plt.xlabel("x axis [cm]")
plt.ylabel("y axis [cm]")
cbar = plt.colorbar()
cbar.set_label('time diff on Y-Axis')
plt.savefig("PS_TOF_Yaxis.png")
plt.show()
plt.close()