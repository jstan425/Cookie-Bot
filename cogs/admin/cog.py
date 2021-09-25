import logging

from disnake.ext import commands
from .ban import Ban
from .kick import Kick
from .mute import Mute


    
def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))
    bot.add_cog(Kick(bot))
    bot.add_cog(Mute(bot))
    print('Admin cog is now loaded.' + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Added Admin Cog.")


def teardown(bot: commands.Bot):
    bot.remove_cog("Ban")
    bot.remove_cog("Kick")
    bot.remove_cog("Mute")
    print('Admin cog is now unloaded.' + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Removed Admin Cog.")