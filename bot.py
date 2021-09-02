import disnake
import os

from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix = "ck.", intents = intents, 
                   test_guilds = [405738567902429244])

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(os.getenv('TOKEN'))
