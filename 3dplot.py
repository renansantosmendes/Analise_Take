from mpl_toolkits.mplot3d import Axes3D  # ajuda do Welton Vaz: https://github.com/weltonvaz
 
import matplotlib.pyplot as plt
import numpy as np

n_angles = 72
n_radii = 4

radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint = True)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())


z = np.sin(-x*(y**2))+np.cos((x**2)*-y)


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, cmap='Oranges', linewidth=0.1)

# ax.scatter(xs, ys, zs, c=c, marker=m)

plt.show()