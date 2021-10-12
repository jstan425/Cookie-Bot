import typing

import disnake
from disnake import client
from disnake import errors
from disnake import Forbidden
from disnake import TextChannel
from disnake import User
from disnake.ext import commands
from disnake.ext.commands import Param


def is_me(author):
    return author.author == client.user


class Purge(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Clear messsage from the Discord channel.")
    async def purge(
        self,
        inter: disnake.ApplicationCommandInteraction,
        messages: int = Param(None, desc="Number of message to clear"),
    ):
        # Clear <n> messages from current channel.
        channel = disnake.TextChannel
        await channel.purge(self, limit=messages, check=is_me, before=None)
        await inter.response.send_message("Messages deleted")
        return True
