# Sauce: rapidtables.com AND checkyourmath.com
# Coded by Pwnulatr with a ton of math help from Exbrandong
from discord.ext import commands
from __main__ import send_cmd_help
from random import choice

class UnitConverter:
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
    @commands.group(pass_context=True)
    async def currency(self, ctx):
        """Units of currency you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
#------------------------------------------------------------------------------
    @commands.group(pass_context=True)
    async def data(self, ctx):
        """Units of data you can convert (In binary form, ex. 1024 not 1000)"""

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
    @speed.command(name= "mps2kmh", pass_context=False)
    async def _mps2kmh_speed(self, userinput):
        """Meters Per Second to Kilometers Per Hour"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 3.6

        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " KMH`")
#------------------------------------------------------------------------------
    @speed.command(name= "kmh2mps", pass_context=False)
    async def _kmh2mps_speed(self, userinput):
        """Kilometers Per Hour to Meters Per Second"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 3.6

        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " M/S`")
#------------------------------------------------------------------------------
    @speed.command(name= "fps2mph", pass_context=False)
    async def _fps2mph_speed(self, userinput):
        """Feet Per Second to Miles Per Hour"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1.46666666666667

        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " MPH`")
#------------------------------------------------------------------------------
    @speed.command(name= "mph2fps", pass_context=False)
    async def _mph2fps_speed(self, userinput):
        """Miles Per Hour to Feet Per Second"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1.46666666666667

        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " FPS`")
#------------------------------------------------------------------------------
    @speed.command(name= "knots2mph", pass_context=False)
    async def _knots2mph_speed(self, userinput):
        """Knots to Miles Per Hour"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1.15078

        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " MPH`")
#------------------------------------------------------------------------------
    @speed.command(name= "mph2knots", pass_context=False)
    async def _mph2knots_speed(self, userinput):
        """Miles Per Hour to Knots"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1.15078

        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " Knots`")
#------------------------------------------------------------------------------
    @speed.command(name= "kmh2knots", pass_context=False)
    async def _kmh2knots_speed(self, userinput):
        """Kilometers Per Hour to Knots"""

        newinteger = int(str(userinput))
        anothaconversion = newinteger / 1.609344
        convertedinteger = anothaconversion / 1.15078

        await self.bot.say("Your converted speed is `" + str(convertedinteger) + " Knots`")
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
    @length.command(name= "cm2mm", pass_context=False)
    async def _cm2mm_length(self, userinput):
        """Centimeters to Millimeters"""

        responses = ["I am so sad that the education system has failed you.", "Just move the decimal point to the right by one integer.", "Are you serious?"]
        newinteger = int(str(userinput))
        convertedinteger = newinteger * 10

        await self.bot.say(responses + " But hey, because you asked... Your converted length is `" + str(convertedinteger) + " Millimeters`")
#------------------------------------------------------------------------------
    @length.command(name= "f2mm", pass_context=False)
    async def _f2mm_length(self, userinput):
        """Feet to Millimeters"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 304.8

        await self.bot.say("Your converted length is `" + str(convertedinteger) + " Millimeters`")
