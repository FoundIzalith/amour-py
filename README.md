# amour-py

amour-py is a Discord bot I made in my spare time for fun. 

She lives in my D&D group and is based on a character I played some years ago. 

Originally, Amour was written in C#, but I lost her code a long time ago and I decided to recreate her in Python so that I could learn the language. 

## Commands
Commands can be invoked with the prefix **$ amour**. Make sure to include a space between the prefix and the command. Commands include:
- greeting. Say hi to Amour
- wikipedia. Get random Wikipedia article
- books. Sends a random book recommendation
- suggest. Give Amour a suggestion and she will save it to a file 
- wiki. Search dndwiki.io  
- deathcount. Get number of times Jackson has died in a given game

## Dependencies 
Amour requires the following packages in order to fully function:
- Discord.py
- Requests
- BeautifulSoup 

## Installation
To install and run Amour, install Python3, and then install all necessary packages using **pip**. 

Go to https://discord.com/developers and create a new bot. Copy the token and invite the bot to your server. In the data folder, create a new file titled "atoken.py"

In atoken.py, put the following line:
``` TOKEN = "{yourToken}"```

Replace {yourToken} with the token you generated on the Discord developer portal. 

In amisc.py, replace the HOME variable with the ID of your server's general or bot channel. 

Open a terminal and run ```python amour.py``` 