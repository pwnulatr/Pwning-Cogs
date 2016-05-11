import discord
from discord.ext import commands
from random import choice
from datetime import datetime
import os

class Isitchristmas:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)

    async def isitchristmas(self):
        """Tells you if it is Christmas or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "Holla :christmas_tree: playa :christmas_tree: it :christmas_tree: is :christmas_tree: finally :christmas_tree: Christmas :christmas_tree:", "BUST OUT THAT FIGGY PUDDIN' Y'ALL! IT'S CHRISTMAS!", "Awwww yeeeee C :snowman: H :snowman: R :snowman: I :snowman: S :snowman: T :snowman: M :snowman: A :snowman: S"]

        if month == 12:
            if day == 25:
                await self.bot.say(choice(yes))
            else:
                await self.bot.say(choice(no))
        else:
            await self.bot.say(choice(no))


def setup(bot):
    n = Isitchristmas(bot)
    bot.add_cog(n)
