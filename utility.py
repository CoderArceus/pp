import random
import discord
from discord.ext import commands

# Random Color Generator (0-255)
def randomColor():
    randColor = lambda: "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return randColor