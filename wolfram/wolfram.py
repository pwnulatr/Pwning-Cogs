from __main__ import send_cmd_help
from discord.ext import commands
from .utils.dataIO import dataIO
from cogs.utils import checks
from urllib.parse import quote_plus
import aiohttp
import os

__author__ = "Pwnulatr"
__version__ = "0.1.2"

PATH = "data/pwning-cogs/wolfram/"
JSON = PATH + "settings.json"
key_filter = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-")


class Wolfram:
    """Ask the Wolfram Computation Knowledge Engine anything"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json(JSON)
        self.root_api_url = "http://api.wolframalpha.com/v1/result?appid="

# =================================GROUP DEFINE================================
    @commands.group(pass_context=True)
    async def wolframsettings(self, ctx):
        """Settings for the Wolfram Alpha Cog"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

# =============================================================================
    @commands.cooldown(1, 10, commands.BucketType.user)
    @wolframsettings.command(name="setapikey", pass_context=True)
    @checks.is_owner()
    async def _setapikey_wolframsettings(self, ctx, key: str):
        """Set your Wolfram API key"""

        await self.bot.type()
        sid = ctx.message.server.id
        char_key = list(key)

        for c in char_key:
            if c not in key_filter:
                await self.bot.say("Invalid character detected:\nMake sure you"
                                   " have copied your key correctly.")
                return

        if len(key) is 17:
            test = self.root_api_url + key + "&i=test"
            async with aiohttp.get(test) as r:
                data = await r.text()
            if data != "Error 1: Invalid appid":
                self.settings[sid] = key
                dataIO.save_json(JSON, self.settings)
                await self.bot.say("API Key has been set.")
            else:
                await self.bot.say("You have not entered a valid API key.")
        else:
            await self.bot.say("You have not entered a valid API key.")

    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.command(name="wolfram", no_pm=True, pass_context=True)
    async def wolfram(self, ctx, *, query: str):
        """Queries the Wolfram API with user input"""

        await self.bot.type()
        sid = ctx.message.server.id
        if sid not in self.settings:
            await self.bot.say("The owner has not set their API Key.\n\n"
                               "You can get one from here:\n"
                               "https://developer.wolframalpha.com/portal/myapps/")
            return

        api_key = self.settings[sid]
        encoded_text = quote_plus(query)
        full_query = self.root_api_url + api_key + "&i=" + encoded_text

        async with aiohttp.get(full_query) as r:
            data = await r.text()

        await self.bot.say(data)


def check_folders():
    if not os.path.exists(PATH):
        print("Creating Wolfram Alpha folder...")
        os.makedirs(PATH)


def check_files():
    if not dataIO.is_valid_json(JSON):
        print("Creating Wolfram Alpha settings json...")
        dataIO.save_json(JSON, {})


def setup(bot):
    check_folders()
    check_files()
    n = Wolfram(bot)
    bot.add_cog(n)
