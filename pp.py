import discord
from discord.ext import commands
import os
import asyncio
import sys

intents = discord.Intents.default()
intents.message_content = True
intents.messages=True
intents.members = True

bot=commands.Bot(command_prefix="pp ", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

with open("token.txt") as file:
    token=file.read()

#loading modules and starting bot

extensions = [
    'cogs.mod_commands',
]
if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Error loading the {extension}", file=sys.stderr)
            traceback.print_exc()

@bot.command()
@commands.is_owner()
async def reload(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.reload_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'Reloaded {filename} Successfully.')
            print(f'Reloaded {filename} Successfully.')

async def main():
    async with bot:
        await bot.start(token)
asyncio.run(main())