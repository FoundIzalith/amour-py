# amour-py

amour-py is a Discord bot I made in my spare time for fun. 

She lives in my D&D group and is based on a character I played some years ago. 

Originally, Amour was written in C#, but I lost her code a long time ago and I decided to recreate her in Python so that I could learn the language. 

## Commands
Commands can be invoked with the prefix **$ amour**. Make sure to include a space between the prefix and the command. Commands include:
- Greeting. Say hi to Amour
- Wikipedia. Get random Wikipedia article
- Books. Sends a random book recommendation

## Depencies 
Amour requires the following packages in order to fully function:
- Discord.py
- Requests
- BeautifulSoup 

## Installation
To install and run Amour, install Python3, and then install all necessary packages using **pip**. 

Go to https://discord.com/developers and create a new bot. Copy the token. In the data folder, create a new file titles "atoken.py"

In atoken.py, put the following line:
``` TOKEN = "{yourToken}```

Replace {yourToken} with the token you generated on the Discord developer portal. 

Open a terminal and run **python amour.py** 