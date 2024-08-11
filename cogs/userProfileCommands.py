import discord
from discord.ext import commands
import random

class userProfileCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
		
    @commands.command(alias=av)
    async def avatar(self, ctx, member: discord.Member=None):
        if member==None:
            embedAvatarSelf = discord.Embed(title=ctx.message.author)
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