import discord
from discord.ext import commands

class ChatCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
        
#chat commands start here ->

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hello!!')

async def setup(bot):
   await bot.add_cog(ChatCommands(bot))