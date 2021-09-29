import disnake
import os
import platform
import logging

from logging.handlers import TimedRotatingFileHandler
from disnake.ext import commands
from dotenv import load_dotenv
from util.db import create_connection, setup_tables

if os.name != "nt":
    import uvloop

    uvloop.install()

load_dotenv()
intents = disnake.Intents.all()
bot = commands.Bot(
    command_prefix="ck.",
    intents=intents,
    test_guilds=[872470314171392001],
    sync_commands_debug=True,
)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")
    print(f"Disnake.py API version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("----------------------------------")


def setup_logging():
    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("disnake")
    logger.setLevel(logging.INFO)
    log_dir = "logs"
    handler = TimedRotatingFileHandler(
        os.path.join(log_dir, "cookiebot.log"), "midnight", interval=1
    )
    handler.suffix = "%Y-%m-%d_%H-%M-%S"
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)
    return logger


logger = setup_logging()

if not os.path.isfile(r"sqlite.db"):
    conn = create_connection(r"sqlite.db")
    setup_tables(conn)

print("Cogs Loaded" + "\n")
for folder in os.listdir("cogs"):
    if os.path.exists(os.path.join("cogs", folder, "cog.py")):
        bot.load_extension(f"cogs.{folder}.cog")

logger.info("Starting Bot")
bot.run(os.getenv("TOKEN"))
logger.info("------ BOT STARTED -------")
