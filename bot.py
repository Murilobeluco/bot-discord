#!/usr/bin/python3
from discord.ext import commands
from discord.ext.commands import Bot
from randomemoji import desenho, random_emoji, turtle_emoji
from util import rng, busca_cotacao, cria_audio, mensagem_formatada, deleta_arquivo, str_qrcode, encurtar_url, retorna_link_youtube
import asyncio
import discord
import os
import time
import psutil
import urllib.parse
import raider

BOT_PREFIX = '!'

client = Bot(command_prefix=BOT_PREFIX)


# client.remove_command('help')

def lervariavel():
    import os
    variavel = os.environ['TOKEN']

    if not variavel:
        raise Exception('Configurar variavel de ambinete TOKEN')

    return variavel


async def envia(ctx, arq):
    with open(arq, 'rb') as fp:
        await ctx.send(file=discord.File(fp, arq))


def enviar_midia(ctx, arq=''):
    def after_func(error):
        if arq:
            coro = envia(ctx, arq)
            print(error)
            fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
            fut.result()

    return after_func


async def tocaraudio(ctx, audio='', arquivo=''):
    if ctx.voice_client is None:
        if not ctx.author.voice is None:
            vc = await ctx.author.voice.channel.connect()
            source = discord.FFmpegPCMAudio(source=audio)

            ctx.voice_client.play(source, after=enviar_midia(ctx=ctx, arq=arquivo))

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
    """retorna um sheriff feito de emoji."""
    mensagem = '{0.author.mention}, este é seu Random Sheriff Emoji: \n {sheriff}'.format(
        ctx.message, sheriff=desenho(random_emoji()))
    await ctx.send(mensagem)


@client.command()
async def link(ctx, arg1):
    """retorna um link direto para download do youtube."""
    resultado = encurtar_url(retorna_link_youtube(arg1))
    await ctx.send(embed=mensagem_formatada(titulo='Link para Download', descricao=f'Video: {arg1}', url=resultado, imagem_url=str_qrcode(resultado)))


@client.command()
async def qrcode(ctx, arg1):
    e = discord.Embed()
    texto = urllib.parse.quote_plus(arg1)
    e.set_image(
        url=str_qrcode(texto))
    await ctx.send(embed=e)


@client.command()
async def pedra(ctx):
    """toca um audio randômico chamando o grupo para fazer pedra."""
    await tocaraudio(ctx,
                     rng(['audios/caralhovamosfazerpedra.mp3', 'audios/cadepedra.mp3', 'audios/vamosfazerpedra.mp3']))


@client.command()
async def blizz(ctx):
    """toca um audio randômico que fala verdades sobre a blizzard."""
    await tocaraudio(ctx, rng(['audios/infoblizzard.mp3', 'audios/wowbug.mp3', 'audios/wowbugado.mp3']))


@client.command(aliases=['vegeta', 'dbz'])
async def olha(ctx):
    """toca um audio da dublagem portuguesa de dragonball z"""
    await tocaraudio(ctx, 'audios/olha.mp3')


@client.command()
async def cohab(ctx):
    """toca um audio da Tulla Luana falando sobre a cohab"""
    await tocaraudio(ctx, 'audios/cohab.mp3')


@client.command()
async def amigo(ctx):
    """toca um audio do Satyrzinho Satanboy"""
    await tocaraudio(ctx, 'audios/amigo.mp3', arquivo='img/Satanboy.gif')


@client.command(aliases=['dolar'])
async def cotacao(ctx):
    """toca um audio com a cotação do dolar"""
    texto = busca_cotacao()
    arquivo = cria_audio(texto)
    await asyncio.sleep(2)
    await tocaraudio(ctx, arquivo)
    await ctx.send(embed=mensagem_formatada(titulo=':moneybag:Cotação:', descricao=texto))
    await deleta_arquivo(arquivo)


@client.command()
async def bfa(ctx):
    """toca um audio pedindo o que todos desejam de bfa: ..... o seu FIM!"""
    await tocaraudio(ctx, 'audios/fimbfa.mp3')


@client.command()
async def maedacarol(ctx):
    """chama a mãe da carol."""
    await tocaraudio(ctx, rng(['audios/obrigacao.mp3', 'audios/maedacarol.mp3']))


@client.command()
async def nerfa(ctx):
    """toca um audio pedindo para nerfar o que é quebrado!"""
    await tocaraudio(ctx, 'audios/broken.mp3')


@client.command()
async def machista(ctx):
    """toca um audio da loly vomito"""
    await tocaraudio(ctx, 'audios/machista.mp3', arquivo='img/machista.gif')


