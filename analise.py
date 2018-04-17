import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random, math
import re
from scipy import stats
from collections import Counter

def read_solutions(file):
	data = pd.read_csv(file, delimiter=';')
	# return data.values.tolist()
	return data

def get_string_data(data):
	return str(pd.to_datetime(data)).split()[0]

if __name__ == '__main__':
	
	data_messages = read_solutions('DadosBrutosMessages_1.csv')
	data_events = read_solutions('DadosBrutosEventTracks_3.csv')

	# Index(['MessageSequentialID', 'StorageDate', 'FromIdentity', 'ToIdentity', 'Message', 'MessageOriginator'],

	actions = []

	# - Qual a quantidade de mensagens dos usuários? 
	print('Quantidade de usuarios = ' + str(data_messages[data_messages['MessageOriginator'] == 'User'].shape[0]))

	# - Quantos são os usuários únicos do Bot?
	print(data_messages[data_messages['MessageOriginator'] == 'Bot'])

	# - Qual a quantidade de mensagens trafegadas?
	user_messages = data_messages[data_messages['MessageOriginator'] == 'User'].shape[0]
	bot_messages = data_messages[data_messages['MessageOriginator'] == 'Bot'].shape[0]
	total_messages = user_messages + bot_messages
	print('Total de mensagens = ' + str(total_messages))

	# - Apresente, da forma como achar melhor, as interações que os foliões tiveram com o Bot.
	

	# - Quais botões foram os que tiveram maior interação?
	

	# HIPOTESES:
	# - 1 - quais os ids que tiveram maior iteração com o bot
	print(pd.value_counts((data_messages['FromIdentity'])).head(11))

	# - 2 - há diferença no horário mais utilizado de cada dia
	dates = []
	for row in pd.to_datetime(data_messages['StorageDate']):
		dates.append(str(row).split()[0])
	dates = sorted(list(set(dates))) 
	print(dates)
	print(data_messages[data_messages['StorageDate'] == dates[0]])
	# print(str(pd.to_datetime(data_messages['StorageDate'])).split())
	 
	print('teste')

	# data_messages['date'] = data_messages['StorageDate'].to_string().split()[2]
	# data_messages['date'].apply(get_string_data(data_messages['StorageDate']))

	print(data_messages.head(11).boxplot(column="StorageDate",by="FromIdentity"))

	# print(data_messages.columns)
	# print(data_messages['date'].head(30))
	# print(data_messages[data_messages['date'] == dates[0]])
	# print(data_messages[data_messages['StorageDate'].to_datetime()]) 
	# print(dates[0] in str(pd.to_datetime(data_messages['StorageDate'])))

	# print(dates[0] in pd.to_datetime(data_messages['StorageDate']).to_string())

	# print(data_messages[data_messages['StorageDate'] != dates[0]])

	# print(dates[0])
	# print(data_messages['StorageDate'].head(1))
	# print(data_messages['StorageDate'].head(1) == pd.to_datetime(dates[0]))
	 # & (data_messages['FromIdentity'] != 'carnabelo@msging.net')
	# print(pd.value_counts(data_events['Action']))
	# print(data_events.sort_index(by='count', ascending=[False]))
	# print(data_messages.groupby(['FromIdentity']))

	# histogram_example = plt.hist(data_messages['FromIdentity'])
	# plt.show()	