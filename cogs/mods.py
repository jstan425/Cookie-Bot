import disnake
import asyncio
from disnake.ext import commands


class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.bot.slash_command(description="Kick user out of the Server.")
    async def kick(self, ctx, user : disnake.user,*,reason: None):
        await ctx.send(user.name + "have been kicked for" + reason)
        await disnake.guild.kick(reason = reason)

    @commands.bot.slash_command(description="Ban user from the Server.")
    async def ban(self, ctx, user : disnake.user,*,reason: None):
        await ctx.send(user.name + "have been ban for" + reason)
        await disnake.guild.ban(reason)
    
    @commands.bot.slash_command(description="Unban user from the Server.")
    async def unban(self, ctx, user : disnake.user,*,reason: None):
        await ctx.send(user.name + "have been ban for" + reason)
        await disnake.guild.unban(reason)
    
    #Tempban a user for certain durations and unban when it duration ends    
    @commands.bot.slash_command(description="Temporary ban user for certain duration, and unban after duration ends.")
    async def tempban(self, ctx, user : disnake.user, duration: int,* , reason: None):
        await ctx.send(user.name + "have been temporary banned for" + reason + "for" + duration + "day.")
        await disnake.guild.ban(user)
        await asyncio.sleep(duration)
        await disnake.guild.unban(user)
        #Find a way to not only send message to the discord, but send DMs to the user as well.