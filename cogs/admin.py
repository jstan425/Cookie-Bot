import disnake
from disnake.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.bot.slash_command(description="Kick Member out of the Server.")
    @commands.has_permissions(kick_members = True)
    async def kick(ctx, member : disnake.Member,*,reason = "No reason provided, contact admin!"):
        await ctx.send(member.name + "have been kicked for" +reason)
        await member.kick(reason=reason)

    @commands.bot.slash_command(description="Ban Member from the Server.")
    @commands.has_permissions(ban_members = True)
    async def ban(ctx, member : disnake.Member,*,reason = "No reason provided, contact admin!"):
        await ctx.send(member.name + "have been ban for" +reason)
        await member.ban(reason=reason)              