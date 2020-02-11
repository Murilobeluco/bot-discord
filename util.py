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