import os
import discord
from datetime import date
from discord.ext import commands
from .utils.dataIO import dataIO

__author__ = "Pwnulatr"
__version__ = "2.1.1"


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
            await self.bot.reply("This appears to be your first outage on record.")
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
    async def howmanytimes(self, ctx, *, user: discord.Member = None):
        """Says what the current tally is"""

        author = ctx.message.author

        if not user:
            user = author

        user_id = user.id

        if user_id in self.settings:
            tally_count = self.settings[user_id]["Tally"]
            last_out = self.settings[user_id]["Last Outage"]
            info = discord.Embed(colour=user.colour)
            info.add_field(name="Total Disconnects", value=tally_count)
            info.add_field(name="Last Outage", value=last_out)

            name = str(user)
            name = " | ".join((name, user.nick)) if user.nick else name

            if user.avatar_url:
                info.set_author(name=name, url=user.avatar_url)
                info.set_thumbnail(url=user.avatar_url)
            else:
                info.set_author(name=name)
            try:
                await self.bot.say(embed=info)
            except discord.HTTPException:
                await self.bot.say("Uh oh! I need the `Embed Links` permission to send fancy embedded messages!")
        elif user_id not in self.settings:
            if user_id == author.id:
                await self.bot.reply("You are not currently in the database. You need to log your first outage before"
                                     " I can tell you what your outage statistics are.")
            else:
                await self.bot.reply("That user is currently not in the database. They would need to log their first"
                                     " outage before I can display their statistics.")
        else:
            await self.bot.reply("Something went wrong.")  # Perfect error handling


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
