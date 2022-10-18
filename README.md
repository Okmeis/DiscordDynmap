# DiscordDynmap
## Purpose
Display A Selected Area Of Your Minecraft Servers Map On Discord every X minutes.
<br/>
<br/>Feel free to modify it however you like and host it on your own discord server.
<br/>I have nothing to do with the developer/s of dynmap, I just appreciate their plugin and thought it would be nice if minecraft players or communities could see their map/s in an extra discord channel.

## Requirements
- a with `discord.py` compatible version of Python and other imports which are listed `DynmapDownloader.py` and `DiscordDynmap.py`
- a minecraft server with a working dynmap plugin
- a discord application you can connect it to. If you don't have one, you can create one here: https://discord.com/developers/applications
<br/>Example: The bot got tested under following requirements:
- Python 3.7.4 for the discord bot
- Plugin `Dynmap-3.3.2-spigot.jar` on a minecraft server for 1.18.1

## Getting started
After installing the required software and setting up a discord bot application with all required intents and permissions and after adding it to your discord server, open `DiscordDynmapConfig.py` and change the settings to your needs. For that I recommend reading the comments inside of the file to understand how set the variables. When  everything is done, either open `DiscordDynmap.py` and replace `SecretSauce.getSauce("ketchup", "s3Nf")` by your bots authentification code in the last line of the file or change the parameters and write your own `SecretSauce.py`.
<br/>If you've done everything right you can open your terminal in the directory the python files are in and start the bot by typing `python DiscordDynmap.py`, consider that it will take a while until the bot downloaded and combined all image fragments. To stop the bot, simply write `!livemap shutdown` into a channel the bot can read.


## Attention!
Please read the warning in the comment above channelID in `DiscordDynmapConfig.py`.
