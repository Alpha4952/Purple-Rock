import discord
from discord.ext import commands
from discord import app_commands
from datetime import timedelta
import asyncio

class Post_create_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_create(self, thread):
        if thread.parent.name == 'support':
            reply = f'Hi {thread.owner.mention}, your issue has been registered.\n<@810760173907738655> is getting here'

            embed = discord.Embed(title='Please wait',
                      description='Be patient and do not mention anyone. Your issue will be handled shortly',
                      colour=0xa6e3a1)

            await thread.send(reply)
            #await thread.send(embed=embed)

        if thread.parent.name == 'request':
            reply = f'Hi {thread.owner.mention}, your request has been registered.\n<@810760173907738655> is getting here'

            embed = discord.Embed(title='Please wait',
                      description='Be patient and do not mention anyone. Your request will be handled shortly',
                      colour=0xa6e3a1)

            await thread.send(reply)
            #await thread.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Post_create_message(bot))