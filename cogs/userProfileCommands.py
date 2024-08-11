import discord
from discord.ext import commands
import random
from utility import randomColor

class userProfileCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
		
    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member: discord.Member=None):
        if member==None:
            embedAvatarSelf = discord.Embed(title=ctx.message.author, color=randomColor())
            userAvatar=ctx.message.author.avatar.url
            embedAvatarSelf.set_image(url=userAvatar)
            await ctx.reply(embed=embedAvatarSelf)
        else:
            embedAvatarOther = discord.Embed(title=member)
            userAvatar=member.avatar.url
            embedAvatarOther.set_image(url=userAvatar)
            await ctx.reply(embed=embedAvatarOther)
		
async def setup(bot):
   await bot.add_cog(userProfileCommands(bot))