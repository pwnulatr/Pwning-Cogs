# YouTube Thumbnail extraction script for Red
# Coded by Pwnulatr
from discord.ext import commands
import urllib.request
import os
import asyncio

class YoutubeThumbnail:
    """Gives you a HQ thumbnail from a YouTube link you provide"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, pass_context=False)
    async def thumbnail(self, ctx):
        """Supply a Youtube link to get the Thumbnail"""

        url = ctx
        image = url.rsplit('=',1)[1]
        thumbnaillink = "https://img.youtube.com/vi/" + image + "/maxresdefault.jpg"

        urllib.request.urlretrieve(thumbnaillink, "data/youtubethumbnail/cache/" + image + ".jpg")
        #await asyncio.sleep(1)
        #await self.bot.send_file(ctx.message.channel, "data/youtubethumbnail/cache/" + image + ".jpg")
        await self.bot.say(thumbnaillink)

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
