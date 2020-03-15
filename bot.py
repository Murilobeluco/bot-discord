#!/usr/bin/python3
from discord.ext import commands
from discord.ext.commands import Bot
import discord
from randomemoji import desenho, random_emoji, turtle_emoji
from util import *
from warcraftlogs import buscarLogs, atualizar_contador
import asyncio
import discord
import ffmpeg
import os
import time
import psutil
import urllib.parse

BOT_PREFIX = ('!')

client = Bot(command_prefix=BOT_PREFIX)
#client.remove_command('help')

def lervariavel():
	import os
	variavel = os.environ['TOKEN']
	
	if not variavel:
		 raise Exception('Configurar variavel de ambinete TOKEN')
	
	return variavel
	
async def tocaraudio(ctx, audio=''):
	if ctx.voice_client is None:
		if not ctx.author.voice is None:
			vc = await ctx.author.voice.channel.connect()
			source = discord.FFmpegPCMAudio(source=audio)
			ctx.voice_client.play(source)
			
			while vc.is_playing():
				await asyncio.sleep(1)
	
			await vc.disconnect()
			# atualizar_contador(BOT_PREFIX + ctx.command.name)
		else:
			await ctx.send('Por favor entre em um canal de áudio para chamar o bot.')
	else:
		await ctx.send('Bot já conectado em uma sala.')
	 
@client.command()
async def sheriff(ctx):
	'retorna um sheriff feito de emoji.'
	mensagem = '{0.author.mention}, este é seu Random Sheriff Emoji: \n {sheriff}'.format(
		ctx.message, sheriff=desenho(random_emoji()))
	await ctx.send(mensagem)

@client.command()
async def qrcode(ctx, arg1):
	e = discord.Embed()
	texto = urllib.parse.quote_plus(arg1)
	e.set_image(url='http://api.qrserver.com/v1/create-qr-code/?color=9EFFC5&bgcolor=000000&data={param}&qzone=3&margin=0&size=450x450&ecc=M'.format(param=texto))
	await ctx.send(embed=e)

@client.command()
async def pedra(ctx):
   'toca um audio randômico chamando o grupo para fazer pedra.'
   await tocaraudio(ctx, rng(['audios/caralhovamosfazerpedra.mp3', 'audios/cadepedra.mp3', 'audios/vamosfazerpedra.mp3']))

@client.command()
async def blizz(ctx):
	'toca um audio randômico que fala verdades sobre a blizzard.'
	await tocaraudio(ctx, rng(['audios/infoblizzard.mp3', 'audios/wowbug.mp3', 'audios/wowbugado.mp3']))

@client.command()
async def bfa(ctx):
	'toca um audio pedindo o que todo mundo deseja de bfa: ..... o seu FIM!'
	await tocaraudio(ctx, 'audios/fimbfa.mp3')

@client.command()
async def maedacarol(ctx):
	'chama a mãe da carol.'
	await tocaraudio(ctx, rng(['audios/obrigacao.mp3', 'audios/maedacarol.mp3']))

@client.command()
async def nerfa(ctx):
	'toca um audio pedindo para nerfar o que é quebrado!'
	await tocaraudio(ctx, 'audios/broken.mp3')

@client.command()
async def amanha(ctx):
	'toca um audio com a famosa frase do Semente quando é perguntado a ele se ele quer fazer ilha'
	await tocaraudio(ctx, 'audios/amanha.mp3')

@client.command()
async def livros(ctx):
	'toca um audio com a fala da boss Bella de lower Karazhan!'
	await tocaraudio(ctx, 'audios/livros.mp3')

@client.command()
async def valkyr(ctx):
	'toca um audio em homenagem a um famoso druida que jogava cliando nas skill!'
	await tocaraudio(ctx, 'audios/mare.mp3')

@client.command()
async def oak(ctx):
	'toca um audio com a fala do boss Oakheart de Darkheart Thicket.'
	await tocaraudio(ctx, 'audios/oak.mp3')

@client.command()
async def xixizinho(ctx):
	'toca um audio com a fala do boss Rokmora da melhor dungeon de legion: Neltharion''s Lair'
	await tocaraudio(ctx, 'audios/xixizinho.mp3')

@client.command()
async def tosco(ctx):
	'toca um audio com a fala da boss Bella de lower Karazhan!'
	await tocaraudio(ctx, 'audios/tosco.mp3')

@client.command()
async def dorime(ctx):
	'toca dorime'
	await tocaraudio(ctx, 'audios/dorime.mp3')
	with open('img/dorime.jpg', 'rb') as fp:
		await ctx.send(file=discord.File(fp, 'dorime.jpg'))

