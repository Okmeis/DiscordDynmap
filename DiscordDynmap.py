# author: Okmeis
# date: 18.10.2022
# version 1.0.0

import discord
from discord.ext import tasks, commands
import SecretSauce, DynmapDownloader
import DiscordDynmapConfig as Config
import os



#discord bot
bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())


#Post Image every x minutes
@tasks.loop(minutes=Config.repeatInMinutes)
async def send_again():
    await bot.wait_until_ready()
    dynmapImage = DynmapDownloader.getSection()
    imageChannel = bot.get_channel(Config.channelID)
    await imageChannel.purge()
    imagePath = "../DiscordDynmap/saves/"
    imageName = "dynmapPNG.png"
    if not os.path.isdir(imagePath):
        os.mkdir(imagePath)
    dynmapImage.save(imagePath+imageName,"PNG")
    with open(imagePath+imageName, "rb") as fh:
        f = discord.File(fh, filename=imagePath+imageName)
        await imageChannel.send(file=f)
    return


#Lets us know when ready
@bot.event
async def on_ready():
    print("Bot is ready!")
    send_again.start()


#Shutdown the bot if this command got used by a botadmin
@bot.command()
async def livemap(ctx, arg1):
    if arg1=="shutdown":
        if ctx.author.id in Config.botAdminIDs:
            await ctx.bot.close()
    return


bot.run(SecretSauce.getSauce("ketchup", "s3Nf"))