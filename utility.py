import random
import discord
from discord.ext import commands

# Random Color Generator (0-255)
def randomColor():
    randColor = '#{:06x}'.format(randint(0, 256**3))
    print(randColor)
    return randColor