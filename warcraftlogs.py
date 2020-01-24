import requests
import json_store_client

ENDERECOLOG = 'https://www.warcraftlogs.com/reports/{reportid}'
SITE = 'https://www.warcraftlogs.com:443/v1/reports/user/{usuario}?api_key=4615d3b11c614e608c6f294610f81fef'

jsonstore = json_store_client.Client(
    'https://www.jsonstore.io/63816dcc35a4ec5cb91d112b23a8c3dafcee418e2736fdf509df97aa8b552e37'
)

def converterData(dataepoch):
    import time
    return time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(dataepoch / 1000))

def iniciarlizarDb(nome):
    db = jsonstore.retrieve(nome)
    if not db:
        jsonstore.store(nome, {'ultimos': '0'})
        db = jsonstore.retrieve(nome)

    return db


def texto(dados):
    texto = ':newspaper: Log:{log} \towner:{owner} \tData:{data}'.format(
        log=ENDERECOLOG.format(reportid=dados['id']),
        owner=dados['owner'],
        data=converterData(dados['end']))
    return texto


def atualizarContador():
    db = jsonstore.retrieve('exec')

    contador = db['count']
    print(str(contador))
    jsonstore.store('exec', {'count': contador + 1})


def buscarLogs(nome):
    url = SITE.format(usuario=nome)
    response = requests.get(url)
    data = []
    data = response.json()

    db = iniciarlizarDb(nome)

    listadb = []
    listalogs = []

    for itens in data:
        listadb.append(itens['id'])
        if itens['id'] not in db['ultimos']:
            listalogs.append(texto(itens))

   # print(listadb)

    jsonstore.store(nome, {'ultimos': listadb})

    if len(listalogs) >= 1:
      atualizarContador()
      print(listadb)

    return listalogs
