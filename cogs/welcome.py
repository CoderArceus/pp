import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')
        
    async def on_member_join(self, member):
        channel = await bot.fetch_channel('1136495497645936793')
        await channel.send(f"Whalecum {member.mention}! Hope you enjoy your stay here. Dont forget to take self roles.")
 
async def setup(bot):
   await bot.add_cog(Welcome(bot))