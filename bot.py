#!/usr/bin/python3
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
    discord.opus.load_opus('opus')

def lervariavel():
    import os
    variavel = os.environ['TOKEN']
    
    if not variavel:
         raise Exception('Configurar variavel de ambinete TOKEN')
         exit()
    
    return variavel
    
async def tocaraudio(ctx, audio=''):
    try:
        channel = client.get_channel(ctx.author.voice.channel.id)
        vc = await channel.connect()
        
        vc.play(discord.FFmpegPCMAudio(source=audio))
        
        while vc.is_playing():
            await asyncio.sleep(1)
        
        await vc.disconnect()
    except:
        await ctx.send('Por favor entre em um canal de audio.')
     
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

@client.event
async def on_ready():
    print('Bot')
    print(client.user.name)
    print(client.user.id)
    print('------')

    activity = discord.Game(name="World of Warcraft")
    await client.change_presence(activity=activity)

@client.command(pass_context=True)
async def maedacarol(ctx):
    await tocaraudio(ctx, 'obrigacao.mp3')

async def rodando():
    await client.wait_until_ready()
    channel = client.get_channel(437937862223069185)

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

        await asyncio.sleep(5)

def main():
    client.bg_task = client.loop.create_task(rodando())
    client.run(lervariavel())

if __name__ == "__main__":
    main()
