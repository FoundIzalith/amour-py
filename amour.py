
import discord
import random 
import os

from data.a-lists import GREETING
from data.a-token import TOKEN

from discord.ext import commands

client = commands.Bot(command_prefix="$ amour ")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    burrowGeneral = client.get_channel(374098163516309505)
    print(burrowGeneral.name)

    await burrowGeneral.send(random.choice(GREETING))    

@client.command(name='help', help='Provides a list of commands')
async def help(ctx):
    print('Command: help')
    response = 'Available commands: help, greeting.'
    await ctx.send(response)

@client.command(name='greeting', help='Says hello')
async def greeting(ctx):
    print('Command: greeting')
    response = random.choice(GREETING)
    await ctx.send(response)

client.run(TOKEN)

