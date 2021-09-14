import disnake
import os
import platform

from disnake.ext import commands
from dotenv import load_dotenv

from cogs.mods import Mods

load_dotenv()
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="ck.", intents=intents,
                   test_guilds=[872470314171392001])

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")
    print(f"Disnake.py API version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

bot.add_cog(Mods(bot))

bot.run(os.getenv("TOKEN"))
