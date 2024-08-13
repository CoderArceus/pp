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
        if not user:
            member = ctx.author
        else:
            member = user
        
        userAvatar=member.avatar.url
        embedAvatar = discord.Embed(title=member, color=discord.Color.random())
        embedAvatar.set_image(url=userAvatar)
        
        await ctx.reply(embed=embedAvatar)

    
    @commands.command(name="banner", aliases=['b'])
    async def banner(self, ctx, *, user: discord.Member=None):
    
        if not user:
            member = ctx.author
        else:
            member = user
            
        fetchedMember = await self.bot.fetch_user(member.id)
        
        if fetchedMember.banner==None:
            await ctx.reply(f'`{fetchedMember}` got no nitro to have a banner, filthy peasant..')
        else:
            userBannerUrl = fetchedMember.banner.url
            embedBanner = discord.Embed(title=fetchedMember, color = discord.Color.random())
            embedBanner.set_image(url=userBannerUrl)
            await ctx.reply(embed=embedBanner)
		
async def setup(bot):
   await bot.add_cog(userProfileCommands(bot))