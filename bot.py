import disnake
import os
import platform
import logging

from logging.handlers import TimedRotatingFileHandler
from disnake.ext import commands
from dotenv import load_dotenv

if os.name != "nt":
    import uvloop

    uvloop.install()

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
    print("----------------------------------")

logger = logging.getLogger("disnake")
logger.setLevel(logging.INFO)
log_dir = "logs"
handler = TimedRotatingFileHandler(
    os.path.join(log_dir, "opentorn-bot.log"), "midnight", interval=1)
handler.suffix = "%Y-%m-%d_%H-%M-%S"
handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
logger.addHandler(handler)

print("Cogs Loaded")
for folder in os.listdir("cogs"):
    if os.path.exists(os.path.join("cogs", folder, "cog.py")):
        bot.load_extension(f"cogs.{folder}.cog")

logger.info("Starting Bot")
bot.run(os.getenv("TOKEN"))