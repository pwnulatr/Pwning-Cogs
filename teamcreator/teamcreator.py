import discord
from redbot.core import commands
from .utils.chat_formatting import escape_mass_mentions
from random import choice, shuffle

__author__ = "Pwnulatr"
__version__ = "0.1.2"

class Teamcreator:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="teams", pass_context=True)
    async def teams(self, ctx, *players):
        """Creates random teams from players in a list"""

        players = [escape_mass_mentions(c) for c in players]

        await self.bot.type()

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

            try:
                await self.bot.say(embed=embed)
            except discord.HTTPException:
                await self.bot.say(f"Team 1:```\n{team1}```Team 2:```{team2}```For better looking, fancy "
                                   f"*embedded messages* please give me the `Embed Links` permission for "
                                   f"future queries.")
                return


def setup(bot):
    n = Teamcreator(bot)
    bot.add_cog(n)
