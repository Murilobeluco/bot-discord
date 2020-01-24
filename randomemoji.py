from itertools import accumulate
from bisect import bisect
from random import randrange
from unicodedata import name as unicode_name

UNICODE_VERSION = 6

EMOJI_RANGES_UNICODE = {
    6: [
        ('\U0001F300', '\U0001F320'),
        ('\U0001F330', '\U0001F335'),
        ('\U0001F337', '\U0001F37C'),
        ('\U0001F380', '\U0001F393'),
        ('\U0001F3A0', '\U0001F3C4'),
        ('\U0001F3C6', '\U0001F3CA'),
        ('\U0001F3E0', '\U0001F3F0'),
        ('\U0001F400', '\U0001F43E'),
        ('\U0001F440', ),
        ('\U0001F442', '\U0001F4F7'),
        ('\U0001F4F9', '\U0001F4FC'),
        ('\U0001F500', '\U0001F53C'),
        ('\U0001F540', '\U0001F543'),
        ('\U0001F550', '\U0001F567'),
        ('\U0001F5FB', '\U0001F5FF')
    ],
    7: [
        ('\U0001F300', '\U0001F32C'),
        ('\U0001F330', '\U0001F37D'),
        ('\U0001F380', '\U0001F3CE'),
        ('\U0001F3D4', '\U0001F3F7'),
        ('\U0001F400', '\U0001F4FE'),
        ('\U0001F500', '\U0001F54A'),
        ('\U0001F550', '\U0001F579'),
        ('\U0001F57B', '\U0001F5A3'),
        ('\U0001F5A5', '\U0001F5FF')
    ],
    8: [
        ('\U0001F300', '\U0001F579'),
        ('\U0001F57B', '\U0001F5A3'),
        ('\U0001F5A5', '\U0001F5FF')
    ]
}

NO_NAME_ERROR = '(No name found for this codepoint)'

def quantos_dias():
    from datetime import datetime
    import random
    nomes = ['Biroliro','Bostonaro','LiroBiro', 'Bolonoro', 'Boldonaro', 'Bobonaro', 'Bolinaro', 'Bololonaro', 'Laranja', 'Coiso', 'Bozo']
    now = datetime.now()

    d2 = datetime.strptime('2022-12-31', '%Y-%m-%d')

    quantidade_dias = abs((now - d2).days)
    return "Ainda vamos ter que aguentar o {nome} por mais {dias} dias :point_right: :point_right: :flag_br:".format(dias=quantidade_dias, nome=random.choice(nomes))

def audio_random_pedra():
    import random
    audio = ['caralhovamosfazerpedra.mp3', 'cadepedra.mp3', 'vamosfazerpedra.mp3']
    escolha = random.choice(audio)
    print(escolha)
    return escolha
    
def audio_random_blizz():
    import random
    audio = ['infoblizzard.mp3', 'wowbug.mp3']
    escolha = random.choice(audio)
    print(escolha)
    return escolha
    
def random_emoji(unicode_version = 6):
    if unicode_version in EMOJI_RANGES_UNICODE:
        emoji_ranges = EMOJI_RANGES_UNICODE[unicode_version]
    else:
        emoji_ranges = EMOJI_RANGES_UNICODE[-1]

    count = [ord(r[-1]) - ord(r[0]) + 1 for r in emoji_ranges]
    weight_distr = list(accumulate(count))

    point = randrange(weight_distr[-1])

    emoji_range_idx = bisect(weight_distr, point)
    emoji_range = emoji_ranges[emoji_range_idx]

    point_in_range = point
    if emoji_range_idx is not 0:
        point_in_range = point - weight_distr[emoji_range_idx - 1]

    emoji = chr(ord(emoji_range[0]) + point_in_range)
    emoji_name = unicode_name(emoji, NO_NAME_ERROR).capitalize()
    emoji_codepoint = "U+{}".format(hex(ord(emoji))[2:].upper())

    return (emoji, emoji_codepoint, emoji_name)

def desenho(emoji):
  return "⠀ ⠀ ⠀  :cowboy:\n　      {emoji}{emoji}\n    {emoji}   {emoji}　{emoji}\n   :wave:  {emoji}{emoji} :thumbsup:\n  　  {emoji}　{emoji}\n　   {emoji}　 {emoji}\n　     :boot:    :boot:\nSheriff feito de: '{emoji_nome}'".format(emoji=emoji[0], emoji_nome=emoji[2])