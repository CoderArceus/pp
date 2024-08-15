import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
        
    @commands.command(aliases=["rj"])
    async def rejoin(self, ctx, user: discord.Member=None):
        
        user = user or ctx.author
        
        if user.flags.did_rejoin==True:
            await ctx.reply(f'`{user}` HAS rejoined the server.')
        else:
            await ctx.reply(f'`{user}` HAS NOT rejoined the server.')
 
async def setup(bot):
   await bot.add_cog(Moderation(bot))