import disnake
from disnake.ext import commands
from disnake.ext.commands import Param


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description = "Kick user from the Server.")
    async def kick(
        self,
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.User = Param(None, desc = "Specify a user"),
        reason: str = Param(None, desc = "Provide a reason"),
    ):
        if user is None:
            await inter.channel.send("Specify a user to kick.")
            return
        embed = disnake.Embed(
            description = (
                f"✅ **{user.display_name}#{user.discriminator} is kicked!"
                ),
                color = disnake.Color.red(),
        )   
        await inter.send(user.name + "have been kicked!"),
        await disnake.guild.kick(reason = reason)

