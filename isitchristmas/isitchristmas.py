# isitchristmas coded by Pwnulatr as a personal test to learn python and put
# it to use :)
# TO-DO Add more yes responses to the Thanksgiving section. Weekday is 3. Possible fall dates are 22-28
import discord
from discord.ext import commands
from random import choice
from datetime import datetime

class Isitchristmas:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=False)

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
# ----------------------------------------------------------------------------
    @commands.command(no_pm=False)

    async def isithalloween(self):
        """Tells you if it is Halloween or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "Spoopy time guise :jack_o_lantern: :ghost: :candy: :skull_crossbones: :spider_web :skull:", "HAPPY HALL:jack_o_lantern:WEEN", "BUST OUT THE PUMPKIN PIE Y'ALL, IT'S SPOOPY HALLOWEEN TIME!"]

        if month == 10:
            if day == 31:
                await self.bot.say(choice(yes))
            else:
                await self.bot.say(choice(no))
        else:
            await self.bot.say(choice(no))
# ----------------------------------------------------------------------------
    @commands.command(no_pm=False)

    async def isitvalentinesday(self):
        """Tells you if it is Valentine's Day or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "Time for the lovin'", "Time to break out the body pillow ;)", "Time to break out that Marvin Gaye :heart_exclamation:"]

        if month == 2:
            if day == 14:
                await self.bot.say(choice(yes))
            else:
                await self.bot.say(choice(no))
        else:
            await self.bot.say(choice(no))
# ----------------------------------------------------------------------------
    @commands.command(no_pm=False)

    async def isitaprilfoolsday(self):
        """Tells you if it is April Fool's Day or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "No ;)"]

        if month == 4:
            if day == 1:
                await self.bot.say(choice(yes))
            else:
                await self.bot.say(choice(no))
        else:
            await self.bot.say(choice(no))
# ----------------------------------------------------------------------------
    @commands.command(no_pm=False)

    async def isitindependenceday(self):
        """Tells you if it is Independence Day (American) or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "YEAH 'MERICA'", "FREEEEEEEEEEDOM DAY!!!", "LIBERRTYYYYY AND JUSTICE!!!!!!!!", "U :gun: S :boom: A :fireworks:"]

        if month == 7:
            if day == 4:
                await self.bot.say(choice(yes))
            else:
                await self.bot.say(choice(no))
        else:
            await self.bot.say(choice(no))
# ----------------------------------------------------------------------------
    @commands.command(no_pm=False)

    async def isitthanksgiving(self):
        """Tells you if it Thanksgiving Day (American) or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        weekday = time.weekday
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "Happy Turkey Day!", ""]
        thisisrepetitiveplezstahp = ["22", "23", "24", "25", "26", "27", "28"]

        if month == 11:
            if weekday == 3:
                if day in thisisrepetitiveplezstahp:
                    await self.bot.say(choice(yes))
                else:
                    await self.bot.say(choice(no))
            else:
                await self.bot.say(choice(no))
        else:
            await self.bot.say(choice(no))
# ----------------------------------------------------------------------------
def setup(bot):
    n = Isitchristmas(bot)
    bot.add_cog(n)
