from disnake.ext import commands
from .mods import Mods


# setup functions for bot
def setup(bot: commands.Bot):
    bot.add_cog(Mods(bot))