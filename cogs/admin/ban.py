import disnake, asyncio, datetime

from disnake.ext import commands
from disnake.ext.commands import Param
from datetime import datetime


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

@commands.slash_command(description="Ban user from the Server.")
async def ban(self, 
              inter: disnake.ApplicationCommandInteraction,
              user: disnake.user = Param(None, desc="Specify a user"), 
              reason = Param(None, desc="Provide a reason"),
):
    embed = disnake.Embed(
        description=(f"✅ **{user.display_name}#{user.discriminator} is banned for {reason}"),
        color=disnake.Color.red(),
    )
    await inter.channel.send(embed=embed)
    await user.ban(user, reason=reason)


@commands.slash_command(description="Unban user from the Server.")
async def unban(self, 
              inter: disnake.ApplicationCommandInteraction,
              user: disnake.user = Param(None, desc="Specify a user"), 
              reason: str = Param(None, desc="Provide a reason"),
):
    embed = disnake.Embed(
        description=(f"✅ **{user.display_name}#{user.discriminator} had been unbanned"),
        color=disnake.Color.green(),
    )
    await inter.channel.send(embed=embed)
    await user.unban(user)


@commands.slash_command(description="Tempban user from the server.")
async def tempban(self, 
              inter: disnake.ApplicationCommandInteraction,
              user: disnake.user = Param(None, desc="Specify a user"), 
              time: str = Param(None, desc="Specify a time"),
              reason: str = Param(None, desc="Provide a reason"),
):
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    ban_time = int(time[0]) * time_convert[time[-1]]
    embed = disnake.Embed(
        description=(f"✅ **{user.display_name}#{user.discriminator} had been tempban for {time} successfully**"),
        color=disnake.Color.green(),
    )
    await user.ban(user, reason=reason)
    await inter.channel.send(embed=embed)
    await asyncio.sleep(ban_time)
    await user.unban(user)
