import os
from datetime import date
from discord.ext import commands
from .utils.dataIO import dataIO

__author__ = "Pwnulatr"
__version__ = "2.0.1"


class Outagetally:
    """A joke tally counter for the amount of times my internet goes out"""

    def __init__(self, bot):
        self.bot = bot
        self.file_path = "data/pwning-cogs/outagecounter/tally.json"
        self.settings = dataIO.load_json(self.file_path)

    @commands.command(no_pm=False, pass_context=True)
    async def internetwentout(self, ctx):
        """Just adds one to the tally"""

        user = ctx.message.author.id
        date_today = date.today()
        await self.bot.type()
        if user not in self.settings:
            self.settings[user] = {}
            self.settings[user]["Tally"] = 1
            self.settings[user]["Last Outage"] = f"{date_today}"
            dataIO.save_json(self.file_path, self.settings)
            await self.bot.reply(f"This appears to be your first outage on record.")
        elif user in self.settings:
            current_tally = self.settings[user]['Tally']
            add_to_tally = current_tally + 1
            self.settings[user]["Tally"] = add_to_tally
            self.settings[user]["Last Outage"] = f"{date_today}"
            dataIO.save_json(self.file_path, self.settings)
            await self.bot.reply(f"Logged! You're currently at {add_to_tally} outages!")
        else:
            await self.bot.reply("Something went wrong.")

    @commands.command(no_pm=False, pass_context=True)
    async def howmanytimes(self, ctx):
        """Says what the current tally is"""

        await self.bot.type()
        user = ctx.message.author.id
        tallycount = self.settings[user]['Tally']
        await self.bot.reply(f"You've had {tallycount} outages so far!")


def check_folders():
    tally_folder = "data/pwning-cogs/outagecounter"
    if not os.path.exists(tally_folder):
        print("Creating outage counter folder...")
        os.makedirs(tally_folder)


def check_files():
    tally_path = "data/pwning-cogs/outagecounter/tally.json"
    if not dataIO.is_valid_json(tally_path):
        print("Creating empty tally.json...")
        dataIO.save_json(tally_path, {})


def setup(bot):
    check_folders()
    check_files()
    n = Outagetally(bot)
    bot.add_cog(n)
