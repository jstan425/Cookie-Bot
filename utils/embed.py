import os
import disnake
import datetime
import asyncio

from disnake.ext import commands
from disnake.ext.commands.bot import Bot
from dotenv import load_dotenv


def return_current_time():
    time = datetime.datetime.utcnow()
    return time.strftime("%A, %b %d %H:%M")


class embed(commands.cog):
    def __init__(self, bot: commands.bot):
        self.bot = Bot


NEGATIVECOLOR = 0xD00000
SLIGHTLYNEGATIVECOLOR = 0xF26E00
POSITIVECOLOR = 0x419400
NEUTRALCOLOR = 0x607D8B
DELETEDCOLOR = 0x3399CC
EDITEDCOLOR = 0x00E4C9
USEREDITCOLOR = 0xE9E6C2
ROLECOLOR = 0x800080


class banEmbed(disnake.embed):
    def __init__(self, banned_user: disnake.user, resp_mod: disnake.user, reason: str):
        local_title = f"{banned_user.name} was banned by {resp_mod.name}"
        local_desc = f"Reason: {reason}"
        super().__init__(
            color=NEGATIVECOLOR,
            title=local_title,
            description=local_desc,
        )
        self.set_footer(text=return_current_time())


class kickEmbed(disnake.embed):
    def __init__(self, kicked_user: disnake.user, resp_mod: disnake.user, reason: str):
        local_title = f"{kicked_user.name} was banned by {resp_mod.name}"
        local_desc = f"Reason: {reason}"
        super().__init__(
            color=NEGATIVECOLOR,
            title=local_title,
            description=local_desc,
        )
        self.set_footer(text=return_current_time())


# class embed(disnake.embed):
#     async def embed_new(title = None, description = None, color = disnake.Embed.Empty, user : disnake.Member = None, fields : dict = None, thumbnail = None):

#         embed = disnake.Embed(title=title, description=description, color=color)

#         if fields != None:
#             for k in fields:
#                 embed.add_field(name=k, value=fields[k], inline=False)

#         if user != None:
#             embed.set_thumbnail(url=user.display_avatar.url)

#         if thumbnail != None:
#             embed.set_thumbnail(url=thumbnail)
#         return embed
