import discord
from discord.ext import commands
import os
import asyncio

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

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.command()
async def reload(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.reload_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'Reloaded {filename} Successfully.')
            print(f'Reloaded {filename} Successfully.')

async def main():
    async with bot:
        await load()
        await bot.start(token)
asyncio.run(main())