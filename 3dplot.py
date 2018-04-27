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


path = '/home/renansantos/Área de Trabalho/GA Testes/'
# file = path + 'MOEAD_R2_2.txt'
file = path + 'moead_3d.txt'

def get_data_from_txt(file,index):
	file = open(file)
	f = []
	for line in file:
		f.append(float(line.replace('[','').replace(']','').replace('\n','').replace(',','').split()[index]))
	return f
	
f1 = get_data_from_txt(file, 0)
f2 = get_data_from_txt(file, 1)
f3 = get_data_from_txt(file, 2)
f = []

for number in f3:
	f.append(number/6000)

f3 = f
print(f1)
print(f2)
print(f3)

# plt.scatter(f2, f1,color='green',marker='o',label='MOEAD')


# ax.plot_trisurf(x, y, z, cmap='Oranges', linewidth=0.1)

# ax.scatter(f1, f2, f3, c=c, marker=m) #,color='green',marker='o',label='MOEAD'
ax.scatter(f1, f2, f3, color='green',marker='o',label='MOEAD')
ax.set_xlabel('Objective Function 1')
ax.set_ylabel('Objective Function 2')
ax.set_zlabel('Objective Function 3')

plt.legend(loc='upper right')

plt.show()