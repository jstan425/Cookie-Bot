import disnake 
from disnake.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot=bot
        
    @commands.bot.slash_command(description="Kick user out of the Server.")
    async def kick(self, ctx, user : disnake.user,*,reason: None):
        await ctx.send(user.name + "have been kicked for" + reason)
        await disnake.guild.kick(reason = reason)