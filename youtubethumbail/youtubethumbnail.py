# YouTube Thumbnail extraction script for Red
# Coded by Pwnulatr
from discord.ext import commands
import urllib.request
import os
from .utils.dataIO import fileIO

class YoutubeThumbnail:
    """Gives you a HQ thumbnail from a YouTube link you provide"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)

    async def thumbnail(self, videourl):
        """Supply a Youtube link to get the Thumbnail"""

        if len(videourl) > 0: #If there is no link supplied

            url = str(videourl)
            image = url.rsplit('=',1)[1]
            thumbnaillink = "https://img.youtube.com/vi/" + image + "/maxresdefault.jpg"

            urllib.request.urlretrieve(thumbnaillink, "data/youtubethumbnail/cache/" + image + ".jpg")

            await self.bot.say(thumbnaillink)
        else:
            await self.bot.say("Please supply a YouTube link")

def check_folders():
    folders = ("data", "data/youtubethumbnail/cache/")
    for folder in folders:
        if not os.path.exists(folder):
            print("Creating " + folder + " folder...")
            os.makedirs(folder)


def setup(bot):
    check_folders()
    n = YoutubeThumbnail(bot)
    bot.add_cog(n)
