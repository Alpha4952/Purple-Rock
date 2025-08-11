import logging
import time
from pytz import timezone
from datetime import datetime

logging.Formatter.converter = lambda *args: datetime.now(tz=timezone('Asia/Bangkok')).timetuple()
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
)

import discord
import asyncio
from discord.ext import commands
from discord import app_commands
import os

bot = commands.Bot(command_prefix='_', intents=discord.Intents.all())

with open('cogs.txt' , 'r') as f:
    cogs_list = f.readlines()

with open('commands.txt', 'r') as f:
    commands_list = f.readlines()

class MyBot(commands.Bot):
    @bot.event
    async def on_ready():
        bot.tree.clear_commands(guild=discord.Object(id=1404219300658811001))

        for cog in cogs_list:
            await bot.load_extension(f'cogs.{cog}'[:-1])
            logging.info(f'Loaded cogs.{cog}'[:-1])

        for command in commands_list:
            await bot.load_extension(f'commands.{command}'[:-1])
            logging.info(f'Loaded commands.{command}'[:-1])

        #bot.tree.copy_global_to(guild=discord.Object(id=1404219300658811001))
        await bot.tree.sync(guild=discord.Object(id=1404219300658811001))

        logging.info(f'Logged on as {bot.user}!')

from dotenv import load_dotenv
load_dotenv()
token = os.getenv('token')

bot.run(token)