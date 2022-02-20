import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix=';')
game = discord.Streaming(name='Arty - Study LOFI', url='https://www.youtube.com/watch?v=5qap5aO4i9A',
                         game='U cazz, devo studiare')



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=game)
    print('Il bot è pronto e funzionante.')
    print(client.user)
    print('------')
    #commands.Bot.get_cog(name="wordle.py")


# check if there is a .py inside the cogs directory and load it
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
       client.load_extension(f'cogs.{filename[:-3]}')

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client.run(os.getenv('TOKEN'))
