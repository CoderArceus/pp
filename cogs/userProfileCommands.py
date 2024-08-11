import discord
from discord.ext import commands
import random

class userProfileCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
		
    @commands.command()
    async def avatar(self, ctx, member: discord.Member=None):
        print('1')
        if member==None:
            print('2')
            embedAvatarSelf = discord.Embed(title=f'{ctx.message.author}')
            print('3')
            userAvatar=ctx.message.author.avatar_url
            print('4')
            embedAvatarSelf.set_image(userAvatar)
            print('5')
            await ctx.reply(embed=embedAvatarSelf)
        else:
            embedAvatarOther = discord.Embed(title=f'{member}')
            embedAvatarOther.set_image(member.avatar_url)
            await ctx.reply(embed=embedAvatarOther)
		
async def setup(bot):
   await bot.add_cog(userProfileCommands(bot))