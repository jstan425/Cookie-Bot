import disnake
import logging

from disnake.ext import commands
from .embedg import *


def setup(bot: commands.Bot):
    bot.add_cog(banEmbed(bot))

    print('Util cog is now loaded.' + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Added Util Cog.")


def teardown(bot: commands.Bot):
    bot.remove_cog("banEmbed")

    print('Util cog is now unloaded.' + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Removed Util Cog.")