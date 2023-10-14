import disnake
from disnake.ext import commands, tasks
from disnake.ext.commands import Param

import asyncio
import datetime
import re
import pytz
from utils.embed import *

class ban(commands.Cog):
        def __init__(self, bot: commands.Bot):
                self.bot = bot
                self.temp_ban_checker.start()
        
        @commands.slash_command(description="Ban user from the Server.")
        async def ban(
            self,
            inter: disnake.ApplicationCommandInteraction,
            user: disnake.User = Param(None, desc="Specify a user"),
            reason=Param(None, desc="Provide a reason"),
        ):
            if user is None:
                await inter.channel.send("Specify a user to ban.")
                return
            
            embed = disnake.Embed(
                description=(
                    f"✅ **{user.display_name}#{user.discriminator} is banned for {reason}"
                ),
                color = disnake.Color.red(),
            )
            await inter.channel.send(embed=embed)
            await user.ban(user, reason=reason)
            
class unban(commands.Cog):     
        def __init__(self, bot: commands.Bot):
                self.bot = bot

        @commands.slash_command(description="Unban user from the Server.")
        async def unban(
            self,
            inter: disnake.ApplicationCommandInteraction,
            user: disnake.User = Param(None, desc="Specify a user"),
            reason: str = Param(None, desc="Provide a reason"),
        ):
            if user is None:
                await inter.channel.send("Specify a user to ban.")
                return

            embed = disnake.Embed(
                description=(
                    f"✅ **{user.display_name}#{user.discriminator} had been unbanned"
                ),
                color=disnake.Color.green(),
            )
            await inter.channel.send(embed=embed)
            await user.unban()

        class kick(commands.Cog):
            def __init__(self, bot: commands.Bot):
                self.bot = bot

            @commands.slash_command(description = "Kick user from the Server.")
            async def kick(
                self,
                inter: disnake.ApplicationCommandInteraction,
                user: disnake.User = Param(None, desc = "Specify a user"),
                reason: str = Param(None, desc = "Provide a reason"),
            ):
                if user is None:
                    await inter.channel.send("Specify a user to kick.")
                    return
                embed = disnake.Embed(
                    description = (
                        f"✅ **{user.display_name}#{user.discriminator} is kicked!"
                        ),
                        color = disnake.Color.red(),
                )   
                # await inter.send(user.name + "have been kicked!"),
                await inter.channel.send(embed=embed)
                await disnake.guild.kick(reason=reason)
    
        class mute(commands.Cog):
            def __init__(self, bot):
                self.bot = bot

                # Timed mute this format: 1d, 20s, 30m, etc..
                @commands.slash_command(description="Mute specified user.")
                async def mute(
                    self,
                    inter: disnake.ApplicationCommandInteraction,
                    user: disnake.User = Param(None, desc="Specify a user"),
                    time: int = Param(None, desc="Specify a time."),
                    reason: str = Param(None, desc="Provide a reason"),
                ):
                    role = disnake.utils.get(inter.guild.roles, name="Muted")
                    time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
                    mute_time = int(time[0]) * time_convert[time[-1]]
                    await user.add_roles(role)
                    embed = disnake.Embed(
                        description=f"✅ **{user.display_name}#{user.discriminator} muted successfuly**",
                        color=disnake.Color.green(),
                    )
                    # TODO: change send embed method.
                    await inter.channel.send(embed=embed)
                    await asyncio.sleep(mute_time)
                    await user.remove_roles(role)
    
        class timeout(commands.Cog):
            def __init__(self, bot):
                self.bot=bot

            @commands.slash_command(description="Timeout specified user.")
            async def timeout(
                self,
                inter: disnake.ApplicationCommandInteraction,
                user: disnake.User = Param(None, desc="Specify a user"),
                time: str = Param(choices={"60s": "60", "5m": "300s", "10m": "600s", "1h": "3600s", "24h": "86400s", "1w": "604800s"}),
                reason: str=Param(None, desc="Provide a reason."),
            ):
                time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
                timeout_time=int(time[0]) * time_convert[time[-1]]
                embed=disnake.Embed(
                    color=disnake.Color.green(),
                )

        await inter.channel.send(embed=embed)
        await user.timeout(duration=timeout_time, reason=reason)
