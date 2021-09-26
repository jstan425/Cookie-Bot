import os
import disnake
import datetime

from disnake.ext import commands
from disnake.ext.commands.bot import Bot
from disnake.ext.commands.core import command
from dotenv import load_dotenv


def return_current_time():
    time = datetime.datetime.utcnow()
    return time.strftime('%A, %b %d %H:%M')


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

class banEmbed(disnake.embed):
    def __init__(self, banned_user: disnake.user, resp_mod: disnake.user, reason: str):
        local_title = f'{banned_user.name} was banned by {resp_mod.name}'
        local_desc = f'Reason: {reason}'
        super().__init__(color=NEGATIVECOLOR, title=local_title, description=local_desc,)
        self.set_footer(text=return_current_time())