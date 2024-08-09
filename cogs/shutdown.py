import discord
from discord.ext import commands

class Shutdown(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
	
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
    
    @commands.command()
    @commands.is_owner()
    async def soja(self, ctx):
        await ctx.send("putting pp to sleep... done!")
        await ctx.bot.close()
        
async def setup(bot):
   await bot.add_cog(Shutdown(bot))