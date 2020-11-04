def rng(lista):
	import random
	escolha = random.choice(lista)
	if escolha == retorna_ultimo_rng():
		escolha = random.choice(lista)
	salvar_rng(escolha)
	return escolha

def mensagem_formatada(titulo='',descricao=''):
	import discord
	em = discord.Embed()
	em.title = titulo
	em.description = descricao
	return em

def cria_audio(texto,lingua='pt-br'):
	from gtts import gTTS
	from io import BytesIO
	import tempfile, os

	byte_stream = BytesIO()
	tts = gTTS('{parametro}'.format(parametro=texto), lang=lingua)
	tts.write_to_fp(byte_stream)
	byte_stream.seek(0)
	
	tempFile, tempPath = tempfile.mkstemp(suffix='.mp3')
	with open(tempPath, mode='wb') as file:
		byte_stream.seek(0)
		file.write(byte_stream.read())
		file.flush()

	os.close(tempFile)
	byte_stream.close()	
	return tempPath

def busca_cotacao():
	import requests
	from datetime import datetime
	try:
		response = requests.get('https://economia.awesomeapi.com.br/json/all/USD')

		dados = response.json()

		data = datetime.strptime(dados['USD']['create_date'], '%Y-%m-%d %H:%M:%S')
		data_convertida = data.strftime('%d/%m/%Y %H:%M:%S')

		return 'Cotação do ' + dados['USD']['name'] + ' é R$ '+ dados['USD']['bid'] + ' Atualizado em: ' + data_convertida
	except Exception as e:
		return 'Erro ao consultar a cotação: ' + str(e)

async def deleta_arquivo(caminho):
	import os
	os.remove(caminho)

def salvar_rng(ultimo_valor):
	import requests

	url = "https://api.jsonbin.io/b/5fa1f89aa03d4a3bab0c7230"
	payload = {"rng": ultimo_valor}
	headers = {
	'Content-Type':'application/json',
	'secret-key': '$2b$10$W1HJIZPyGuvMH26c8DmrSedhgbGtlrAPio4l8.tiCuAUeWchLyKcq',
	'versioning': 'false'
	}

	requests.put(url, json=payload, headers=headers)

def retorna_ultimo_rng():
	import requests

	url = "https://api.jsonbin.io/b/5fa1f89aa03d4a3bab0c7230"
	headers = {
	'Content-Type':'application/json',
	'secret-key': '$2b$10$W1HJIZPyGuvMH26c8DmrSedhgbGtlrAPio4l8.tiCuAUeWchLyKcq',
	}
	response = requests.get(url, headers=headers)
	json_resposta = response.json()
	return json_resposta['rng']