#------------------------------------------------------------------------------
    @length.command(name= "f2in", pass_context=False)
    async def _f2in_length(self, userinput):
        """Feet to Inches"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 12

        await self.bot.say("Your converted length is `" + str(convertedinteger) + " Inches`")
#------------------------------------------------------------------------------
    @length.command(name= "f2m", pass_context=False)
    async def _f2m_length(self, userinput):
        """Feet to Meters"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 0.3048

        await self.bot.say("Your converted length is `" + str(convertedinteger) + " Meters`")
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||CURRENCY||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
    @currency.command(name= "msp2dollar", pass_context=False)
    async def _msp2dollar_currency(self, userinput):
        """Microsoft Points to US/CA Dollars"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 80

        await self.bot.say("Your converted currency is `$" + str(round(convertedinteger, 2)) + "`")
#------------------------------------------------------------------------------
    @currency.command(name= "dollar2msp", pass_context=False)
    async def _dollar2msp_currency(self, userinput):
        """US/CA Dollars to Microsoft Points"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 80

        await self.bot.say("Your converted currency is `" + str(int(convertedinteger)) + " Points`")
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||DATA||||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
    @data.command(name= "bits2bytes", pass_context=False)
    async def _bits2bytes_data(self, userinput):
        """Bits to Bytes (will work with any data prefix if converting to same prefix)"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 8

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " bytes`")
#------------------------------------------------------------------------------
    @data.command(name= "bytes2bits", pass_context=False)
    async def _bytes2bits_data(self, userinput):
        """Bytes to Bits (will work with any data prefix if converting to same prefix)"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 8

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " bits`")
#------------------------------------------------------------------------------
    @data.command(name= "b2kb", pass_context=False)
    async def _b2kb_data(self, userinput):
        """Bits/Bytes to Kilobits/Kilobytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1024

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Kilobits/Kilobytes`")
#------------------------------------------------------------------------------
    @data.command(name= "b2mb", pass_context=False)
    async def _b2mb_data(self, userinput):
        """Bits/Bytes to Megabits/Megabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1048576

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Megabits/Megabytes`")
#------------------------------------------------------------------------------
    @data.command(name= "b2gb", pass_context=False)
    async def _b2gb_data(self, userinput):
        """Bits/Bytes to Gigabits/Gigabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1073741824

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Gigabits/Gigabytes`")
#------------------------------------------------------------------------------
    @data.command(name= "b2tb", pass_context=False)
    async def _b2tb_data(self, userinput):
        """Bits/Bytes to Terabits/Terabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1099511627776

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Terabits/Terabytes`")
#||||||||||||||||||||||||||||||||||KILOBITS||||||||||||||||||||||||||||||||||||
    @data.command(name= "kb2b", pass_context=False)
    async def _kb2b_data(self, userinput):
        """Kilobits/Kilobytes to Bits/Bytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1024

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Bits/Bytes`")
#------------------------------------------------------------------------------
    @data.command(name= "kb2mb", pass_context=False)
    async def _kb2mb_data(self, userinput):
        """Kilobits/Kilobytes to Megabits/Megabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1024

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Megabits/Megabytes`")
#------------------------------------------------------------------------------
    @data.command(name= "kb2gb", pass_context=False)
    async def _kb2gb_data(self, userinput):
        """Kilobits/Kilobytes to Gigabits/Gigabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1048576

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Gigabits/Gigabytes`")
#------------------------------------------------------------------------------
    @data.command(name= "kb2tb", pass_context=False)
    async def _kb2tb_data(self, userinput):
        """Kilobits/Kilobytes to Gigabits/Gigabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1073741824

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Terabits/Terabytes`")
#||||||||||||||||||||||||||||||||||MEGABITS||||||||||||||||||||||||||||||||||||
    @data.command(name= "mb2b", pass_context=False)
    async def _mb2b_data(self, userinput):
        """Megabits/Megabytes to Bits/Bytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1048576

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Bits/Bytes`")
#------------------------------------------------------------------------------
    @data.command(name= "mb2kb", pass_context=False)
    async def _mb2kb_data(self, userinput):
        """Megabits/Megabytes to Kilobits/Kilobytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1024

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Kilobits/Kilobytes`")
#------------------------------------------------------------------------------
    @data.command(name= "mb2gb", pass_context=False)
    async def _mb2gb_data(self, userinput):
        """Megabits/Megabytes to Gigabits/Gigabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1024

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Gigabits/Gigabytes`")
#------------------------------------------------------------------------------
    @data.command(name= "mb2tb", pass_context=False)
    async def _mb2tb_data(self, userinput):
        """Megabits/Megabytes to Terabits/Terabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1048576

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Terabits/Terabytes`")
#||||||||||||||||||||||||||||||||||GIGABITS||||||||||||||||||||||||||||||||||||
    @data.command(name= "gb2b", pass_context=False)
    async def _gb2b_data(self, userinput):
        """Gigabits/Gigabytes to Bits/Bytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1073741824

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Bits/Bytes`")
#------------------------------------------------------------------------------
    @data.command(name= "gb2kb", pass_context=False)
    async def _gb2kb_data(self, userinput):
        """Gigabits/Gigabytes to Kilobits/Kilobytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1048576

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Kilobits/Kilobytes`")
#------------------------------------------------------------------------------
    @data.command(name= "gb2mb", pass_context=False)
    async def _gb2mb_data(self, userinput):
        """Gigabits/Gigabytes to Kilobits/Kilobytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1024

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Megabits/Megabytes`")
#------------------------------------------------------------------------------
    @data.command(name= "gb2tb", pass_context=False)
    async def _gb2tb_data(self, userinput):
        """Gigabits/Gigabytes to Terabits/Terabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger / 1024

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Terabits/Terabytes`")
#||||||||||||||||||||||||||||||||||TERABITS||||||||||||||||||||||||||||||||||||
    @data.command(name= "tb2b", pass_context=False)
    async def _tb2b_data(self, userinput):
        """Terabits/Terabytes to Bits/Bytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1099511627776

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Bits/Bytes`")
#------------------------------------------------------------------------------
    @data.command(name= "tb2kb", pass_context=False)
    async def _tb2kb_data(self, userinput):
        """Terabits/Terabytes to Kilobits/Kilobytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1073741824

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Kilobits/Kilobytes`")
#------------------------------------------------------------------------------
    @data.command(name= "tb2mb", pass_context=False)
    async def _tb2mb_data(self, userinput):
        """Terabits/Terabytes to Megabits/Megabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1048576

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Megabits/Megabytes`")
#------------------------------------------------------------------------------
    @data.command(name= "tb2gb", pass_context=False)
    async def _tb2gb_data(self, userinput):
        """Terabits/Terabytes to Gigabits/Gigabytes, respectively"""

        newinteger = int(str(userinput))
        convertedinteger = newinteger * 1024

        await self.bot.say("Your converted data amount is `" + str(convertedinteger) + " Gigabits/Gigabytes`")
#------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||||||DEFINE|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
# This tells the bot to add these commands to the help context
def setup(bot):
    n = UnitConverter(bot)
    bot.add_cog(n)
