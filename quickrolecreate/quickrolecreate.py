import discord
from discord.ext import commands
from .utils import checks
from discord.ext.commands import converter

__author__ = "Pwnulatr"
__version__ = "0.1.1"


class Quickrolecreate:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="createrole", no_pm=True, pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def createrole(self, ctx, color: str, *, role_name):
        """Create an empty role with a color"""

        server = ctx.message.server

        await self.bot.type()
        try:
            color = converter.ColourConverter(ctx, color).convert()
        except commands.BadArgument:
            await self.bot.say("That is not a valid hexadecimal value.")
            return

        if role_name not in [r.name for r in server.roles]:
            try:
                perms = discord.Permissions.none()
                await self.bot.create_role(server, name=role_name,
                                           colour=color, permissions=perms)
                await self.bot.say("Done.")
            except discord.Forbidden:
                await self.bot.say("I don't have permissions to create roles.")
                return
            except discord.HTTPException:
                await self.bot.say("Could not make request.")
                return


def setup(bot):
    n = Quickrolecreate(bot)
    bot.add_cog(n)
