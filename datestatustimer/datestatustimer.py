# Coded by Pwnulatr with the help of many cogs that came with Red
from discord.ext import commands
from __main__ import send_cmd_help
from datetime import datetime
from .utils.dataIO import dataIO
from datetime import date
from cogs.utils import checks
import discord
import os
import time
import asyncio

class Datestatustimer:
    """Calculates the time between dates and makes it the bot \"playing\" status"""

    def __init__(self, bot):
        self.bot = bot
        self.file_path = "data/pwning-cogs/datestatustimer/settings.json"
        self.settings = dataIO.load_json(self.file_path)

#================================GROUP DEFINE==================================
    @commands.group(pass_context=True)
    async def datestatusset(self, ctx):
        """These are the settings for the date status cog"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
#==============================================================================
    @datestatusset.command(name= "month", pass_context=False)
    @checks.is_owner()
    async def _month_datestatusset(self, monthinput : int):
        """Month for date (1-12)"""
        monthrange = list(range(1, 13))

        if monthinput in monthrange:
            self.settings["MONTH_NUMBER"] = monthinput
            dataIO.save_json(self.file_path, self.settings)
            await self.bot.say("Month successfully set to `{}`".format(str(monthinput)))
        else:
            await self.bot.say("You have not entered a valid month number.")
#==============================================================================
    @datestatusset.command(name= "day", pass_context=False)
    @checks.is_owner()
    async def _day_datestatusset(self, dayinput : int):
        """Day for date (1-28/29/30/31, depending on month)"""
        dayrange = list(range(1, 32))
        monthnumber = self.settings["MONTH_NUMBER"]
        thirty_month = [4, 6, 9, 11]

        if dayinput in dayrange:
            if monthnumber == 2 and dayinput <= 28:
                self.settings["DAY_NUMBER"] = dayinput
                dataIO.save_json(self.file_path, self.settings)
                await self.bot.say("Day successfully set to `{}`".format(str(dayinput)))
            elif monthnumber in thirty_month and dayinput <= 30:
                self.settings["DAY_NUMBER"] = dayinput
                dataIO.save_json(self.file_path, self.settings)
                await self.bot.say("Day successfully set to `{}`".format(str(dayinput)))
            else:
                await self.bot.say("You have not entered a valid day number for the month you have set.")
        else:
            await self.bot.say("You have not entered a valid day number for the month you have set.")
#==============================================================================
    @datestatusset.command(name= "name", pass_context=False)
    @checks.is_owner()
    async def _name_datestatusset(self, *, name=None):
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
    @datestatusset.command(name= "force_update", pass_context=False)
    @checks.is_owner()
    async def _force_update_datestatusset(self):
        """Forces an update of the status on command"""
        datename = self.settings["DATE_NAME"]
        status_verify = self.status_creator()

        await self.bot.change_presence(game=discord.Game(name=status_verify))
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
    async def check_date_looper(self):
        #checkeddate = self.datecheck() #Todo, implement changes check
        status_verify = self.status_creator()

        await self.bot.change_presence(game=discord.Game(name=status_verify))
        await asyncio.sleep(3600)#3600 = 1 hour in seconds
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
    loop = asyncio.get_event_loop()
    loop.create_task(n.check_date_looper())
    bot.add_cog(n)
