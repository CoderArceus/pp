import discord
from discord.ext import commands
import os
import asyncio
import logging

intents = discord.Intents.default()
intents.message_content = True
intents.messages=True
intents.members = True

bot=commands.Bot(command_prefix=["pp ", "Pp ", "PP ", "pP "], intents=discord.Intents.all())

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
@commands.is_owner()
async def reload(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.reload_extension(f'cogs.{filename[:-3]}')
            await ctx.send(f'Reloaded {filename} Successfully.')
            print(f'Reloaded {filename} Successfully.')

#LOGGING

logging.basicConfig(level=logging.INFO)


async def main():
    async with bot:
        await load()
        await bot.start(token)
asyncio.run(main())