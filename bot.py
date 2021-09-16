import disnake
import os
import platform
import logging

from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="ck.", intents=intents,
                   test_guilds=[872470314171392001])

# Logging the disnake for verbose
logger = logging.getLogger('disnake')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='disnake.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Get the modules of all cogs whose directory structure is cogs/<module_name>/cog.py
for folder in os.listdir("cogs"):
    if os.path.exists(os.path.join("cogs", folder, "cog.py")):
        bot.load_extension(f"cogs.{folder}.cog")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")
    print(f"Disnake.py API version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")


bot.run(os.getenv("TOKEN"))
