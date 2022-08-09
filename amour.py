
import discord
import random 
import os
import webbrowser 
import requests 

from bs4 import BeautifulSoup
from data.alists import GREETING, RECOMMENDATION, BOOKS
from data.atoken import TOKEN
from data.amisc import HOME 
from random import randrange 

from discord.ext import commands

client = commands.Bot(command_prefix="$ amour ")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    general = client.get_channel(HOME)

    #await general.send(random.choice(GREETING))    

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

@client.command(name='suggest', help='Give a suggestion')
async def suggest(ctx, *args):
    print('Command: suggest')

    try:
        suggestionFile = open("data/suggestions.txt", "a")
    except: 
        print('Failed to open suggestions.txt')
        await ctx.send("[ERROR] I can't find my notebook!")
        return 

    try: 
        content = ""

        for item in args:    
            content = content + " " + item

        suggest = "Suggestion by " + ctx.author.name + " in " + ctx.guild.name + ": " + content + "\n"
        suggestionFile.write(suggest)
        await ctx.send("Acknowledged and saved.")
    except:
        print('Suggest failed to write')
        await ctx.send("[ERROR] Your suggestion sucks and I'm not taking it.")
        return 

@client.command(name='wiki', help="Searches for D&D rules for you")
async def wiki(ctx, *args):
    search = ""
    for item in args:
        search = search + item + "+"

    print('Command: wiki ' + search)

    await ctx.send("Sure, I'll take a look for you.")

    query = requests.get("https://www.dndwiki.io/search?query=" + search)
    parsed = BeautifulSoup(query.content, "html.parser")
    
    results = []

    for link in parsed.find_all('a', class_='search-result-title', limit=3):
        print(link)
        result = link.get('href')
        print(result)
        results.append("https://www.dndwiki.io" + result)
    
    await ctx.send("Here's what I found:")
    await ctx.send(results[0])
    await ctx.send(results[1])
    await ctx.send(results[2])
    
@client.command(name='github', help='github')
async def github(ctx):
    print('Command: github')
    await ctx.send("https://github.com/FoundIzalith/amour-py")
            
@client.command(name='deathcount', help='Display Jackson\'s deathcount')
async def deathcount(ctx, *args):
    print('Command: deathcount')

    rand1 = randrange(5000)
    rand2 = randrange(5000)
    rand = rand1 + rand2

    game = ""

    for item in args:
        game = game + item + " "

    await ctx.send("Jackson has died " + str(rand) + " times in " + game)


def main():
    client.run(TOKEN)

if __name__ == '__main__':
    main()
