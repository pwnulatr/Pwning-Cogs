# Coded by Pwnulatr with the help of many cogs that came with Red
from discord.ext import commands
from __main__ import send_cmd_help
from .utils.dataIO import dataIO
from datetime import date
from cogs.utils import checks
import discord
import os
import time

__author__ = "Pwnulatr"
__version__ = "1.1"

monthname = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"}

class Datestatustimer:
    """Calculates the time between dates and makes it the bot \"playing\" status"""

    def __init__(self, bot):
        self.bot = bot
        self.file_path = "data/pwning-cogs/datestatustimer/settings.json"
        self.settings = dataIO.load_json(self.file_path)
        self.last_check = None

#================================GROUP DEFINE==================================
    @commands.group(pass_context=True)
    async def datestatus(self, ctx):
        """These are the settings for the date status cog"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
#==============================================================================
    @datestatus.command(name="date", pass_context=True)
    @checks.is_owner()
    async def _date_datestatus(self, ctx, month:int, day:int):
        """Set the date for countdown"""
        monthrange = list(range(1, 13))
        dayrange = list(range(1,32))
        thirty_month = [4, 6, 9, 11]

        if month in monthrange and day in dayrange:
            if month == 2 and day <= 28:
                self.settings["MONTH_NUMBER"] = month
                self.settings["DAY_NUMBER"] = day
                dataIO.save_json(self.file_path, self.settings)
                await self.bot.say("Date set to {} of {}".format(day, monthname[month]))
            elif monthnumber in thirty_month and day <= 30:
                self.settings["MONTH_NUMBER"] = month
                self.settings["DAY_NUMBER"] = day
                dataIO.save_json(self.file_path, self.settings)
                await self.bot.say("Date set to {} of {}".format(day, monthname[month]))
            elif month == 2 and day >= 29:
                await self.bot.say("You have not entered a valid date.\nBe sure it is formatted as `month/day`")
            else:
                self.settings["MONTH_NUMBER"] = month
                self.settings["DAY_NUMBER"] = day
                dataIO.save_json(self.file_path, self.settings)
                await self.bot.say("Date set to {} {}".format(monthname[month], day))
        else:
            await self.bot.say("You have not entered a valid date.\nBe sure it is formatted as `month/day`")
#==============================================================================
    @datestatus.command(name="printdate", pass_context=False)
    @checks.is_owner()
    async def _printdate_datestatus(self, dayinput : int):
        """Prints date that the cog is counting towards"""
        month = self.settings["MONTH_NUMBER"]
        day = self.settings["DAY_NUMBER"]

        await self.bot.say("Counting down towards {} {}".format(monthname[month], day))
#==============================================================================
    @datestatus.command(name="name", pass_context=False)
    @checks.is_owner()
    async def _name_datestatus(self, *, name=None):
        """Name for the day that you are counting down for. Leave blank to clear."""

        if name:
            self.settings["DATE_NAME"] = name
            dataIO.save_json(self.file_path, self.settings)
            await self.bot.say("Date name successfully set to `{}`".format(name))
        else:
            self.settings["DATE_NAME"] = None
            dataIO.save_json(self.file_path, self.settings)
            await self.bot.say("Date name cleared.")
#==============================================================================
    @datestatus.command(name="force_update", pass_context=False)
    @checks.is_owner()
    async def _force_update_datestatus(self):
        """Forces an update of the status on command"""
        datename = self.settings["DATE_NAME"]
        status_verify = self.status_creator()

        await self.bot.change_presence(game=discord.Game(name=status_verify))
        self.last_check = int(time.perf_counter())
        await self.bot.say("Done.")
#==============================================================================
    def datecheck(self):
        today = date.today()
        monthnumber = self.settings["MONTH_NUMBER"]
        daysnumber = self.settings["DAY_NUMBER"]
        targetdate = date(today.year, monthnumber, daysnumber)


        if targetdate < today:
            targetdate = targetdate.replace(year=today.year + 1)
            daysremain = abs(targetdate - today)
            return daysremain.days
        else:
            daysremain = abs(targetdate - today)
            return daysremain.days
#==============================================================================
    def status_creator(self):
        days_remaining = self.datecheck()
        datename = self.settings["DATE_NAME"]
        if datename == None:
            return "{} Days Remain!".format(days_remaining)
        else:
            return "{} Days until {}!".format(days_remaining, datename)
#==============================================================================
    async def check_date_looper(self, message):
        if not message.channel.is_private:
            status_verify = self.status_creator()
            current_game = str(message.server.me.game)

            if self.last_check == None: #first run
                self.last_check = int(time.perf_counter())
                await self.bot.change_presence(game=discord.Game(name=status_verify))

            if abs(self.last_check - int(time.perf_counter())) >= 3600:
                self.last_check = int(time.perf_counter())
                if status_verify != current_game:
                    await self.bot.change_presence(game=discord.Game(name=status_verify))
#==============================================================================
def check_folders():
    if not os.path.exists("data/pwning-cogs/datestatustimer"):
        print("Creating datestatustimer folder...")
        os.makedirs("data/pwning-cogs/datestatustimer")

def check_files():
    settings = {"DATE_NAME" : "New Year's", "MONTH_NUMBER" : 1, "DAY_NUMBER" : 1}

    if not dataIO.is_valid_json("data/pwning-cogs/datestatustimer/settings.json"):
        print("Creating example settings.json for datestatustimer...")
        dataIO.save_json("data/pwning-cogs/datestatustimer/settings.json", settings)

def setup(bot):
    check_folders()
    check_files()
    n = Datestatustimer(bot)
    bot.add_listener(n.check_date_looper, "on_message")
    bot.add_cog(n)
