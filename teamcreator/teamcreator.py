import discord
from discord.ext import commands
from .utils.chat_formatting import escape_mass_mentions
# from __main__ import send_cmd_help
# from cogs.utils import checks
from random import choice, shuffle


class Teamcreator:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="teams", pass_context=True)
    async def teams(self, ctx, *players):
        """Creates random teams from players in a list"""

        players = [escape_mass_mentions(c) for c in players]
        if len(players) < 2:
            await self.bot.say("Not enough members")
        else:
            shuffle(players)
            team1 = players[::2]
            team2 = players[1::2]
            author = ctx.message.author

            embed = discord.Embed(colour=author.colour)
            embed.add_field(name="Team 1", value="\n".join(team1))
            embed.add_field(name="Team 2", value="\n".join(team2))

            await self.bot.say(embed=embed)


def setup(bot):
    n = Teamcreator(bot)
    bot.add_cog(n)
