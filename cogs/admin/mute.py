import disnake, asyncio, datetime

from disnake import embeds
from disnake.ext import commands
from disnake.ext.commands import Param
from datetime import datetime


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Timed mute this format: 1d, 20s, 30m, etc..
@commands.slash_command(description="Mute specified user.")
async def tempmute(
    self,
    inter: disnake.ApplicationCommandInteraction,
    user: disnake.User = Param(None, desc="Specify a user"),
    time: str = Param(None, desc="Specify a time"),
    reason: str = Param(None, desc="Provide a reason"),
):
    role = disnake.utils.get(inter.guild.roles, name="Muted")
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    mute_time = int(time[0]) * time_convert[time[-1]]
    await user.add_roles(role)
    embed = disnake.Embed(
        description=f"✅ **{user.display_name}#{user.discriminator} muted successfuly**",
        color=disnake.Color.green(),
    )
    # TODO: change send embed method.
    await inter.channel.send(embed=embed)
    await asyncio.sleep(mute_time)
    await user.remove_roles(role)
