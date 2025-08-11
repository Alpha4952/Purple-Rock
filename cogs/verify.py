import discord
from discord.ext import commands
from discord import app_commands
from datetime import timedelta
import asyncio

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 1404344092707655803:
            guild = self.bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            if str(payload.emoji) == "✅":
                role = discord.utils.get(guild.roles, id = 1404326116335943702)
                await member.add_roles(role)
        
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 1404344092707655803:
            guild = self.bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            if str(payload.emoji) == "✅":
                role = discord.utils.get(guild.roles, id = 1404326116335943702)
                await member.remove_roles(role)

async def setup(bot):
    await bot.add_cog(Verify(bot))