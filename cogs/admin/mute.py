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
async def tempmute(ctx, user: disnake.user = None, time=int, d=str, *, reason=None):
    guild = ctx.guild

    for role in guild.roles:
        #if role.name == "Muted":
        if role.id == 889864145040736266:
            await user.add_roles(role)

            embed = disnake.Embed(
                title="Muted!",
                description=f"{user.mention} has been tempmuted",
                colour=disnake.Colour.light_gray(),
            )
            embed.add_field(name="reason:", value=reason, inline=False)
            embed.add_field(
                name="Time left for the mute:", value=f"{time}{d}", inline=False
            )
            await ctx.send(embed=embed)

        if d == "d":
            seconds = time * 86400
        elif d == "h":
            seconds = time * 60 * 60
        elif d == "m":
            seconds = time * 60
        elif d == "s":
            seconds = time * 1
        await user.remove_roles(role)

        embed = disnake.Embed(
            title="Temp Unmute",
            description=f"Unmuted - {user.mention}",
            colour=disnake.colour.light_gray(),
        )
        await ctx.send(embed=embed)

        return
