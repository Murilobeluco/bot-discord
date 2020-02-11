import requests
import json_store_client

ENDERECOLOG = 'https://www.warcraftlogs.com/reports/{reportid}'
SITE = 'https://www.warcraftlogs.com:443/v1/reports/user/{usuario}?api_key=4615d3b11c614e608c6f294610f81fef'

jsonstore = json_store_client.Client(
	'https://www.jsonstore.io/8a65b049ddc108a80d6fadafe50b5858a4e591110895fa36dcb2b423114f9727'
)

def converterData(dataepoch):
	import time
	return time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(dataepoch / 1000))

def iniciarlizarDb(nome, chave):
	db = jsonstore.retrieve(nome)
	if not db:
		jsonstore.store(nome, {chave : '0'})
		db = jsonstore.retrieve(nome)

	return db

def texto(dados):
	texto = ':newspaper: Log:{log} \towner:{owner} \tData:{data}'.format(
		log=ENDERECOLOG.format(reportid=dados['id']),
		owner=dados['owner'],
		data=converterData(dados['end']))

	return texto

def atualizar_contador(comando):
	db = iniciarlizarDb(comando, 'vezes')
	
	contador = int(db['vezes']) + 1
	jsonstore.store(comando, {'vezes' : contador})

def buscarLogs(nome):
	url = SITE.format(usuario=nome)
	response = requests.get(url)
	data = []
	data = response.json()

	db = iniciarlizarDb(nome, 'ultimos')

	listadb = []
	listalogs = []

	#print(db['ultimos'])

	for itens in data:
		listadb.append(itens['id'])
		if itens['id'] not in db['ultimos']:
			listalogs.append(texto(itens))

	jsonstore.store(nome, {'ultimos': listadb})
	
	return listalogs