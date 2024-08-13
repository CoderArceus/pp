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
    async def avatar(self, ctx, *, user: discord.Member=None):
    
        user = user or ctx.author
        userAvatar=user.display_avatar.url
        embedAvatar = discord.Embed(title=user, color=discord.Color.random())
        embedAvatar.set_image(url=userAvatar)
        
        await ctx.reply(embed=embedAvatar)

    
    @commands.command()
    async def banner(self, ctx, *, user: discord.Member=None):
    
        user = user or ctx.author
            
        fetchedUser = await self.bot.fetch_user(user.id)
        
        if fetchedUser.banner==None:
            await ctx.reply(f'`{fetchedUser}` got no nitro to have a banner, filthy peasant..')
        else:
            userBannerUrl = fetchedUser.banner.url
            embedBanner = discord.Embed(title=fetchedUser, color = discord.Color.random())
            embedBanner.set_image(url=userBannerUrl)
            await ctx.reply(embed=embedBanner)
		
async def setup(bot):
   await bot.add_cog(userProfileCommands(bot))