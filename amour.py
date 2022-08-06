
import discord
import random 
import os
import webbrowser 
import requests 

from bs4 import BeautifulSoup
from data.alists import GREETING, RECOMMENDATION, BOOKS
from data.atoken import TOKEN

from discord.ext import commands

client = commands.Bot(command_prefix="$ amour ")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    burrowGeneral = client.get_channel(374098163516309505)
    print(burrowGeneral.name)

    #await burrowGeneral.send(random.choice(GREETING))    

@client.command(name='greeting', help='Says hello')
async def greeting(ctx):
    print('Command: greeting')
    response = random.choice(GREETING)
    await ctx.send(response)

@client.command(name='wikipedia', help='Sends a random Wikipedia article')
async def wikipedia(ctx):
    print('Command: wikipedia')
    article = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    print(article.url)
    parsed = BeautifulSoup(article.content, "html.parser")
    title = parsed.find(class_="firstHeading").text
    response = "Check out this article on " + title + "! " + article.url
    await ctx.send(response)

@client.command(name='books', help='Recommends a random book')
async def books(ctx):
    print('Command: books')
    response = random.choice(RECOMMENDATION) + random.choice(BOOKS)
    await ctx.send(response)

client.run(TOKEN)

