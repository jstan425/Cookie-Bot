import logging

from disnake.ext import commands

from .moderation import ban, kick, mute


def setup(bot: commands.Bot):
    bot.add_cog(ban(bot))
    bot.add_cog(kick(bot))
    bot.add_cog(mute(bot))
    bot.add_cog(timeout(bot))
    # bot.add_cog(purge(bot))

    print("Admin cog is now loaded." + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Added Admin Cog.")


def teardown(bot: commands.Bot):
    bot.remove_cog("ban")
    bot.remove_cog("kick")
    bot.remove_cog("mute")
    bot.remove_cog("timeout")
    # bot.remove_cog("purge")
    
    print("Admin cog is now unloaded." + "\n")
    logger = logging.getLogger("disnake")
    logger.info("Removed Admin Cog.")
