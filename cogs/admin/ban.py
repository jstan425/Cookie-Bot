import disnake, asyncio, datetime

from disnake.ext import commands
from datetime import datetime


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.bot.slash_command(description="Ban user from the Server.")
    async def ban(self, ctx, user : disnake.user,*,reason: None):
        await ctx.response.send_message(user.name + "have been ban for" + reason)
        await disnake.guild.ban(reason)
    
    @commands.bot.slash_command(description="Unban user from the Server.")
    async def unban(self, ctx, user : disnake.user):
        await ctx.response.send_message(user.name + "have been unban!")
        await disnake.guild.unban(user)
    
    #Tempban a user for certain durations and unban when it duration ends    
    @commands.bot.slash_command(description="Temporary ban user for certain duration, and unban after duration ends.")
    async def tempban(self, ctx, user : disnake.user, duration: int,* , reason: None):
        await ctx.send(user.name + "have been temporary banned for" + reason + "for" + duration  + "day.")
        await disnake.guild.ban(user)
        await asyncio.sleep(duration)
        await disnake.guild.unban(user)
        #Find a way to not only send message to the discord, but send DMs to the user as well.
        #Create a way to keep the time in a file and have the bot check for the time when the server is offline.