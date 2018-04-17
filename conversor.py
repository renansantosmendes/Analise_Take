import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random, math
import re
import csv
from scipy import stats
from collections import Counter

FILE_NAME = '/home/renansantos/Área de Trabalho/PD/Resultados/Offline/r150n12tw10k4/nsga_pareto_9fo.txt'
file = open(FILE_NAME,'r')
# writer = csv.writer(open("cl_nsga.csv", "wb"))
# writer = csv.writer('cl_nsga.' , 'w')
# np.savetxt('data.csv', (col1_array, col2_array, col3_array), delimiter=',')
for line in file:
	# np.savetxt('cl_nsga.csv', line.split, delimiter = ',')
	# writer.writerows(line.split())
	# print(int(line.split()))
	line_data = []
	for data in line.split():
		line_data.append(float(data))
	print(line_data)