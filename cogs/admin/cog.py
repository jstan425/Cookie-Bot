import logging

from disnake.ext import commands
from .ban import Ban
from .kick import Kick
from inc.core import *


    
def setup(bot: commands.Bot):
    bot.add_cog(Ban(bot))
    print(f"Ban cog is now loaded." +"\n")
    logger = logging.getLogger("disnake")
    logger.info("Added Ban Cog.")


def teardown(bot: commands.Bot):
    bot.remove_cog("Ban")
    print(f"Ban cog is now unloaded." +"\n")
    logger = logging.getLogger("disnake")
    logger.info("Removed Ban Cog.")    