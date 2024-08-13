import discord
from discord.ext import commands
import random
from discord import Spotify

class ChatCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
        
#chat commands start here ->

    @commands.command(aliases=['hi'])
    async def hello(self, ctx):
        await ctx.send('hello!!')
        
    @commands.command()
    async def roast(self, ctx, member: discord.Member=None):
    	if member==None:
    	    await ctx.reply("you wanna grill yourself lil bro?")
    	else:
        	await ctx.send(f'when girls call {member.mention} smooth, they probably mean their brain')
            
    @commands.command()
    async def howlong(self, ctx, member: discord.Member=None):
        ppsize=random.randint(-3, 11)
        if member==None:
            await ctx.reply(f"{ctx.message.author.mention}'s dingus is {ppsize} inches... *oh my*..")
        else:
            await ctx.reply(f"{member.mention}'s dingus is {ppsize} inches... *oh my*..")
            
    @commands.command()
    async def spotify(self, ctx, *, user: discord.Member=None):
    
        user = user or ctx.author
        if user.activities:
            for activity in user.activities:
                if isinstance(activity, Spotify):
                    await ctx.reply(f"`{user}` is listening to `{activity.title}` by `{activity.artist}` → [Song Link]({activity.track_url})")
        else:
            await ctx.reply(f"`{user}` aint listening no shit")
        
async def setup(bot):
   await bot.add_cog(ChatCommands(bot))