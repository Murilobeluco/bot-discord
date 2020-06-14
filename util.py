def rng(lista):
	import random
	escolha = random.choice(lista)
	return escolha

def mensagem_formatada(titulo='',descricao=''):
	import discord
	em = discord.Embed()
	em.title = titulo
	em.description = descricao
	return em

def cria_audio(texto):
	from gtts import gTTS
	from io import BytesIO
	import tempfile, os

	byte_stream = BytesIO()
	tts = gTTS('{parametro}'.format(parametro=texto), lang='pt-br')
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

async def deleta_arquivo(caminho):
	import os
	os.remove(caminho)