@client.command()
async def amanha(ctx):
    """toca um audio com a famosa frase do Semente quando é perguntado a ele se ele quer fazer ilha"""
    await tocaraudio(ctx, rng(['audios/amanha.mp3', 'audios/amanha1.mp3']))


@client.command()
async def livros(ctx):
    """toca um audio com a fala da boss Bella de lower Karazhan!"""
    await tocaraudio(ctx, 'audios/livros.mp3')


@client.command(aliases=['fumamais'])
async def fuma(ctx):
    """Isso FUMA MAIS!!!!!"""
    await tocaraudio(ctx, 'audios/fuma.mp3')


@client.command(aliases=['caipira'])
async def parana(ctx):
    """Toca um audio de uma paranaense"""
    await tocaraudio(ctx, 'audios/parana.mp3')


@client.command()
async def valkyr(ctx):
    """toca um audio em homenagem a um famoso druida que jogava cliando nas skill!"""
    await tocaraudio(ctx, 'audios/mare.mp3')


@client.command(aliases=['diabo', 'satyrzinho'])
async def satan(ctx):
    """toca um audio do Satyrzinho Satanboy"""
    await tocaraudio(ctx, rng(['audios/mortoVivoVoador.mp3', 'audios/nazareno.mp3', 'audios/chapeuDeLata.mp3']))


@client.command()
async def oak(ctx):
    """toca um audio com a fala do boss Oakheart de Darkheart Thicket."""
    await tocaraudio(ctx, 'audios/oak.mp3')


@client.command()
async def xixizinho(ctx):
    """toca um audio com a fala do boss Rokmora da melhor dungeon de legion: Neltharion''s Lair"""
    await tocaraudio(ctx, 'audios/xixizinho.mp3')


@client.command()
async def tosco(ctx):
    """toca um audio com a fala da boss Bella de lower Karazhan!"""
    await tocaraudio(ctx, 'audios/tosco.mp3')


@client.command()
async def dorime(ctx):
    """toca dorime"""
    await tocaraudio(ctx, 'audios/dorime.mp3', arquivo='img/dorime.jpg')


@client.command()
async def tururu(ctx):
    """toca a musica triste do naruto"""
    await tocaraudio(ctx, 'audios/tururu.mp3', 'img/naruto.png')


@client.command()
async def gaucho(ctx):
    """toca um audio de um gaucho falando verdades sobre armandinho"""
    await tocaraudio(ctx, 'audios/gaucho.mp3')


@client.command()
async def saizica(ctx):
    """toca um audio da boss galindra de lower karazhan"""
    await tocaraudio(ctx, 'audios/zica.mp3', 'img/titus.gif')


@client.command()
async def triste(ctx):
    """eu fico muito triste com uma noticia dessas"""
    await tocaraudio(ctx, 'audios/triste.mp3', 'img/triste.gif')


@client.command(aliases=['essencias', 'essences', 'iongod'])
async def milagre(ctx):
    """posta uma imagem de um milagre"""
    await tocaraudio(ctx, 'audios/milagre.mp3', 'img/essence.png')


@client.command()
async def personagem(ctx, arg1):
    """Retorna Informações sobre personagem"""
    nome = arg1[:arg1.find('/')]
    reino = arg1[arg1.find('/')+1:]
    await ctx.send(embed=raider.informacao(nome, reino))


@client.command()
async def falar(ctx, arg1, arg2='pt-br'):
    """Faz o bot falar"""
    arquivo = cria_audio(arg1, arg2)
    await asyncio.sleep(2)
    await tocaraudio(ctx, arquivo)
    await deleta_arquivo(arquivo)


@client.command()
async def drogas(ctx):
    """toca um audio avisando que chegou drogas"""
    await tocaraudio(ctx, 'audios/droga.mp3')


@client.command()
async def heart(ctx):
    """toca um audio em homenagem ao Heart"""
    await tocaraudio(ctx, 'audios/heart.mp3')


@client.command()
async def birl(ctx):
    """Birl"""
    await tocaraudio(ctx, 'audios/birl.mp3')


@client.command(aliases=['radiohead', 'vida'])
async def padraodevida(ctx):
    """Fitter Happier"""
    await tocaraudio(ctx, 'audios/FitterHappier.mp3')


@client.command(aliases=['pedro', 'calouro'])
async def fodo(ctx):
    """Pedro Gordo Calouro"""
    await tocaraudio(ctx, rng(['audios/fodo.mp3', 'audios/oralzinho.mp3']))


@client.command()
async def turtle(ctx):
    """toca a musica A Turtle Made It to the Water!"""
    await tocaraudio(ctx, 'audios/turtle.mp3')
    await ctx.send(turtle_emoji())


@client.command(aliases=['corona', 'coronavirus'])
async def virus(ctx):
    """CoronaVirus"""
    await tocaraudio(ctx, 'audios/coronavirus.mp3', arquivo='img/virus.gif')


