import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random, math
import re
from scipy import stats
from collections import Counter

path = '/home/renansantos/Área de Trabalho/GA Testes/'
file_name = 'pareto_nsgaii.csv'

file = pd.read_csv(path + file_name, delimiter=',')
	# return data.values.tolist()

print(file.values.tolist())	
f1 = []
f2 = []

for line in file.values.tolist():
	f1.append(float(line[0]))
	f2.append(float(line[1]))


plt.style.use('fast')
plt.scatter(f1, f2,color='blue',marker='x',label='NSGA-II (framework)')

plt.xlabel('Objective Function 1')
plt.ylabel('Objective Function 2')


file_name = 'nsgaii_renan_2.csv'

file = open(path + file_name,'r')
file = pd.read_csv(path + file_name, delimiter=',')
f1 = []
f2 = []

for line in file.values.tolist():
	f1.append(float(line[0]))
	f2.append(float(line[1]))

plt.scatter(f1, f2,color='red',marker='^',label='NSGA-II (implemented)')

path = '/home/renansantos/Área de Trabalho/GA Testes/'
file = path + 'MOEAD_R2_2.txt'

def get_data_from_txt(file,index):
	file = open(file)
	f = []
	for line in file:
		f.append(float(line.replace('[','').replace(']','').replace('\n','').replace(',','').split()[index]))
	return f
	
f1 = get_data_from_txt(file, 0)
f2 = get_data_from_txt(file, 1)

plt.scatter(f1, f2,color='green',marker='o',label='MOEAD')
plt.legend(loc='upper right')

# plt.xlim(20000, 70000)
plt.grid(True)
plt.show()