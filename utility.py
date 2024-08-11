import random
import discord
from discord.ext import commands

# Random Color Generator (0-255)
def randomColor():
    randColor = "%06x" % random.randint(0, 0xFFFFFF)
    return randColor