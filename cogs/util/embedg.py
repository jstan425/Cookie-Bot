import os
import disnake

from disnake.ext import commands
from disnake.ext.commands.bot import Bot
from disnake.ext.commands.core import command
from dotenv import load_dotenv


class EmbedG(commands.cog):
    def __init__(self, bot:commands.bot):
        self.bot=Bot

NEGATIVECOLOR = 0xD00000
SLIGHTLYNEGATIVECOLOR = 0xF26E00
POSITIVECOLOR = 0x419400
NEUTRALCOLOR = 0x607d8b
DELETEDCOLOR = 0x3399CC
EDITEDCOLOR = 0x00E4C9
USEREDITCOLOR = 0xe9e6c2
ROLECOLOR = 0x800080

def embedGenerator(type, title, description):
    if type == "good":
        embed = disnake.Embed(title=title, description=description, color=POSITIVECOLOR)
    elif type == "neutral":
        embed = disnake.Embed(title=title, description=description, color=NEUTRALCOLOR)
    elif type == "bad":
        embed = disnake.Embed(title=title, description=description, color=NEGATIVECOLOR)

    embed.set_author(name="CookieBot")
    return embed