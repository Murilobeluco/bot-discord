#!/usr/bin/python3
from discord.ext import commands
from discord.ext.commands import Bot
import discord
from randomemoji import desenho, random_emoji, quantos_dias, audio_random_pedra, audio_random_blizz
from warcraftlogs import buscarLogs
import asyncio
import discord
import ffmpeg

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

if not discord.opus.is_loaded():
	discord.opus.load_opus("opus")

def lervariavel():
	import os
	variavel = os.environ["TOKEN"]
	
	if not variavel:
		 raise Exception("Configurar variavel de ambinete TOKEN")
		 exit()
	
	return variavel
   
async def tocaraudio(ctx, audio=""):
	if ctx.voice_client is None:
		if not ctx.author.voice is None:
			vc = await ctx.author.voice.channel.connect()
			source = discord.FFmpegPCMAudio(source=audio)
			ctx.voice_client.play(source)
	
			while vc.is_playing():
				await asyncio.sleep(1)
	
			await vc.disconnect()
		else:
			await ctx.send("Por favor entre em um canal de áudio para chamar o bot.")
	else:
		await ctx.send("Bot já conectado em uma sala.")
	 
@client.command(pass_context=True)
async def sheriff(ctx):
	mensagem = "{0.author.mention}, este é seu Random Sheriff Emoji: \n {sheriff}".format(
		ctx.message, sheriff=desenho(random_emoji()))
	await ctx.send(mensagem)

@client.command(pass_context=True)
async def dias(ctx):
	mensagem = quantos_dias()
	await ctx.send(mensagem)

@client.command(pass_context=True)
async def pedra(ctx):
   await tocaraudio(ctx, audio_random_pedra())

@client.command(pass_context=True)
async def blizz(ctx):
	await tocaraudio(ctx, audio_random_blizz())

@client.command(pass_context=True)
async def bfa(ctx):
	await tocaraudio(ctx, "fimbfa.mp3")

@client.command(pass_context=True)
async def maedacarol(ctx):
	await tocaraudio(ctx, "obrigacao.mp3")

@client.command(pass_context=True)
async def calma(ctx):
	await tocaraudio(ctx, "calma.mp3")

@client.command(pass_context=True)
async def nerfa(ctx):
	await tocaraudio(ctx, "broken.mp3")

@client.command(pass_context=True)
async def amanha(ctx):
	await tocaraudio(ctx, "amanha.mp3")

@client.command(pass_context=True)
async def ping(ctx):
	em = discord.Embed()
	em.title ='Ping:'
	em.description = f'{client.ws.latency * 1000:.2f} ms'
	await ctx.send(embed=em)

@client.event
async def on_command_error(ctx, exception):
	if isinstance(exception, commands.CommandNotFound):
		em = discord.Embed()
		em.title ='\N{WARNING SIGN}Erro:'
		em.description = f'Comando: {ctx.message.content} não encontrado.'
		await ctx.send(embed=em)

@client.event
async def on_ready():
	print("Bot")
	print(client.user.name)
	print(client.user.id)
	print("------")

	activity = discord.Game(name="World of Warcraft")
	await client.change_presence(activity=activity)

async def rodando():
	await client.wait_until_ready()
	channel = client.get_channel(437937862223069185)

	while not client.is_closed():
		nomes = ["Murilobeluco", "Heartmelody", "Enocc"]

		retorno = ""
		for val in nomes:
			result = buscarLogs(val)
			if len(result) >= 1:
				for itens in result:
					retorno = retorno + "\n" + itens

		if retorno:
			await channel.send(retorno)
			retorno = ""

		await asyncio.sleep(5)

def main():
	client.bg_task = client.loop.create_task(rodando())
	client.run(lervariavel())

if __name__ == "__main__":
	main()