@client.command(aliases=['braba', 'tadinha'])
async def brava(ctx):
    """Luciana gimenes perguntando se voce esta brava!"""
    await tocaraudio(ctx, 'audios/brava.mp3')


@client.command()
async def bichao(ctx):
    """Você é o bichao mesmo em doido"""
    await tocaraudio(ctx, 'audios/bichao.mp3')


@client.command()
async def paula(ctx):
    """Paula e seus amigos"""
    await tocaraudio(ctx, 'audios/paula.mp3')


@client.command(aliases=['deus', 'timming'])
async def tempodedeus(ctx):
    """God''s timing is always right"""
    await tocaraudio(ctx, 'audios/tempodedeus.mp3')


@commands.has_any_role(754441783362060289, 754441373582622811)
@client.command(pass_context=True)
async def kick(user: discord.Member):
    await user.move_to(None)


@client.command(aliases=['cenaotinhaquenemtaaquilinda', 'barraco'])
async def tati(ctx):
    """Tati quebra barraco dizendo: "voce nao tinha que nem estar aqui linda\""""
    await tocaraudio(ctx,
                     rng(['audios/tati.mp3', 'audios/madame.mp3', 'audios/gostocada.mp3', 'audios/presidentetati.mp3']))


@client.command()
async def ping(ctx):
    """mostra o ping do bot com o servidor do discord"""
    before = time.monotonic()
    before_ws = int(round(client.latency * 1000, 1))
    message = await ctx.send("🏓 Pong")
    pings = (time.monotonic() - before) * 1000
    await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(pings)}ms")


@client.command(aliases=['joinme', 'join', 'botinvite'])
async def invite(ctx):
    """gera um link para convite do bot"""
    await ctx.author.send(
        f"**{ctx.author.name}**, Use essa URL para me convidar para o seu servidor\n<{discord.utils.oauth_url(client.user.id)}>")


@client.command(aliases=['info', 'stats', 'status'])
async def about(ctx):
    """informação sobre o bot"""
    process = psutil.Process(os.getpid())
    ram_usage = process.memory_full_info().rss / 1024 ** 2
    avgmembers = round(len(client.users) / len(client.guilds))

    embed = discord.Embed(color=0xbe2f2f, title=f"**__Status do Bot__**")
    embed.set_thumbnail(url=ctx.bot.user.avatar_url)
    embed.add_field(name="📙 Library", value="discord.py - Versão {versao}".format(versao=discord.__version__),
                    inline=True)
    embed.add_field(name="🖥️ Servidores", value=f"{len(ctx.bot.guilds)} (avg: {avgmembers} users/server)", inline=True)
    embed.add_field(name="📜 Comandos", value=len([x.name for x in client.commands]), inline=True)
    embed.add_field(name="💾 RAM", value=f"{ram_usage:.2f} MB", inline=True)

    await ctx.send(content=f"ℹ Informações sobre o Bot: **{ctx.bot.user}**", embed=embed)


@client.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.CommandNotFound):
        await ctx.send(embed=mensagem_formatada(titulo='\N{WARNING SIGN}Erro:',
                                                descricao=f'Comando: {ctx.message.content} não encontrado.'))
    elif isinstance(exception, commands.MissingRequiredArgument):
        await ctx.send('O comando precisa de um parametro')
    elif isinstance(exception, commands.CommandInvokeError):
        await ctx.send('Erro ao executar comando: ' + ctx.message.content + ' Erro Interno: ' + str(exception))
    elif isinstance(exception, commands.errors.MissingRole):
        await ctx.send('Você não tem permissão para usar esse comando!')
    elif isinstance(exception, commands.errors.MissingAnyRole):
        await ctx.send('Você não tem permissão para usar esse comando!')


@client.event
async def on_ready():
    print('Bot')
    print(client.user.name)
    print(client.user.id)
    print('------')

    activity = discord.Game(name='World of Warcraft')
    await client.change_presence(activity=activity)


# async def rodando():
#     await client.wait_until_ready()
#     channel = client.get_channel(437937862223069185)
#
#     if channel is not None:
#         while not client.is_closed():
#             nomes = ['Murilobeluco', 'Heartmelody', 'Enocc']
#
#             retorno = ''
#             for val in nomes:
#                 result = buscarLogs(val)
#                 if len(result) >= 1:
#                     for itens in result:
#                         retorno = retorno + '\n' + itens
#
#             if retorno:
#                 await channel.send(retorno)
#                 retorno = ''
#
#             await asyncio.sleep(600)

def main():
    # client.bg_task = client.loop.create_task(rodando())
    client.run(lervariavel())


if __name__ == '__main__':
    main()
