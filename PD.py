import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random, math
import re
from scipy import stats
from collections import Counter

def read_solutions(file):
	data = pd.read_csv(file, delimiter=',')
	return data.values.tolist()


def dissimilarity(s1,s2):
	# print(s1)
	# print(s2)
	if len(s1) != len(s2):
		print('dimensions error')
		return None
	else:
		total = 0
		for i in range(0,len(s1)):
			total = total + norm_Lp(s1[i],s2[i], 0.1)
		return total

def norm_Lp(x1,x2,p):
	return math.pow(math.fabs(x1 - x2),p)


def pure_diversity(data):
	diversity_matrix = []
	for i in range(0, len(data)):
		line = []
		for j in range(0, len(data)):
			line.append(dissimilarity(data[i],data[j]))
		diversity_matrix.append(line)

	# print(len(diversity_matrix[0]))
	# print(len(data))
	# print(diversity_matrix[1][1])
	sorted_data = []

	for j in range(0, len(diversity_matrix)):
		sorted_data.append(sorted(diversity_matrix[j]))
	# print(sorted_data[1])
	
	PD = []

	for j in range(0, len(sorted_data)):
		PD.append(sorted_data[j][1])
	# print(sum(PD))
	return sum(PD)

def min_size(data1,data2):
	size1 = len(data1)
	size2 = len(data2)
	return min([size1, size2])

if __name__ == '__main__':
	
	pd_cl_nsga = []
	pd_nsga = []
	x = []
	print('r050n12tw10k4')
	# cl_nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Resultados/Online/r050n12tw10k4/nsga_pareto_9fo.csv')
	# nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Resultados/Offline/r050n12tw10k4/nsga_pareto_9fo.csv')
	cl_nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Teste BETH/CL_NSGA-II_5/r050n12tw10k4/nsga_pareto_9fo.csv')
	nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Teste BETH/NSGA-II/r050n12tw10k4/nsga_pareto_9fo.csv')
	
	print('PD(CL-NSGA-II) = ' + str(pure_diversity(cl_nsga[0:min_size(nsga,cl_nsga)])))
	print('PD(NSGA-II) = ' + str(pure_diversity(nsga[0:min_size(nsga,cl_nsga)])))
	pd_cl_nsga.append(pure_diversity(cl_nsga[0:min_size(nsga,cl_nsga)]))
	pd_nsga.append(pure_diversity(nsga[0:min_size(nsga,cl_nsga)]))
	x.append(50)

	

	# print('r100n12tw10k4')
	# cl_nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Resultados/Online/r100n12tw10k4/nsga_pareto_9fo.csv')
	# nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Resultados/Offline/r100n12tw10k4/nsga_pareto_9fo.csv')
	# print('PD(CL-NSGA-II) = ' + str(pure_diversity(cl_nsga[0:min_size(nsga,cl_nsga)])))
	# print('PD(NSGA-II) = ' + str(pure_diversity(nsga[0:min_size(nsga,cl_nsga)])))
	# pd_cl_nsga.append(pure_diversity(cl_nsga[0:min_size(nsga,cl_nsga)]))
	# pd_nsga.append(pure_diversity(nsga[0:min_size(nsga,cl_nsga)]))
	# x.append(100)


	# print('r150n12tw10k4')
	# cl_nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Resultados/Online/r150n12tw10k4/nsga_pareto_9fo.csv')
	
	# print('PD(CL-NSGA-II) = ' + str(pure_diversity(cl_nsga[0:min_size(nsga,cl_nsga)])))
	# nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Resultados/Offline/r150n12tw10k4/nsga_pareto_9fo.csv')
	# print('PD(NSGA-II) = ' + str(pure_diversity(nsga[0:min_size(nsga,cl_nsga)])))
	# pd_cl_nsga.append(pure_diversity(cl_nsga[0:min_size(nsga,cl_nsga)]))
	# pd_nsga.append(pure_diversity(nsga[0:min_size(nsga,cl_nsga)]))
	# x.append(150)
	
	# print('r200n12tw10k4')
	# cl_nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Resultados/Online/r200n12tw10k4/nsga_pareto_9fo.csv')
	# nsga = read_solutions('/home/renansantos/Área de Trabalho/PD/Resultados/Offline/r200n12tw10k4/nsga_pareto_9fo.csv')
	# print('PD(CL-NSGA-II) = ' + str(pure_diversity(cl_nsga[0:min_size(nsga,cl_nsga)])))
	# print('PD(NSGA-II) = ' + str(pure_diversity(nsga[0:min_size(nsga,cl_nsga)])))
	# pd_cl_nsga.append(pure_diversity(cl_nsga[0:min_size(nsga,cl_nsga)]))
	# pd_nsga.append(pure_diversity(nsga[0:min_size(nsga,cl_nsga)]))
	# x.append(200)

	# plt.plot( x, pd_cl_nsga, 'b^')
	# plt.plot( x, pd_cl_nsga, 'k--', color='blue', label="CL-NSGA-II")  # linha tracejada azul

	# plt.plot( x, pd_nsga, 'go') # green bolinha
	# plt.plot( x, pd_nsga, 'k:', color='green', label="NSGA-II") # linha pontilha orange

	# # plt.axis([40, 210, 250,700])

	# plt.grid(True)
	# plt.xlabel("Number of Requests")
	# plt.xticks(x, x)
	# plt.ylabel("PD values")
	# plt.legend(loc='upper right')
	# plt.show()


	# Values
	# committer_line = chart.plot(x1,y1,'r',label='Committer')
	# contribution_line = chart.plot(x1,y2,'b--',label='Contribution')
	# years = list(range(first_year,2017))
	# chart.xticks(years,[str(i) for i in years],rotation=45) # Usa isto para definires as tuas labels

	# # Legend
	# chart.legend()

	# # Show/Save
	# #chart.savefig(images_path + file_name.replace('.txt','-commiter-contribution.eps'), format='eps')
	# chart.show()