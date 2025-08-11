import discord
from discord.ext import commands

class Solved(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name='solved', description='Mark a post as solved')
    async def _solved(self, ctx: commands.Context):
        if str(ctx.channel.type) == 'public_thread' or str(ctx.channel.type) == 'private_thread':
            thread = ctx.channel

            if thread.parent.name == 'support':
                available_tags = thread.parent.available_tags
                solved_tag = [tag for tag in available_tags if tag.id == 1404351321187815444][0]
                await thread.add_tags(solved_tag)

                await thread.edit(locked=True)

                await thread.send(':white_check_mark: Issue archived!')

            if thread.parent.name == 'request':
                await thread.edit(locked=True)

                await thread.send(':white_check_mark: Request archived!')
        else:
            await ctx.channel.send('This is not a thread')

async def setup(bot):
    await bot.add_cog(Solved(bot))