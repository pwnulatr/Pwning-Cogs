# Sauces: http://www.rapidtables.com/ AND https://www.checkyourmath.com/index.php
from discord.ext import commands
from __main__ import send_cmd_help
import math

class Converter:
    """Unit conversion tool"""

    def __init__(self, bot):
        self.bot = bot
#------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||GROUP DEFINING|||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
# Defining the group command and if no subcommand is sent, send the help message
    @commands.group(pass_context=True)
    async def temp(self, ctx):
        """Units of Temperature you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
#------------------------------------------------------------------------------
    @commands.group(pass_context=True)
    async def speed(self, ctx):
        """Units of speed you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
#------------------------------------------------------------------------------
    @commands.group(pass_context=True)
    async def length(self, ctx):
        """Units of distance you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||TEMPERATURE|||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
# And thus we begin the Copy-Paste abuse
    @temp.command(name= "f2c", pass_context=False)
    async def _f2c_temp(self, userinput):
        """Fahrenheit to Celsius"""

        newinteger = int(str(userinput))
        convertedinteger = ( newinteger - 32 ) / 1.8
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°C`")
#------------------------------------------------------------------------------
    @temp.command(name= "c2f", pass_context=False)
    async def _c2f_temp(self, userinput):
        """Celsius to Fahrenheit"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1.8 + 32
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°F`")
#------------------------------------------------------------------------------
    @temp.command(name= "f2k", pass_context=False)
    async def _f2k_temp(self, userinput):
        """Fahrenheit to Kelvin"""

        newinteger = int(str(userinput))
        convertedinteger = ( newinteger + 459.67 ) * 5 / 9
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°K`")
#------------------------------------------------------------------------------
    @temp.command(name= "c2k", pass_context=False)
    async def _c2k_temp(self, userinput):
        """Celsius to Kelvin"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger + 273.15
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°K`")
#------------------------------------------------------------------------------
    @temp.command(name= "r2k", pass_context=False)
    async def _r2k_temp(self, userinput):
        """Rankine to Kelvin"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 5 / 9
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°K`")
#------------------------------------------------------------------------------
    @temp.command(name= "c2r", pass_context=False)
    async def _c2r_temp(self, userinput):
        """Celsius to Rankine"""

        newinteger = int(str(userinput))
        convertedinteger = ( newinteger + 273.15) * 9 / 5
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°R`")
#------------------------------------------------------------------------------
    @temp.command(name= "f2r", pass_context=False)
    async def _f2r_temp(self, userinput):
        """Fahrenheit to Rankine"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger + 459.67
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°R`")
#------------------------------------------------------------------------------
    @temp.command(name= "k2f", pass_context=False)
    async def _k2f_temp(self, userinput):
        """Kelvin to Fahrenheit"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 9 / 5 - 459.67
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°F`")
#------------------------------------------------------------------------------
    @temp.command(name= "k2c", pass_context=False)
    async def _k2c_temp(self, userinput):
        """Kelvin to Celsius"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger - 273.15
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°C`")
#------------------------------------------------------------------------------
    @temp.command(name= "k2r", pass_context=False)
    async def _k2r_temp(self, userinput):
        """Kelvin to Rankine"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 9 / 5
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°R`")
#------------------------------------------------------------------------------
    @temp.command(name= "r2f", pass_context=False)
    async def _r2f_temp(self, userinput):
        """Rankine to Fahrenheit"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger - 459.67
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°F`")
#------------------------------------------------------------------------------
    @temp.command(name= "r2c", pass_context=False)
    async def _r2c_temp(self, userinput):
        """Rankine to Celsius"""

        newinteger = int(str(userinput))
        convertedinteger = ( newinteger - 491.67 ) * 5 / 9
        await self.bot.say("Your converted temperature is `" + str(convertedinteger) + "°C`")
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||SPEED|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
    @speed.command(name= "mph2kmh", pass_context=False)
    async def _mph2kmh_speed(self, userinput):
        """Miles Per Hour to Kilometers Per Hour"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1.609344
        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " KMH`")
#------------------------------------------------------------------------------
    @speed.command(name= "kmh2mph", pass_context=False)
    async def _kmh2mph_speed(self, userinput):
        """Kilometers Per Hour to Miles Per Hour"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1.609344
        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " MPH`")
#------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||||||LENGTH|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
    @length.command(name= "cm2f", pass_context=False)
    async def _cm2f_length(self, userinput):
        """Centimeters to Feet"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 30.48
        inches = convertedinteger * 12

        if convertedinteger < 1:
            await self.bot.say("Your converted length is `" + str(convertedinteger) + " feet` or `0 feet " + str(inches) + " inches`")
        else:
            remaininch = inches - (12 * int(convertedinteger))
            await self.bot.say("Your converted length is `" + str(convertedinteger) + " feet` or `" + str(int(convertedinteger)) + " feet " + str(remaininch) + " inches`")
# Thanks for the help with the math Exbrandong :D couldn't have done it w/o you
#------------------------------------------------------------------------------
    @length.command(name= "cm2in", pass_context=False)
    async def _cm2in_length(self, userinput):
        """Centimeters to Inches"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 2.54

        if convertedinteger < 12:
            await self.bot.say("Your converted length is `" + str(convertedinteger) + " inches`")
        else:
            feet = convertedinteger / 12
            inches = convertedinteger - (12 * int(feet))
            await self.bot.say("Your converted length is `" + str(convertedinteger) + " inches` or `" + str(int(feet)) + " feet " + str(inches) + " inches`")
#------------------------------------------------------------------------------
    @length.command(name= "f2cm", pass_context=False)
    async def _f2cm_length(self, userinput):
        """Feet to Centimeters"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 30.48

        await self.bot.say("Your converted length is `" + str(convertedinteger) + " centimeters`")
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
def setup(bot):
    n = Converter(bot)
    bot.add_cog(n)
