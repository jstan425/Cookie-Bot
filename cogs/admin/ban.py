import disnake, asyncio, datetime

from disnake import embeds, Option, OptionType
from disnake.ext import commands
from datetime import datetime

from disnake.ext.commands.core import command, has_permissions


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


@commands.bot.slash_command(
    description="Ban user from the Server.",
    options=[
        Option("user", "Specify user would like to ban.", OptionType.user, True),
        Option("reason", "Reason being punish", OptionType.string, False),
    ],
)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: disnake.user, *, reason: None):
    embed = disnake.Embed(
        description=f"✅ **{user.display_name}#{user.discriminator} is banned for {reason}",
        color=disnake.Color.red(),
    )
    await ctx.channel.send(embed=embed)
    await user.ban(reason)


@commands.bot.slash_command(
    description="Unban user from the Server.",
    options=[Option("user", "Specify user would like to ban.", OptionType.user, True)],
)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: disnake.user):
    embed = disnake.Embed(
        description=f"✅ **{user.display_name}#{user.discriminator} had been unbanned",
        color=disnake.Color.green(),
    )
    await ctx.channel.send(embed=embed)
    await user.unban(user)


@commands.bot.slash_command(
    description="Tempban specified user.",
    options=[
        Option("user", "Specify user would like to ban.", OptionType.user, True),
        Option("time", "Specify duration.", OptionType.string, True),
        Option("reason", "Reason being punish", OptionType.string, False),
    ],
)
@commands.has_permissions(ban_members=True)
async def tempban(ctx, user: disnake.member = None, time=str, *, reason=None):
    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    ban_time = int(time[0]) * time_convert[time[-1]]
    embed = disnake.Embed(
        description=f"✅ **{user.display_name}#{user.discriminator} had been tempban for {time} successfully**",
        color=disnake.Color.green(),
    )
    await ctx.channel.send(embed=embed)
    await user.ban(reason)
    await asyncio.sleep(ban_time)
    await user.unban(user)
