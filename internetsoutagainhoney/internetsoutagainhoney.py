import os
from discord.ext import commands
from .utils.dataIO import dataIO
from cogs.utils import checks

class Internetsoutagain:
    """A joke tally counter for the amount of times my internet goes out"""
    def __init__(self, bot):
        self.bot = bot
        self.file_path = "data/internetcounter/tally.json"
        self.settings = dataIO.load_json(self.file_path)

    @commands.command(no_pm=False)
    @checks.is_owner()
    async def internetwentout(self):
        """Just adds one to the tally"""

        tallycount = self.settings["TALLYCOUNT"]
        writetotally = tallycount + 1
        self.settings["TALLYCOUNT"] = writetotally
        dataIO.save_json(self.file_path, self.settings)
        await self.bot.say("Anotha one. Currently at {} outages.".format(writetotally))

    @commands.command(no_pm=False)
    @checks.is_owner()
    async def howmanytimes(self):
        """Says what the current tally is"""

        tallycount = self.settings["TALLYCOUNT"]
        await self.bot.say("Current number of outages are `{}`".format(tallycount))

def check_folders():
    if not os.path.exists("data/internetcounter"):
        print("Creating data/internetcounter folder...")
        os.makedirs("data/internetcounter")

def check_files():
    settings = {"TALLYCOUNT" : 0}
    if not dataIO.is_valid_json("data/internetcounter/tally.json"):
        print("Creating empty tally.json...")
        dataIO.save_json("data/internetcounter/tally.json", settings)

def setup(bot):
    check_folders()
    check_files()
    n = Internetsoutagain(bot)
    bot.add_cog(n)