@client.command()
async def tururu(ctx):
	'toca a musica triste do naruto'
	await tocaraudio(ctx, 'audios/tururu.mp3')
	with open('img/naruto.png', 'rb') as fp:
		message = await ctx.send(file=discord.File(fp, 'naruto.png'))
		await message.add_reaction('\N{LOUDLY CRYING FACE}')

@client.command()
async def gaucho(ctx):
	'toca um audio de um gaucho falando verdades sobre armandinho'
	await tocaraudio(ctx, 'audios/gaucho.mp3')

@client.command()
async def saizica(ctx):
	'toca um audio da boss galindra de lower karazhan'
	await tocaraudio(ctx, 'audios/zica.mp3')
	with open('img/titus.gif', 'rb') as fp:
		await ctx.send(file=discord.File(fp, 'titus.gif'))

@client.command(aliases=['essencias', 'essences', 'iongod'])
async def milagre(ctx):
	'posta uma imagem de um milagre'
	await tocaraudio(ctx, 'audios/milagre.mp3')
	with open('img/essence.png', 'rb') as fp:
		await ctx.send('A prova que milagres existem!')
		await ctx.send(file=discord.File(fp, 'essence.png'))

@client.command()
async def choras(ctx, arg1):
	arquivo = cria_audio(arg1[:20])
	await tocaraudio(ctx, arquivo)
	await deleta_arquivo(arquivo)

@client.command()
async def drogas(ctx):
	'toca um audio avisando que chegou drogas'
	await tocaraudio(ctx, 'audios/droga.mp3')

@client.command()
async def heart(ctx):
	'toca um audio em homenagem ao Heart'
	await tocaraudio(ctx, 'audios/heart.mp3')

@client.command()
async def turtle(ctx):
	'toca a musica A Turtle Made It to the Water!'
	await tocaraudio(ctx, 'audios/turtle.mp3')
	await ctx.send(turtle_emoji())

@client.command()
async def ping(ctx):
	'mostra o ping do bot com o servidor do discord'
	before = time.monotonic()
	before_ws = int(round(client.latency * 1000, 1))
	message = await ctx.send("🏓 Pong")
	ping = (time.monotonic() - before) * 1000
	await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

@client.command(aliases=['joinme', 'join', 'botinvite'])
async def invite(ctx):
	'gera um link para convite do bot'
	await ctx.author.send(f"**{ctx.author.name}**, Use essa URL para me convidar para o seu servidor\n<{discord.utils.oauth_url(client.user.id)}>")

@client.command(aliases=['info', 'stats', 'status'])
async def about(ctx):
	'informação sobre o bot'
	process = psutil.Process(os.getpid())
	ramUsage = process.memory_full_info().rss / 1024**2
	avgmembers = round(len(client.users) / len(client.guilds))

	embed = discord.Embed(color=0xbe2f2f, title=f"**__Status do Bot__**")
	embed.set_thumbnail(url=ctx.bot.user.avatar_url)
	embed.add_field(name="📙 Library", value="discord.py - Versão {versao}".format(versao=discord.__version__), inline=True)
	embed.add_field(name="🖥️ Servidores", value=f"{len(ctx.bot.guilds)} (avg: {avgmembers} users/server)", inline=True)
	embed.add_field(name="📜 Comandos", value=len([x.name for x in client.commands]), inline=True)
	embed.add_field(name="💾 RAM", value=f"{ramUsage:.2f} MB", inline=True)

	await ctx.send(content=f"ℹ Informações sobre o Bot: **{ctx.bot.user}**", embed=embed)

@client.event
async def on_command_error(ctx, exception):
	if isinstance(exception, commands.CommandNotFound):
		await ctx.send(embed=mensagem_formatada(titulo='\N{WARNING SIGN}Erro:', descricao=f'Comando: {ctx.message.content} não encontrado.'))
	elif isinstance(exception, commands.MissingRequiredArgument):
		await ctx.send('O comando precisa de um parametro')

@client.event
async def on_ready():
	print('Bot')
	print(client.user.name)
	print(client.user.id)
	print('------')

	activity = discord.Game(name='World of Warcraft')
	await client.change_presence(activity=activity)

async def rodando():
	await client.wait_until_ready()
	channel = client.get_channel(437937862223069185)

	if channel is not None:
		while not client.is_closed():
			nomes = ['Murilobeluco', 'Heartmelody', 'Enocc']

			retorno = ''
			for val in nomes:
				result = buscarLogs(val)
				if len(result) >= 1:
					for itens in result:
						retorno = retorno + '\n' + itens

			if retorno:
				await channel.send(retorno)
				retorno = ''

			await asyncio.sleep(600)

def main():
	#client.bg_task = client.loop.create_task(rodando())
	client.run(lervariavel())

if __name__ == '__main__':
	main()
