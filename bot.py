#!/usr/bin/python3
from discord.ext import commands
from discord.ext.commands import Bot
import discord
from randomemoji import desenho, random_emoji, rng
from warcraftlogs import buscarLogs
import asyncio
import discord
import ffmpeg
import os

BOT_PREFIX = ('?', '!')

client = Bot(command_prefix=BOT_PREFIX)
#client.remove_command('help')

def lervariavel():
	import os
	variavel = os.environ['TOKEN']
	
	if not variavel:
		 raise Exception('Configurar variavel de ambinete TOKEN')
	
	return variavel

def mensagem_formatada(titulo='',descricao=''):
	em = discord.Embed()
	em.title = titulo
	em.description = descricao
	return em
		
async def tocaraudio(ctx, audio=''):
	if ctx.voice_client is None:
		if not ctx.author.voice is None:
			vc = await ctx.author.voice.channel.connect()
			source = discord.FFmpegPCMAudio(source=audio)
			ctx.voice_client.play(source)
	
			while vc.is_playing():
				await asyncio.sleep(1)
	
			await vc.disconnect()
		else:
			await ctx.send('Por favor entre em um canal de áudio para chamar o bot.')
	else:
		await ctx.send('Bot já conectado em uma sala.')
	 
@client.command(pass_context=True)
async def sheriff(ctx):
	'retorna um sheriff feito de emoji.'
	mensagem = '{0.author.mention}, este é seu Random Sheriff Emoji: \n {sheriff}'.format(
		ctx.message, sheriff=desenho(random_emoji()))
	await ctx.send(mensagem)

@client.command(pass_context=True)
async def pedra(ctx):
   'toca um audio randômico chamando o grupo para fazer pedra.'
   await tocaraudio(ctx, rng(['audios/caralhovamosfazerpedra.mp3', 'audios/cadepedra.mp3', 'audios/vamosfazerpedra.mp3']))

@client.command(pass_context=True)
async def blizz(ctx):
	'toca um audio randômico que fala verdades sobre a blizzard.'
	await tocaraudio(ctx, rng(['audios/infoblizzard.mp3', 'audios/wowbug.mp3', 'audios/wowbugado.mp3']))

@client.command(pass_context=True)
async def bfa(ctx):
	'toca um audio pedindo o que todo mundo deseja de bfa: ..... o seu FIM!'
	await tocaraudio(ctx, 'audios/fimbfa.mp3')

@client.command(pass_context=True)
async def maedacarol(ctx):
	'chama a mãe da carol.'
	await tocaraudio(ctx, rng(['audios/obrigacao.mp3', 'audios/maedacarol.mp3']))

@client.command(pass_context=True)
async def calma(ctx):
	'toca um audio para acalmar o Itália'
	await tocaraudio(ctx, 'audios/calma.mp3')

@client.command(pass_context=True)
async def nerfa(ctx):
	'toca um audio pedindo para nerfar o que é quebrado!'
	await tocaraudio(ctx, 'audios/broken.mp3')

@client.command(pass_context=True)
async def amanha(ctx):
	'toca um audio com a famosa frase do Semente quando é perguntado a ele se ele quer fazer ilha'
	await tocaraudio(ctx, 'audios/amanha.mp3')

@client.command(pass_context=True)
async def livros(ctx):
	'toca um audio com a fala da boss Bella de lower Karazhan!'
	await tocaraudio(ctx, 'audios/livros.mp3')

@client.command(pass_context=True)
async def valkyr(ctx):
	'toca um audio em homenagem a um famoso druida que jogava cliando nas skill!'
	await tocaraudio(ctx, 'audios/mare.mp3')

@client.command(pass_context=True)
async def oak(ctx):
	'toca um audio com a fala do boss Oakheart de Darkheart Thicket.'
	await tocaraudio(ctx, 'audios/oak.mp3')

@client.command(pass_context=True)
async def xixizinho(ctx):
	'toca um audio com a fala do boss Rokmora da melhor dungeon de legion: Neltharion''s Lair'
	await tocaraudio(ctx, 'audios/xixizinho.mp3')

@client.command(pass_context=True)
async def tosco(ctx):
	'toca um audio com a fala da boss Bella de lower Karazhan!'
	await tocaraudio(ctx, 'audios/tosco.mp3')

@client.command(pass_context=True)
async def dorime(ctx):
	'toca dorime'
	await tocaraudio(ctx, 'audios/dorime.mp3')
	with open('img/naruto.png', 'rb') as fp:
		await ctx.send(file=discord.File(fp, 'dorime.png'))

@client.command(pass_context=True)
async def tururu(ctx):
	'toca a musica triste do naruto'
	await tocaraudio(ctx, 'audios/tururu.mp3')
	with open('img/naruto.png', 'rb') as fp:
		message = await ctx.send(file=discord.File(fp, 'naruto.png'))
		await message.add_reaction('\N{LOUDLY CRYING FACE}')

@client.command(pass_context=True)
async def ping(ctx):
	'mostra o ping do bot com o servidor do discord'
	await ctx.send(embed=mensagem_formatada(titulo='Ping:', descricao=f'{client.ws.latency * 1000:.2f} ms'))

@client.event
async def on_command_error(ctx, exception):
	if isinstance(exception, commands.CommandNotFound):
		await ctx.send(embed=mensagem_formatada(titulo='\N{WARNING SIGN}Erro:', descricao=f'Comando: {ctx.message.content} não encontrado.'))
	else:
		await ctx.send(exception)

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
	client.bg_task = client.loop.create_task(rodando())
	client.run(lervariavel())

if __name__ == '__main__':
	main()
