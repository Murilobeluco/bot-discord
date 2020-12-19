import requests
import util
import discord
import os


def informacao(personagem, reino):
    try:
        resposta = requests.get(f'https://raider.io/api/v1/characters/profile?region=us&realm={reino}&name={personagem}&fields=gear,covenant,mythic_plus_scores_by_season:current,mythic_plus_recent_runs,raid_progression')
        if resposta.status_code == 200:
            json_resposta = resposta.json()

            dados_personagem = (f'Nome: {json_resposta["name"]}'
                                f'{os.linesep}'
                                f'Spec: {json_resposta["active_spec_name"]} '
                                f'{os.linesep}'
                                f'Covenant: {json_resposta["covenant"]["name"]}'
                                f'{os.linesep}'
                                f'Renown: {json_resposta["covenant"]["renown_level"]}'
                                f'{os.linesep}'
                                f'ILVL: {json_resposta["gear"]["item_level_equipped"]}'
                                )

            dados_raider = (f'Score DPS: {json_resposta["mythic_plus_scores_by_season"][0]["scores"]["dps"]}'
                            f'{os.linesep}'
                            f'Score Healer: {json_resposta["mythic_plus_scores_by_season"][0]["scores"]["healer"]}'
                            f'{os.linesep}'
                            f'Score Tank: {json_resposta["mythic_plus_scores_by_season"][0]["scores"]["tank"]}'
                            f'{os.linesep}'
                            f'Score Total: {json_resposta["mythic_plus_scores_by_season"][0]["scores"]["all"]}')

            lista_dgs = []
            for dgs in json_resposta["mythic_plus_recent_runs"]:
                lista_dgs.append(f'Dungeon: {dgs["dungeon"]} +{dgs["mythic_level"]} - {"Quebrou" if dgs["num_keystone_upgrades"]==0 else "Up+: " + str(dgs["num_keystone_upgrades"])} {os.linesep}')

            dados_raid = (f'Progressao: {json_resposta["raid_progression"]["castle-nathria"]["summary"]}'
                          f'{os.linesep}'
                          f'Normal: {str(json_resposta["raid_progression"]["castle-nathria"]["normal_bosses_killed"])}'
                          f'{os.linesep}'
                          f'Heroico: {str(json_resposta["raid_progression"]["castle-nathria"]["heroic_bosses_killed"])}'
                          f'{os.linesep}'
                          f'Mítico: {str(json_resposta["raid_progression"]["castle-nathria"]["heroic_bosses_killed"])}'
                          )

            embed = discord.Embed(color=0xbe2f2f, title=f"Informação sobre o personagem")
            embed.set_thumbnail(url=json_resposta['thumbnail_url'])
            embed.set_footer(text=f'Utlimo Scan do Raider.io: {json_resposta["last_crawled_at"]}')
            embed.url = json_resposta["profile_url"]
            embed.add_field(name="Personagem", value=dados_personagem, inline=True)
            embed.add_field(name="Raider.IO", value=dados_raider, inline=True)
            embed.add_field(name="Progressão de Raid", value=dados_raid, inline=True)
            embed.add_field(name="Ultimas Dungeons", value=' '.join([str(elem) for elem in lista_dgs]), inline=False)

            return embed
    except Exception as e:
        return print(e)
