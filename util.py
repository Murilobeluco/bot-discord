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
    tts = gTTS('Por que choras?!, {parametro}'.format(parametro=texto), lang='pt-br')
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

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    import textwrap
    from PIL import ImageDraw
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=40)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text), 
                  line, font=font, fill=text_color)
        y_text += line_height

async def gerar_meme(texto):
    from PIL import Image, ImageFont 
    image = Image.open("img/drauzio.jpg")
    fontsize = 40 
    font = ImageFont.truetype("Roboto-Regular.ttf", fontsize)

    text_color = (0, 0, 0)
    text_start_height = 0
    draw_multiple_line_text(image, texto, font, text_color, 400)
    image.save('img/drauzio-edit.jpg')