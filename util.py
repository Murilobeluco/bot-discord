def rng(lista):
    import random
    escolha = random.choice(lista)
    if escolha == retorna_ultimo_rng():
        escolha = rng(lista)
    salvar_rng(escolha)
    return escolha


def mensagem_formatada(titulo='', descricao='', url='', imagem_url=''):
    import discord
    em = discord.Embed()
    em.title = titulo
    if url:
        em.url = url
    if imagem_url:
        em.set_image(url=imagem_url)
    em.description = descricao
    return em


def cria_audio(texto, lingua='pt-br'):
    from gtts import gTTS
    from io import BytesIO
    import tempfile
    import os

    byte_stream = BytesIO()
    tts = gTTS('{parametro}'.format(parametro=texto), lang=lingua)
    tts.write_to_fp(byte_stream)
    byte_stream.seek(0)

    temp_file, temp_path = tempfile.mkstemp(suffix='.mp3')
    with open(temp_path, mode='wb') as file:
        byte_stream.seek(0)
        file.write(byte_stream.read())
        file.flush()

    os.close(temp_file)
    byte_stream.close()
    return temp_path


def busca_cotacao():
    import requests
    from datetime import datetime
    try:
        response = requests.get('https://economia.awesomeapi.com.br/json/all/USD')

        dados = response.json()

        data = datetime.strptime(dados['USD']['create_date'], '%Y-%m-%d %H:%M:%S')
        data_convertida = data.strftime('%d/%m/%Y %H:%M:%S')

        return 'Cotação do ' + dados['USD']['name'] + ' é R$ ' + dados['USD'][
            'bid'] + ' Atualizado em: ' + data_convertida
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
        'Content-Type': 'application/json',
        'secret-key': '$2b$10$W1HJIZPyGuvMH26c8DmrSedhgbGtlrAPio4l8.tiCuAUeWchLyKcq',
        'versioning': 'false'
    }

    requests.put(url, json=payload, headers=headers)


def retorna_ultimo_rng():
    import requests

    url = "https://api.jsonbin.io/b/5fa1f89aa03d4a3bab0c7230"
    headers = {
        'Content-Type': 'application/json',
        'secret-key': '$2b$10$W1HJIZPyGuvMH26c8DmrSedhgbGtlrAPio4l8.tiCuAUeWchLyKcq',
    }
    response = requests.get(url, headers=headers)
    json_resposta = response.json()
    return json_resposta['rng']


def retorna_link_youtube(url):
    from youtube_dl import YoutubeDL
    ydl = YoutubeDL({
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '420',
        }],
    })
    resposta = ydl.extract_info(url, download=False)
    return resposta['url']


def encurtar_url(url):
    import requests
    callback = f'https://tinyurl.com/api-create.php?url={url}'
    response = requests.get(url=callback)
    return response.text


def str_qrcode(texto):
    return f'http://api.qrserver.com/v1/create-qr-code/?data={texto}&qzone=3&margin=0&size=450x450&ecc=M'
