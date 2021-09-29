import disnake
from disnake.ext import commands
from disnake.ext.commands import Param


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Unban user from the Server.")
    async def kick(
        self,
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.User = Param(None, desc="Specify a user"),
        reason: str = Param(None, desc="Provide a reason"),
    ):
        await inter.send(user.name + "have been kicked for" + reason)
        await disnake.guild.kick(reason=reason)
