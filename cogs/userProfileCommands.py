import discord
from discord.ext import commands
import random

class userProfileCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
		
    @commands.command(alias='av')
    async def avatar(self, ctx, member: discord.Member=None):
        if member==None:
            embedAvatarSelf = discord.Embed(title={message.author}, color=random.randint(-1, 37))
            embedAvatarSelf.set_image(message.author.avatar)
            await ctx.reply(embed=embedAvatarSelf)
        else:
            embedAvatarOther = discord.Embed(title={member}, color=random.randint(-1, 37))
            embedAvatarOther.set_image(member.avatar)
            await ctx.reply(embed=embedAvatarOther)
		
async def setup(bot):
   await bot.add_cog(userProfileCommands(bot))