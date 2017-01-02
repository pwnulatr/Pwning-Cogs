# Sauce: rapidtables.com AND checkyourmath.com
# Coded by Pwnulatr with a ton of math help from Exbrandong
from discord.ext import commands
from __main__ import send_cmd_help


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

    @temp.command(name="f2c", pass_context=False)
    async def _f2c_temp(self, userinput: int):
        """Fahrenheit to Celsius"""

        convertedinteger = (userinput - 32) / 1.8

        await self.bot.say("Your converted temperature is `{}°C`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="c2f", pass_context=False)
    async def _c2f_temp(self, userinput: int):
        """Celsius to Fahrenheit"""

        convertedinteger = userinput * 1.8 + 32

        await self.bot.say("Your converted temperature is `{}°F`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="f2k", pass_context=False)
    async def _f2k_temp(self, userinput: int):
        """Fahrenheit to Kelvin"""

        convertedinteger = (userinput + 459.67) * 5 / 9

        await self.bot.say("Your converted temperature is `{}°K`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="c2k", pass_context=False)
    async def _c2k_temp(self, userinput: int):
        """Celsius to Kelvin"""

        convertedinteger = userinput + 273.15

        await self.bot.say("Your converted temperature is `{}°K`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="r2k", pass_context=False)
    async def _r2k_temp(self, userinput: int):
        """Rankine to Kelvin"""

        convertedinteger = userinput * 5 / 9

        await self.bot.say("Your converted temperature is `{}°K`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="c2r", pass_context=False)
    async def _c2r_temp(self, userinput: int):
        """Celsius to Rankine"""

        convertedinteger = (userinput + 273.15) * 9 / 5

        await self.bot.say("Your converted temperature is `{}°R`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="f2r", pass_context=False)
    async def _f2r_temp(self, userinput: int):
        """Fahrenheit to Rankine"""

        convertedinteger = userinput + 459.67

        await self.bot.say("Your converted temperature is `{}°R`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="k2f", pass_context=False)
    async def _k2f_temp(self, userinput: int):
        """Kelvin to Fahrenheit"""

        convertedinteger = userinput * 9 / 5 - 459.67

        await self.bot.say("Your converted temperature is `{}°F`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="k2c", pass_context=False)
    async def _k2c_temp(self, userinput: int):
        """Kelvin to Celsius"""

        convertedinteger = userinput - 273.15

        await self.bot.say("Your converted temperature is `{}°C`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="k2r", pass_context=False)
    async def _k2r_temp(self, userinput: int):
        """Kelvin to Rankine"""

        convertedinteger = userinput * 9 / 5

        await self.bot.say("Your converted temperature is `{}°R`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="r2f", pass_context=False)
    async def _r2f_temp(self, userinput: int):
        """Rankine to Fahrenheit"""

        convertedinteger = userinput - 459.67

        await self.bot.say("Your converted temperature is `{}°F`".format(convertedinteger))
#------------------------------------------------------------------------------

    @temp.command(name="r2c", pass_context=False)
    async def _r2c_temp(self, userinput: int):
        """Rankine to Celsius"""

        convertedinteger = (userinput - 491.67) * 5 / 9

        await self.bot.say("Your converted temperature is `{}°C`".format(convertedinteger))
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||SPEED|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

    @speed.command(name="mph2kmh", pass_context=False)
    async def _mph2kmh_speed(self, userinput: int):
        """Miles Per Hour to Kilometers Per Hour"""

        convertedinteger = userinput * 1.609344

        await self.bot.say("Your converted speed is `{} KMH`".format(convertedinteger))
#------------------------------------------------------------------------------

    @speed.command(name="kmh2mph", pass_context=False)
    async def _kmh2mph_speed(self, userinput: int):
        """Kilometers Per Hour to Miles Per Hour"""

        convertedinteger = userinput / 1.609344

        await self.bot.say("Your converted speed is `{} MPH`".format(convertedinteger))
#------------------------------------------------------------------------------

    @speed.command(name="mps2kmh", pass_context=False)
    async def _mps2kmh_speed(self, userinput: int):
        """Meters Per Second to Kilometers Per Hour"""

        convertedinteger = userinput * 3.6

        await self.bot.say("Your converted speed is `{} KMH`".format(convertedinteger))
#------------------------------------------------------------------------------

    @speed.command(name="kmh2mps", pass_context=False)
    async def _kmh2mps_speed(self, userinput: int):
        """Kilometers Per Hour to Meters Per Second"""

        convertedinteger = userinput / 3.6

        await self.bot.say("Your converted speed is `{} M/S`".format(convertedinteger))
#------------------------------------------------------------------------------

    @speed.command(name="fps2mph", pass_context=False)
    async def _fps2mph_speed(self, userinput: int):
        """Feet Per Second to Miles Per Hour"""

        convertedinteger = userinput / 1.46666666666667

        await self.bot.say("Your converted speed is `{} MPH`".format(convertedinteger))
#------------------------------------------------------------------------------

    @speed.command(name="mph2fps", pass_context=False)
    async def _mph2fps_speed(self, userinput: int):
        """Miles Per Hour to Feet Per Second"""

        convertedinteger = userinput * 1.46666666666667

        await self.bot.say("Your converted speed is `{} FPS`".format(convertedinteger))
#------------------------------------------------------------------------------

    @speed.command(name="knots2mph", pass_context=False)
    async def _knots2mph_speed(self, userinput: int):
        """Knots to Miles Per Hour"""

        convertedinteger = userinput * 1.15078

        await self.bot.say("Your converted speed is `{} MPH`".format(convertedinteger))
#------------------------------------------------------------------------------

    @speed.command(name="mph2knots", pass_context=False)
    async def _mph2knots_speed(self, userinput: int):
        """Miles Per Hour to Knots"""

        convertedinteger = userinput / 1.15078

        await self.bot.say("Your converted speed is `{} Knots`".format(convertedinteger))
#------------------------------------------------------------------------------

    @speed.command(name="kmh2knots", pass_context=False)
    async def _kmh2knots_speed(self, userinput: int):
        """Kilometers Per Hour to Knots"""

        anothaconversion = userinput / 1.609344
        convertedinteger = anothaconversion / 1.15078

        await self.bot.say("Your converted speed is `{} Knots`".format(convertedinteger))
#------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||||||LENGTH|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

    @length.command(name="cm2f", pass_context=False)
    async def _cm2f_length(self, userinput: int):
        """Centimeters to Feet"""

        convertedinteger = userinput / 30.48
        inches = convertedinteger * 12

        if convertedinteger < 1:
            await self.bot.say("Your converted length is `{} feet` or `0 feet {} inches`".format(convertedinteger, inches))
        else:
            remaininch = inches - (12 * int(convertedinteger))
            await self.bot.say("Your converted length is `" + str(convertedinteger) + " feet` or `" + str(int(convertedinteger)) + " feet " + str(remaininch) + " inches`")
# Thanks for the help with the math Exbrandong :D couldn't have done it w/o you
#------------------------------------------------------------------------------

    @length.command(name="cm2in", pass_context=False)
    async def _cm2in_length(self, userinput: int):
        """Centimeters to Inches"""

        convertedinteger = userinput / 2.54

        if convertedinteger < 12:
            await self.bot.say("Your converted length is `{} inches`".format(convertedinteger))
        else:
            feet = convertedinteger / 12
            inches = convertedinteger - (12 * int(feet))
            await self.bot.say("Your converted length is `" + str(convertedinteger) + " inches` or `" + str(int(feet)) + " feet " + str(inches) + " inches`")
#------------------------------------------------------------------------------

    @length.command(name="f2cm", pass_context=False)
    async def _f2cm_length(self, userinput: int):
        """Feet to Centimeters"""

        convertedinteger = userinput * 30.48

        await self.bot.say("Your converted length is `{} centimeters`".format(convertedinteger))
#------------------------------------------------------------------------------

    @length.command(name="cm2mm", pass_context=False)
    async def _cm2mm_length(self, userinput: int):
        """Centimeters to Millimeters"""

        convertedinteger = userinput * 10

        await self.bot.say("Your converted length is `{} Millimeters`")
#------------------------------------------------------------------------------

    @length.command(name="f2mm", pass_context=False)
    async def _f2mm_length(self, userinput: int):
        """Feet to Millimeters"""

        convertedinteger = userinput * 304.8

        await self.bot.say("Your converted length is `{} Millimeters`".format(convertedinteger))
#------------------------------------------------------------------------------

    @length.command(name="f2in", pass_context=False)
    async def _f2in_length(self, userinput: int):
        """Feet to Inches"""

        convertedinteger = userinput * 12

        await self.bot.say("Your converted length is `{} Inches`".format(convertedinteger))
#------------------------------------------------------------------------------

    @length.command(name="f2m", pass_context=False)
    async def _f2m_length(self, userinput: int):
        """Feet to Meters"""

        convertedinteger = userinput * 0.3048

        await self.bot.say("Your converted length is `{} Meters`".format(convertedinteger))
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||CURRENCY||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

    @currency.command(name="msp2dollar", pass_context=False)
    async def _msp2dollar_currency(self, userinput: int):
        """Microsoft Points to US/CA Dollars"""

        mathstuff = userinput / 80
        convertedinteger = round(mathstuff, 2)

        await self.bot.say("Your converted currency is `${}`".format(convertedinteger))
#------------------------------------------------------------------------------

    @currency.command(name="dollar2msp", pass_context=False)
    async def _dollar2msp_currency(self, userinput: int):
        """US/CA Dollars to Microsoft Points"""

        convertedinteger = userinput * 80

        await self.bot.say("Your converted currency is `{} Points`".format(convertedinteger))
#------------------------------------------------------------------------------

    @currency.command(name="platinum2dollar", pass_context=False)
    async def _platinum2dollar_currency(self, userinput: int):
        """Platinum (WarFrame currency) to US/CA Dollars"""

        mathstuff = userinput / 15
        convertedinteger = round(mathstuff, 2)

        await self.bot.say("Your converted currency is `${}`".format(convertedinteger))
#------------------------------------------------------------------------------

    @currency.command(name="dollar2platinum", pass_context=False)
    async def _dollar2platinum_currency(self, userinput: int):
        """US/CA Dollars to Platinum (WarFrame currency)"""

        convertedinteger = userinput * 15

        await self.bot.say("Your converted currency is '{} Platinum'".format(convertedinteger))
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||DATA||||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

    @data.command(name="bits2bytes", pass_context=False)
    async def _bits2bytes_data(self, userinput: int):
        """Bits to Bytes (will work with any data prefix if converting to same prefix)"""

        convertedinteger = userinput / 8

        await self.bot.say("Your converted data amount is `{} bytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="bytes2bits", pass_context=False)
    async def _bytes2bits_data(self, userinput: int):
        """Bytes to Bits (will work with any data prefix if converting to same prefix)"""

        convertedinteger = userinput * 8

        await self.bot.say("Your converted data amount is `{} bits`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="b2kb", pass_context=False)
    async def _b2kb_data(self, userinput: int):
        """Bits/Bytes to Kilobits/Kilobytes, respectively"""

        convertedinteger = userinput / 1024

        await self.bot.say("Your converted data amount is `{} Kilobits/Kilobytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="b2mb", pass_context=False)
    async def _b2mb_data(self, userinput: int):
        """Bits/Bytes to Megabits/Megabytes, respectively"""

        convertedinteger = userinput / 1048576

        await self.bot.say("Your converted data amount is `{} Megabits/Megabytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="b2gb", pass_context=False)
    async def _b2gb_data(self, userinput: int):
        """Bits/Bytes to Gigabits/Gigabytes, respectively"""

        convertedinteger = userinput / 1073741824

        await self.bot.say("Your converted data amount is `{} Gigabits/Gigabytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="b2tb", pass_context=False)
    async def _b2tb_data(self, userinput: int):
        """Bits/Bytes to Terabits/Terabytes, respectively"""

        convertedinteger = userinput / 1099511627776

        await self.bot.say("Your converted data amount is `{} Terabits/Terabytes`".format(convertedinteger))
#||||||||||||||||||||||||||||||||||KILOBITS||||||||||||||||||||||||||||||||||||

    @data.command(name="kb2b", pass_context=False)
    async def _kb2b_data(self, userinput: int):
        """Kilobits/Kilobytes to Bits/Bytes, respectively"""

        convertedinteger = userinput * 1024

        await self.bot.say("Your converted data amount is `{} Bits/Bytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="kb2mb", pass_context=False)
    async def _kb2mb_data(self, userinput: int):
        """Kilobits/Kilobytes to Megabits/Megabytes, respectively"""

        convertedinteger = userinput / 1024

        await self.bot.say("Your converted data amount is `{} Megabits/Megabytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="kb2gb", pass_context=False)
    async def _kb2gb_data(self, userinput: int):
        """Kilobits/Kilobytes to Gigabits/Gigabytes, respectively"""

        convertedinteger = userinput / 1048576

        await self.bot.say("Your converted data amount is `{} Gigabits/Gigabytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="kb2tb", pass_context=False)
    async def _kb2tb_data(self, userinput: int):
        """Kilobits/Kilobytes to Gigabits/Gigabytes, respectively"""

        convertedinteger = userinput / 1073741824

        await self.bot.say("Your converted data amount is `{} Terabits/Terabytes`".format(convertedinteger))
#||||||||||||||||||||||||||||||||||MEGABITS||||||||||||||||||||||||||||||||||||

    @data.command(name="mb2b", pass_context=False)
    async def _mb2b_data(self, userinput: int):
        """Megabits/Megabytes to Bits/Bytes, respectively"""

        convertedinteger = userinput * 1048576

        await self.bot.say("Your converted data amount is `{} Bits/Bytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="mb2kb", pass_context=False)
    async def _mb2kb_data(self, userinput: int):
        """Megabits/Megabytes to Kilobits/Kilobytes, respectively"""

        convertedinteger = userinput * 1024

        await self.bot.say("Your converted data amount is `{} Kilobits/Kilobytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="mb2gb", pass_context=False)
    async def _mb2gb_data(self, userinput: int):
        """Megabits/Megabytes to Gigabits/Gigabytes, respectively"""

        convertedinteger = userinput / 1024

        await self.bot.say("Your converted data amount is `{} Gigabits/Gigabytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="mb2tb", pass_context=False)
    async def _mb2tb_data(self, userinput: int):
        """Megabits/Megabytes to Terabits/Terabytes, respectively"""

        convertedinteger = userinput / 1048576

        await self.bot.say("Your converted data amount is `{} Terabits/Terabytes`".format(convertedinteger))
#||||||||||||||||||||||||||||||||||GIGABITS||||||||||||||||||||||||||||||||||||

    @data.command(name="gb2b", pass_context=False)
    async def _gb2b_data(self, userinput: int):
        """Gigabits/Gigabytes to Bits/Bytes, respectively"""

        convertedinteger = userinput * 1073741824

        await self.bot.say("Your converted data amount is `{} Bits/Bytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="gb2kb", pass_context=False)
    async def _gb2kb_data(self, userinput: int):
        """Gigabits/Gigabytes to Kilobits/Kilobytes, respectively"""

        convertedinteger = userinput * 1048576

        await self.bot.say("Your converted data amount is `{} Kilobits/Kilobytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="gb2mb", pass_context=False)
    async def _gb2mb_data(self, userinput: int):
        """Gigabits/Gigabytes to Kilobits/Kilobytes, respectively"""

        convertedinteger = userinput * 1024

        await self.bot.say("Your converted data amount is `{} Megabits/Megabytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="gb2tb", pass_context=False)
    async def _gb2tb_data(self, userinput: int):
        """Gigabits/Gigabytes to Terabits/Terabytes, respectively"""

        convertedinteger = userinput / 1024

        await self.bot.say("Your converted data amount is `{} Terabits/Terabytes`".format(convertedinteger))
#||||||||||||||||||||||||||||||||||TERABITS||||||||||||||||||||||||||||||||||||

    @data.command(name="tb2b", pass_context=False)
    async def _tb2b_data(self, userinput: int):
        """Terabits/Terabytes to Bits/Bytes, respectively"""

        convertedinteger = userinput * 1099511627776

        await self.bot.say("Your converted data amount is `{} Bits/Bytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="tb2kb", pass_context=False)
    async def _tb2kb_data(self, userinput: int):
        """Terabits/Terabytes to Kilobits/Kilobytes, respectively"""

        convertedinteger = userinput * 1073741824

        await self.bot.say("Your converted data amount is `{} Kilobits/Kilobytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="tb2mb", pass_context=False)
    async def _tb2mb_data(self, userinput: int):
        """Terabits/Terabytes to Megabits/Megabytes, respectively"""

        convertedinteger = userinput * 1048576

        await self.bot.say("Your converted data amount is `{} Megabits/Megabytes`".format(convertedinteger))
#------------------------------------------------------------------------------

    @data.command(name="tb2gb", pass_context=False)
    async def _tb2gb_data(self, userinput: int):
        """Terabits/Terabytes to Gigabits/Gigabytes, respectively"""

        convertedinteger = userinput * 1024

        await self.bot.say("Your converted data amount is `{} Gigabits/Gigabytes`".format(convertedinteger))
#------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||||||DEFINE|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------
# This tells the bot to add these commands to the help context


def setup(bot):
    n = UnitConverter(bot)
    bot.add_cog(n)
