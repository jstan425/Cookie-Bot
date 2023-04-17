import disnake
import logging

from disnake.ext import commands
from .embed import embed, banEmbed, kickEmbed


def setup(bot: commands.Bot):
    bot.add_cog(embed(bot))
    bot.add_cog(banEmbed(bot))
    bot.add_cog(kickEmbed(bot))

    print('Util cog is now loaded.' + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Added Util Cog.")


def teardown(bot: commands.Bot):
    bot.remove_cog("embed")
    bot.remove_cog("banEmbed")
    bot.remove_cog("kickEmbed")

    print('Util cog is now unloaded.' + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Removed Util Cog.")