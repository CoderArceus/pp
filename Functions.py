from random import randint
import discord
from discord.ext import commands

# Random Color Generator (0-255)
async def randomColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    randColor = (r, g, b)