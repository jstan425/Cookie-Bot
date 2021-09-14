import disnake
from disnake.ext import commands


class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.bot.slash_command(description="Kick user out of the Server.")
    async def kick(self, ctx, user : disnake.user,*,reason: None):
        await ctx.send(user.name + "have been kicked for" + reason)
        await user.kick(reason = reason)

    @commands.bot.slash_command(description="Ban user from the Server.")
    async def ban(self, ctx, user : disnake.user,*,reason: None):
        await ctx.send(user.name + "have been ban for" + reason)
        await user.ban(reason)
    
    @commands.bot.slash_command(description="Unban user from the Server.")
    async def unban(self, ctx, user : disnake.user,*,reason: None):
        await ctx.send(user.name + "have been ban for" + reason)
        await user.unban(reason)