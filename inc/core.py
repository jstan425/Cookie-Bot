import os
import disnake

from dotenv import load_dotenv


def embedGenerator(type, title, description):
    if type == "good":
        embed = disnake.Embed(title=title, description=description, color=0x2BFF00)
    elif type == "neutral":
        embed = disnake.Embed(title=title, description=description, color=0xFFAE00)
    elif type == "bad":
        embed = disnake.Embed(title=title, description=description, color=0xFF0000)

    embed.set_author(name="OpenTorn")
    return embed