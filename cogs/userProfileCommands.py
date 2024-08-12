import discord
from discord.ext import commands
import random

class userProfileCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
		
    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member: discord.Member=None):
        if member==None:
            embedAvatarSelf = discord.Embed(title=ctx.message.author, color=discord.Color.random())
            userAvatar=ctx.message.author.avatar.url
            embedAvatarSelf.set_image(url=userAvatar)
            await ctx.reply(embed=embedAvatarSelf)
        else:
            embedAvatarOther = discord.Embed(title=member, color=discord.Color.random())
            userAvatar=member.avatar.url
            embedAvatarOther.set_image(url=userAvatar)
            await ctx.reply(embed=embedAvatarOther)
    
    @commands.command()
    async def banner(self, ctx, member: discord.Member=None):
        print("1")
        if member==None:
            print("2")
            user = await bot.fetch_user(ctx.message.author.id)
            print("3")
            embedBannerSelf = discord.Embed(title=ctx.message.author, color=discord.Color.random())
            print("4")
            userBanner=user.banner.url
            print("5")
            embedBannerSelf.set_image(url=userBanner)
            print("6")
            await ctx.reply(embed=embedBannerSelf)
        else:
            embedBannerOther = discord.Embed(title=member, color=discord.Color.random())
            userBanner=member.banner.url
            embedBannerOther.set_image(url=userBanner)
            await ctx.reply(embed=embedBannerOther)
		
async def setup(bot):
   await bot.add_cog(userProfileCommands(bot))