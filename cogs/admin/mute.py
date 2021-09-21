import disnake, asyncio, datetime

from disnake import embeds
from disnake.ext import commands
from datetime import datetime


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# Timed mute this format: 1d, 20s, 30m, etc..
@commands.bot.slash_command(description="Mute specified user.")
@commands.has_permission(manage_messages=True)
async def tempmute(ctx, user: disnake.user, time=int, d=str, *, reason=None):
    if not user:
        await ctx.send("You must mention a member to mute!")
    elif not time:
        await ctx.send("You must mention a time!")
    elif not reason:
        reason = "No reason given"
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await user.add_roles(role)

            embed = disnake.Embed(
                title="Muted!",
                description=f"{user.mention} has been tempmuted",
                olour=disnake.Colour.light_gray(),
            )
            embed.add_field(name="reason:", value=reason, inline=False)
            embed.add_field(
                name="Time left for the mute:", value=f"{time}{d}", inline=False
            )
            await ctx.send(embed=embed)

        if d == "s":
            seconds = time * 1
        elif d == "m":
            seconds = time * 60
        elif d == "h":
            seconds = time * 60 * 60
        elif d == "d":
            seconds = time * 86400

        await user.remove_roles(role)

        embed = disnake.Embed(
            title="Temp Unmute",
            description=f"Unmuted - {user.mention}",
            colour=disnake.colour.light_gray(),
        )
        await ctx.send(embed=embed)

        return
