import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import aiohttp

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
#logger.addHandler(handler)

game = discord.Streaming(name='Arty - Study LOFI', url='https://www.youtube.com/watch?v=5qap5aO4i9A',
                         game='U cazz, devo studiare')

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=';', intents=intents,help_command=None)
        #https://gist.github.com/Rapptz/6706e1c8f23ac27c98cee4dd985c8120#extcommands-breaking-changes
    
    async def on_ready(self):
        await bot.change_presence(status=discord.Status.idle, activity=game)
        

    async def setup_hook(self):
        print('Il bot è pronto e funzionante.')
        print(bot.user)
        print('------')
        for filename in os.listdir('./cog'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.tree.sync(guild=discord.Object(id=383386139333230592))

bot = MyBot()
bot.run(os.getenv('TOKEN'),log_handler=handler)








    
    
    


