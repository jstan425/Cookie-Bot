import disnake, asyncio, datetime

from disnake import embeds, Option, OptionType
from disnake.ext import commands
from datetime import datetime


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Timed mute this format: 1d, 20s, 30m, etc..
@commands.bot.slash_command(
    description="Mute specified user.",
    options=[
        Option("user", "Specify user would like to mute.", OptionType.user, True), Option("time", "Specify duration.", OptionType.string, True), Option("reason", "Reason being punish", OptionType.string, False)
    ],
)
@commands.has_permissions(manage_messages=True)
async def tempmute(ctx, user: disnake.user = None, time=str, *, reason=None):
    role = disnake.utils.get(ctx.guild.roles, name="Muted")
    time_convert = {"s":1, "m":60, "h":3600,"d":86400}
    mute_time = int(time[0]) * time_convert[time[-1]]
    await user.add_roles(role)
    embed = disnake.Embed(description= f"✅ **{user.display_name}#{user.discriminator} muted successfuly**", 
                          color=disnake.Color.green()
                          )
    await ctx.send(embed=embed, delete_after=5)
    await asyncio.sleep(mute_time)
    await user.remove_roles(role)

    return
