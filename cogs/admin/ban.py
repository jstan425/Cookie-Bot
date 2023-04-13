import disnake, asyncio, datetime
import re
import pytz

from disnake.ext import commands, tasks
from disnake.ext.commands import Param
from datetime import datetime, timedelta
from util.db import *

time_pattern = re.compile(r'^(\d+)([smhd])$')

match = time_pattern.match(time)
if not match:
    await inter.channel.send("Provide the correct time format.")
else:
    amount, unit = match.groups()
    ban_time = int(amount) * time_convert[unit]
    
class Ban(commands.Cog):
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
            color=disnake.Color.red(),
        )
        await inter.channel.send(embed=embed)
        await user.ban(user, reason=reason)

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

    @commands.slash_command(description="Tempban user from the server.")
    async def tempban(
        self,
        inter: disnake.ApplicationCommandInteraction,
        user: disnake.User = Param(None, desc="Specify a user"),
        time: str = Param(None, desc="Specify a time"),
        reason: str = Param(None, desc="Provide a reason"),
    ):
        time_convert = {"s": 1, "m": 60, "h": 3600, "d": 86400}
        ban_time = int(time[0]) * time_convert[time[-1]]
        end_time = datetime.now() + timedelta(seconds=ban_time)
        embed = disnake.Embed(
            description=(
                f"✅ **{user.display_name}#{user.discriminator} had been tempban for {time} successfully**"
            ),
            color=disnake.Color.green()
        member = inter.guild.get_member(user.id)
        if not member:
            await inter.channel.send("Specift a user to tempban")
        else:
            await user.ban(reason=reason)
        await inter.response.send_message(embed=embed)
        await asyncio.sleep(ban_time)
        await user.unban(user)
        )

        conn = create_connection(r"sqlite.db")
        sql = f" INSERT INTO temp_ban(guild_id,user_id,end_time) VALUES({inter.guild.id},{user.id},{end_time.timestamp()}) "
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        

    # TODO change this to how often you want this to run, i'd suggest every minute
    @tasks.loop(minutes=1.0)
    async def temp_ban_checker(self):
        conn = create_connection(r"sqlite.db")
        timestamp_now = datetime.now().timestamp()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM temp_ban WHERE end_time < {timestamp_now}")
        rows = cur.fetchall()
        for row in rows:
            selected_guild = self.bot.get_guild(row[1])
            bans = await selected_guild.bans()
            for ban in bans:
                if row[2] == ban.user.id:
                    print (f"unbanning {ban.user}")
                    await selected_guild.unban(ban.user)

    @temp_ban_checker.before_loop
    async def before_printer(self):
        print("waiting...")
        await self.bot.wait_until_ready()
