import disnake
import logging
import os

from disnake.ext import commands
from disnake.ext.commands import Param


class Essential(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Ping the bot!")
    async def ping(self, 
                   inter: disnake.ApplicationCommandInteraction,):
        await inter.response.send_message(f"Cookie Crumps detected in {round(self.bot.latency * 1000)}ms")
    
    @commands.slash_command(description="Reloads all cogs")
    async def reload(self, inter: disnake.ApplicationCommandInteraction):
        for folder in os.listdir("cogs"):
            if os.path.exists(os.path.join("cogs", folder, "cog.py")):
                self.bot.unload_extension(f"cogs.{folder}.cog")
                self.bot.load_extension(f"cogs.{folder}.cog")
        await inter.response.send_message('Cogs fully reloaded.')
        
def setup(bot: commands.Bot):
    bot.add_cog(Essential(bot))
    print('Essentials cog is now loaded' + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Added Essential Cog")

def teardown(bot: commands.Bot):
    bot.remove_cog("Essential")
    print('Essentials cog is now unloaded' + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Removed Essential Cog")