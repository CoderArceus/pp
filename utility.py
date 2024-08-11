from random import randint
import discord
from discord.ext import commands

# Random Color Generator (0-255)
async def randomColor():
    randColor = tuple(map(randint, [0]*3, [255]*3))