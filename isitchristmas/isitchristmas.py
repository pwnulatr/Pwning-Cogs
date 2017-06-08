# isitchristmas coded by Pwnulatr as a personal test to learn python and put
# it to use :)
from discord.ext import commands
from __main__ import send_cmd_help
from random import choice
from datetime import datetime

class Isitchristmas:
    """Determine if it is a Holiday today"""

    def __init__(self, bot):
        self.bot = bot
# -----------------------------------------------------------------------------
    @commands.group(pass_context=True)

    async def isit(self, ctx):
        """These are the different holidays you can query."""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
# -----------------------------------------------------------------------------
    @isit.command(name="christmas", pass_context=False)

    async def _christmas_isit(self):
        """Tells you if it is Christmas or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "Holla :christmas_tree: playa :christmas_tree: it :christmas_tree: is :christmas_tree: finally :christmas_tree: Christmas :christmas_tree:", "BUST OUT THAT FIGGY PUDDIN' Y'ALL! IT'S CHRISTMAS!", "Awwww yeeeee C :snowman: H :snowman: R :snowman: I :snowman: S :snowman: T :snowman: M :snowman: A :snowman: S"]

        if month == 12 and day == 25:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
    @isit.command(name="halloween", pass_context=False)

    async def _halloween_isit(self):
        """Tells you if it is Halloween or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "Spoopy time guise :jack_o_lantern: :ghost: :candy: :skull_crossbones: :spider_web: :skull:", "HAPPY HALL:jack_o_lantern:WEEN", "BUST OUT THE PUMPKIN PIE Y'ALL, IT'S SPOOPY HALLOWEEN TIME!"]

        if month == 10 and day == 31:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
    @isit.command(name="valentinesday", pass_context=False)

    async def _valentinesday_isit(self):
        """Tells you if it is Valentine's Day or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "Time for the lovin'", "Time to break out the body pillow ;)", "Time to break out that Marvin Gaye :heart_exclamation:"]

        if month == 2 and day == 14:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
    @isit.command(name="aprilfoolsday", pass_context=False)

    async def _aprilfoolsday_isit(self):
        """Tells you if it is April Fool's Day or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "No ;)"]

        if month == 4 and day == 1:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
    @isit.command(name="independenceday", pass_context=False)

    async def _independenceday_isit(self):
        """Tells you if it is Independence Day (American) or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "YEAH 'MERICA'", "FREEEEEEEEEEDOM DAY!!!", "LIBERRTYYYYY AND JUSTICE!!!!!!!!", "U :gun: S :boom: A :fireworks:"]

        if month == 7 and day == 4:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
    @isit.command(name="thanksgiving", pass_context=False)

    async def _thanksgiving_isit(self):
        """Tells you if it is Thanksgiving Day (American) or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        weekday = time.weekday()
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi", "Happy Turkey Day!", "Y :turkey: E :turkey: S"]
        daterange = list(range(22, 29))

        if month == 11 and weekday == 3 and day in daterange:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
    @isit.command(name="thanksgivingincanada", pass_context=False)

    async def _thanksgivingincanada_isit(self):
        """Tells you if it is Thanksgiving Day (Canada) or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        weekday = time.weekday()
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi"]
        daterange = list(range(8, 15))

        if month == 11 and weekday == 0 and day in daterange:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
    @isit.command(name="mothersday", pass_context=False)

    async def _mothersday_isit(self):
        """Tells you if it is Mother's Day or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        weekday = time.weekday()
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi"]
        daterange = list(range(8, 15))

        if month == 5 and weekday == 6 and day in daterange:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
    @isit.command(name="fathersday", pass_context=False)

    async def _fathersday_isit(self):
        """Tells you if it is Father's Day or not"""
        time = datetime.now()
        month = time.month
        day = time.day
        weekday = time.weekday()
        no = ["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not", "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не", "Nie", "No way!"]
        yes = ["Yes", "Yee", "Das right boi"]
        daterange = list(range(15, 23))

        if month == 6 and weekday == 6 and day in daterange:
            await self.bot.say(choice(yes))
        else:
            await self.bot.say(choice(no))
# -----------------------------------------------------------------------------
def setup(bot):
    n = Isitchristmas(bot)
    bot.add_cog(n)
