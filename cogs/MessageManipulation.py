import discord
from discord.ext import commands

class MessageManipulation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online!')

#message manipulation commands start here -> 

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.embeds:
            if before.author.bot:
                return
            else:
                await before.reply("can't you type properly once??")
        
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        member=message.author
        if message.author.bot:
        	return
        else:
        	await message.channel.send(f'{member.mention} fuk u hidin bih?')
            
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content=="good pp":
            await message.reply("Thanks :deer:")
        else:
            return
        
async def setup(bot):
   await bot.add_cog(MessageManipulation(bot))