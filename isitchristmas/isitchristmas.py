from discord.ext import commands
from __main__ import send_cmd_help
from random import choice
from datetime import datetime


def yes(alternative_choices=[]) -> str:
    return choice(["Yes", "Yee", "Das right boi"] + alternative_choices)


def no() -> str:
    return choice(["No", "Nah", "Nope", "Nu-uh", "Not yet", "Nada", "Nein", "It ain't happening", "Of course not",
                   "Not today", "How about no", "Not at the moment, young one", "Meh", "hakuna", "нет", "Nee", "не",
                   "Nie", "No way!"])


class Isitchristmas:
    async def possibly_say(self, condition, yes_choices=[]):
        time = datetime.now()
        month = time.month
        day = time.day
        weekday = time.weekday()
        await self.bot.say((yes(yes_choices) if condition(month, day, weekday) else no()))

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def isit(self, ctx):
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @isit.command(name="christmas", pass_context=False)
    async def _christmas_isit(self):
        await self.possibly_say(lambda month, day, _: month == 12 and day == 25, yes_choices=[
            "Holla :christmas_tree: playa :christmas_tree: it :christmas_tree: is :christmas_tree: finally "
            ":christmas_tree: Christmas :christmas_tree:", "BUST OUT THAT FIGGY PUDDIN' Y'ALL! IT'S CHRISTMAS!",
            "Awwww yeeeee C :snowman: H :snowman: R :snowman: I :snowman: S :snowman: T :snowman: M :snowman: "
            "A :snowman: S"])

    @isit.command(name="halloween", pass_context=False)
    async def _halloween_isit(self):
        await self.possibly_say(lambda month, day, _: month == 10 and day == 31, yes_choices=[
            "Spoopy time guise :jack_o_lantern: :ghost: :candy: :skull_crossbones: :spider_web: :skull:",
            "HAPPY HALL:jack_o_lantern:WEEN", "BUST OUT THE PUMPKIN PIE Y'ALL, IT'S SPOOPY HALLOWEEN TIME!"])

    @isit.command(name="valentinesday", pass_context=False)
    async def _valentinesday_isit(self):
        await self.possibly_say(lambda month, day, _: month == 10 and day == 31, yes_choices=[
            "Time for the lovin'", "Time to break out the body pillow ;)",
            "Time to break out that Marvin Gaye :heart_exclamation:"])

    @isit.command(name="aprilfoolsday", pass_context=False)
    async def _aprilfoolsday_isit(self):
        await self.possibly_say(lambda month, day, _: month == 4 and day == 1, yes_choices=["No ;)"])

    @isit.command(name="independenceday", pass_context=False)
    async def _independenceday_isit(self):
        await self.possibly_say(lambda month, day, _: month == 7 and day == 4, yes_choices=[
            "YEAH 'MERICA'", "FREEEEEEEEEEDOM DAY!!!", "LIBERRTYYYYY AND JUSTICE!!!!!!!!",
            "U :gun: S :boom: A :fireworks:"])

    @isit.command(name="thanksgiving", pass_context=False)
    async def _thanksgiving_isit(self):
        await self.possibly_say(lambda month, day, weekday: month == 1 and weekday == 3 and day in list(range(22, 29)),
                                yes_choices=["Happy Turkey Day!", "Y :turkey: E :turkey: S"])

    @isit.command(name="thanksgivingincanada", pass_context=False)
    async def _thanksgivingincanada_isit(self):
        await self.possibly_say(lambda month, day, weekday: month == 1 and weekday == 0 and day in list(range(8, 15)))

    @isit.command(name="mothersday", pass_context=False)
    async def _mothersday_isit(self):
        await self.possibly_say(lambda month, day, weekday: month == 5 and weekday == 6 and day in list(range(8, 15)))

    @isit.command(name="fathersday", pass_context=False)
    async def _fathersday_isit(self):
        await self.possibly_say(lambda month, day, weekday: month == 6 and weekday == 6 and day in list(range(15, 23)))

    @isit.command(name="canadaday", pass_context=False)
    async def _canadaday_isit(self):
        await self.possibly_say(lambda month, day, _: month == 7 and day == 1)


def setup(bot):
    bot.add_cog(Isitchristmas(bot))
