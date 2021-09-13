import disnake
from disnake.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.bot.slash_command(description="Kick Member out of the Server.")
    async def kick(self, ctx, user : disnake.user,*,reason: str = "No reason provided, contact admin!"):
        await ctx.send(user.name + "have been kicked for" + reason)
        await user.kick(reason=reason)

    @commands.bot.slash_command(description="Ban Member from the Server.")
    async def ban(self, ctx, user : disnake.user,*,reason: str = "No reason provided, contact admin!"):
        await ctx.send(user.name + "have been ban for" + reason)
        await user.ban(reason=reason)              