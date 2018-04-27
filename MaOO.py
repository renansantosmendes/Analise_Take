import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random, math
import re
from scipy import stats
from collections import Counter

path = '/home/renansantos/NetBeansProjects/MOEA_VRPDRT_Refactoring/AlgorithmsResults/CLNSGAII/WFG1_2/'
file = 'CLNSGAII_CoombinedPareto.txt'

file = open(path + file)
data = []
f1 = []
f2 = []
for line in file:
	f1.append(float(line.replace('[','').replace(']','').replace('\n','').replace(',','').split()[0]))
	f2.append(float(line.replace('[','').replace(']','').replace('\n','').replace(',','').split()[1]))

# print(f1)
# print(f2)

x = np.arange(0.0, 1.0, 0.01)
y = []
for number in x:
	# y.append(1 - math.sqrt(number))
	y.append(1 - number*number)

plt.scatter(f1, f2,color='red',marker='x')
# plt.plot(x,y)
plt.xlabel('Objective Function 1')
plt.ylabel('Objective Function 2')

plt.show()