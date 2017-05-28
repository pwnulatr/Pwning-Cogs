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
    async def temperature(self, ctx):
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

    @temperature.command(name="f2c", pass_context=False)
    async def _f2c_temperature(self, userinput: float):
        """Fahrenheit to Celsius"""

        convertednumber = (userinput - 32) / 1.8

        await self.bot.say("Your converted temperature is `{}°C`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="c2f", pass_context=False)
    async def _c2f_temperature(self, userinput: float):
        """Celsius to Fahrenheit"""

        convertednumber = userinput * 1.8 + 32

        await self.bot.say("Your converted temperature is `{}°F`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="f2k", pass_context=False)
    async def _f2k_temperature(self, userinput: float):
        """Fahrenheit to Kelvin"""

        convertednumber = (userinput + 459.67) * 5 / 9

        await self.bot.say("Your converted temperature is `{}°K`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="c2k", pass_context=False)
    async def _c2k_temperature(self, userinput: float):
        """Celsius to Kelvin"""

        convertednumber = userinput + 273.15

        await self.bot.say("Your converted temperature is `{}°K`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="r2k", pass_context=False)
    async def _r2k_temperature(self, userinput: float):
        """Rankine to Kelvin"""

        convertednumber = userinput * 5 / 9

        await self.bot.say("Your converted temperature is `{}°K`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="c2r", pass_context=False)
    async def _c2r_temperature(self, userinput: float):
        """Celsius to Rankine"""

        convertednumber = (userinput + 273.15) * 9 / 5

        await self.bot.say("Your converted temperature is `{}°R`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="f2r", pass_context=False)
    async def _f2r_temperature(self, userinput: float):
        """Fahrenheit to Rankine"""

        convertednumber = userinput + 459.67

        await self.bot.say("Your converted temperature is `{}°R`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="k2f", pass_context=False)
    async def _k2f_temperature(self, userinput: float):
        """Kelvin to Fahrenheit"""

        convertednumber = userinput * 9 / 5 - 459.67

        await self.bot.say("Your converted temperature is `{}°F`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="k2c", pass_context=False)
    async def _k2c_temperature(self, userinput: float):
        """Kelvin to Celsius"""

        convertednumber = userinput - 273.15

        await self.bot.say("Your converted temperature is `{}°C`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="k2r", pass_context=False)
    async def _k2r_temperature(self, userinput: float):
        """Kelvin to Rankine"""

        convertednumber = userinput * 9 / 5

        await self.bot.say("Your converted temperature is `{}°R`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="r2f", pass_context=False)
    async def _r2f_temperature(self, userinput: float):
        """Rankine to Fahrenheit"""

        convertednumber = userinput - 459.67

        await self.bot.say("Your converted temperature is `{}°F`".format(convertednumber))
#------------------------------------------------------------------------------

    @temperature.command(name="r2c", pass_context=False)
    async def _r2c_temperature(self, userinput: float):
        """Rankine to Celsius"""

        convertednumber = (userinput - 491.67) * 5 / 9

        await self.bot.say("Your converted temperature is `{}°C`".format(convertednumber))
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||SPEED|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

    @speed.command(name="mph2kmh", pass_context=False)
    async def _mph2kmh_speed(self, userinput: float):
        """Miles Per Hour to Kilometers Per Hour"""

        convertednumber = userinput * 1.609344

        await self.bot.say("Your converted speed is `{} KMH`".format(convertednumber))
#------------------------------------------------------------------------------

    @speed.command(name="kmh2mph", pass_context=False)
    async def _kmh2mph_speed(self, userinput: float):
        """Kilometers Per Hour to Miles Per Hour"""

        convertednumber = userinput / 1.609344

        await self.bot.say("Your converted speed is `{} MPH`".format(convertednumber))
#------------------------------------------------------------------------------

    @speed.command(name="mps2kmh", pass_context=False)
    async def _mps2kmh_speed(self, userinput: float):
        """Meters Per Second to Kilometers Per Hour"""

        convertednumber = userinput * 3.6

        await self.bot.say("Your converted speed is `{} KMH`".format(convertednumber))
#------------------------------------------------------------------------------

    @speed.command(name="kmh2mps", pass_context=False)
    async def _kmh2mps_speed(self, userinput: float):
        """Kilometers Per Hour to Meters Per Second"""

        convertednumber = userinput / 3.6

        await self.bot.say("Your converted speed is `{} M/S`".format(convertednumber))
#------------------------------------------------------------------------------

    @speed.command(name="fps2mph", pass_context=False)
    async def _fps2mph_speed(self, userinput: float):
        """Feet Per Second to Miles Per Hour"""

        convertednumber = userinput / 1.46666666666667

        await self.bot.say("Your converted speed is `{} MPH`".format(convertednumber))
#------------------------------------------------------------------------------

    @speed.command(name="mph2fps", pass_context=False)
    async def _mph2fps_speed(self, userinput: float):
        """Miles Per Hour to Feet Per Second"""

        convertednumber = userinput * 1.46666666666667

        await self.bot.say("Your converted speed is `{} FPS`".format(convertednumber))
#------------------------------------------------------------------------------

    @speed.command(name="knots2mph", pass_context=False)
    async def _knots2mph_speed(self, userinput: float):
        """Knots to Miles Per Hour"""

        convertednumber = userinput * 1.15078

        await self.bot.say("Your converted speed is `{} MPH`".format(convertednumber))
#------------------------------------------------------------------------------

    @speed.command(name="mph2knots", pass_context=False)
    async def _mph2knots_speed(self, userinput: float):
        """Miles Per Hour to Knots"""

        convertednumber = userinput / 1.15078

        await self.bot.say("Your converted speed is `{} Knots`".format(convertednumber))
#------------------------------------------------------------------------------

    @speed.command(name="kmh2knots", pass_context=False)
    async def _kmh2knots_speed(self, userinput: float):
        """Kilometers Per Hour to Knots"""

        anothaconversion = userinput / 1.609344
        convertednumber = anothaconversion / 1.15078

        await self.bot.say("Your converted speed is `{} Knots`".format(convertednumber))
#------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||||||LENGTH|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

    @length.command(name="cm2f", pass_context=False)
    async def _cm2f_length(self, userinput: float):
        """Centimeters to Feet"""

        convertednumber = userinput / 30.48
        inches = convertednumber * 12

        if convertednumber < 1:
            await self.bot.say("Your converted length is `{} feet` or `0 feet {} inches`".format(convertednumber, inches))
        else:
            remaininch = inches - (12 * int(convertednumber))
            await self.bot.say("Your converted length is `" + str(convertednumber) + " feet` or `" + str(int(convertednumber)) + " feet " + str(remaininch) + " inches`")
# Thanks for the help with the math Exbrandong :D couldn't have done it w/o you
#------------------------------------------------------------------------------

    @length.command(name="cm2in", pass_context=False)
    async def _cm2in_length(self, userinput: float):
        """Centimeters to Inches"""

        convertednumber = userinput / 2.54

        if convertednumber < 12:
            await self.bot.say("Your converted length is `{} inches`".format(convertednumber))
        else:
            feet = convertednumber / 12
            inches = convertednumber - (12 * int(feet))
            await self.bot.say("Your converted length is `" + str(convertednumber) + " inches` or `" + str(int(feet)) + " feet " + str(inches) + " inches`")
#------------------------------------------------------------------------------

    @length.command(name="f2cm", pass_context=False)
    async def _f2cm_length(self, userinput: float):
        """Feet to Centimeters"""

        convertednumber = userinput * 30.48

        await self.bot.say("Your converted length is `{} centimeters`".format(convertednumber))
#------------------------------------------------------------------------------

    @length.command(name="cm2mm", pass_context=False)
    async def _cm2mm_length(self, userinput: float):
        """Centimeters to Millimeters"""

        convertednumber = userinput * 10

        await self.bot.say("Your converted length is `{} Millimeters`")
#------------------------------------------------------------------------------

    @length.command(name="f2mm", pass_context=False)
    async def _f2mm_length(self, userinput: float):
        """Feet to Millimeters"""

        convertednumber = userinput * 304.8

        await self.bot.say("Your converted length is `{} Millimeters`".format(convertednumber))
#------------------------------------------------------------------------------

    @length.command(name="f2in", pass_context=False)
    async def _f2in_length(self, userinput: float):
        """Feet to Inches"""

        convertednumber = userinput * 12

        await self.bot.say("Your converted length is `{} Inches`".format(convertednumber))
#------------------------------------------------------------------------------

    @length.command(name="f2m", pass_context=False)
    async def _f2m_length(self, userinput: float):
        """Feet to Meters"""

        convertednumber = userinput * 0.3048

        await self.bot.say("Your converted length is `{} Meters`".format(convertednumber))
#------------------------------------------------------------------------------

    @length.command(name="height", pass_context=False)
    async def _height_length(self, metric_or_customary, feet_or_meters : float, inches_or_centimeters : float):
        """Converts from metric height to customary height or vice versa"""

        if metric_or_customary == "metric":

#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||CURRENCY||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

    @currency.command(name="msp2dollar", pass_context=False)
    async def _msp2dollar_currency(self, userinput: float):
        """Microsoft Points to US/CA Dollars"""

        mathstuff = userinput / 80
        convertednumber = round(mathstuff, 2)

        await self.bot.say("Your converted currency is `${}`".format(convertednumber))
#------------------------------------------------------------------------------

    @currency.command(name="dollar2msp", pass_context=False)
    async def _dollar2msp_currency(self, userinput: float):
        """US/CA Dollars to Microsoft Points"""

        convertednumber = userinput * 80

        await self.bot.say("Your converted currency is `{} Points`".format(convertednumber))
#------------------------------------------------------------------------------

    @currency.command(name="platinum2usd", aliases=["plat2usd"], pass_context=False)
    async def _platinum2usd_currency(self, userinput: float):
        """Platinum (WarFrame currency) to US Dollars"""

        mathstuff = userinput / 15
        convertednumber = round(mathstuff, 2)

        await self.bot.say("Your converted currency is `${}`".format(convertednumber))
#------------------------------------------------------------------------------

    @currency.command(name="usd2platinum", aliases=["usd2plat"], pass_context=False)
    async def _usd2platinum_currency(self, userinput: float):
        """US Dollars to Platinum (WarFrame currency)"""

        convertednumber = userinput * 15

        await self.bot.say("Your converted currency is `{} Platinum`".format(convertednumber))
#------------------------------------------------------------------------------

    @currency.command(name="platinum2cad", aliases=["plat2cad"], pass_context=False)
    async def _platinum2cad_currency(self, userinput: float):
        """Platinum (WarFrame currency) to CA Dollars"""

        mathstuff = userinput / 13.66120218579235
        convertednumber = round(mathstuff, 2)

        await self.bot.say("Your converted currency is `${}`".format(convertednumber))
#------------------------------------------------------------------------------

    @currency.command(name="cad2platinum", aliases=["cad2plat"], pass_context=False)
    async def _cad2platinum_currency(self, userinput: float):
        """CA Dollars to Platinum (WarFrame currency)"""

        mathstuff = userinput * 13.66120218579235
        convertednumber = round(mathstuff)

        await self.bot.say("Your converted currency is `{} Platinum`".format(convertednumber))
#------------------------------------------------------------------------------
#||||||||||||||||||||||||||||||||||||DATA||||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

    @data.command(name="bits2bytes", pass_context=False)
    async def _bits2bytes_data(self, userinput: float):
        """Bits to Bytes (will work with any data prefix if converting to same prefix)"""

        convertednumber = userinput / 8

        await self.bot.say("Your converted data amount is `{} bytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="bytes2bits", pass_context=False)
    async def _bytes2bits_data(self, userinput: float):
        """Bytes to Bits (will work with any data prefix if converting to same prefix)"""

        convertednumber = userinput * 8

        await self.bot.say("Your converted data amount is `{} bits`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="b2kb", pass_context=False)
    async def _b2kb_data(self, userinput: float):
        """Bits/Bytes to Kilobits/Kilobytes, respectively"""

        convertednumber = userinput / 1024

        await self.bot.say("Your converted data amount is `{} Kilobits/Kilobytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="b2mb", pass_context=False)
    async def _b2mb_data(self, userinput: float):
        """Bits/Bytes to Megabits/Megabytes, respectively"""

        convertednumber = userinput / 1048576

        await self.bot.say("Your converted data amount is `{} Megabits/Megabytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="b2gb", pass_context=False)
    async def _b2gb_data(self, userinput: float):
        """Bits/Bytes to Gigabits/Gigabytes, respectively"""

        convertednumber = userinput / 1073741824

        await self.bot.say("Your converted data amount is `{} Gigabits/Gigabytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="b2tb", pass_context=False)
    async def _b2tb_data(self, userinput: float):
        """Bits/Bytes to Terabits/Terabytes, respectively"""

        convertednumber = userinput / 1099511627776

        await self.bot.say("Your converted data amount is `{} Terabits/Terabytes`".format(convertednumber))
#||||||||||||||||||||||||||||||||||KILOBITS||||||||||||||||||||||||||||||||||||

    @data.command(name="kb2b", pass_context=False)
    async def _kb2b_data(self, userinput: float):
        """Kilobits/Kilobytes to Bits/Bytes, respectively"""

        convertednumber = userinput * 1024

        await self.bot.say("Your converted data amount is `{} Bits/Bytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="kb2mb", pass_context=False)
    async def _kb2mb_data(self, userinput: float):
        """Kilobits/Kilobytes to Megabits/Megabytes, respectively"""

        convertednumber = userinput / 1024

        await self.bot.say("Your converted data amount is `{} Megabits/Megabytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="kb2gb", pass_context=False)
    async def _kb2gb_data(self, userinput: float):
        """Kilobits/Kilobytes to Gigabits/Gigabytes, respectively"""

        convertednumber = userinput / 1048576

        await self.bot.say("Your converted data amount is `{} Gigabits/Gigabytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="kb2tb", pass_context=False)
    async def _kb2tb_data(self, userinput: float):
        """Kilobits/Kilobytes to Gigabits/Gigabytes, respectively"""

        convertednumber = userinput / 1073741824

        await self.bot.say("Your converted data amount is `{} Terabits/Terabytes`".format(convertednumber))
#||||||||||||||||||||||||||||||||||MEGABITS||||||||||||||||||||||||||||||||||||

    @data.command(name="mb2b", pass_context=False)
    async def _mb2b_data(self, userinput: float):
        """Megabits/Megabytes to Bits/Bytes, respectively"""

        convertednumber = userinput * 1048576

        await self.bot.say("Your converted data amount is `{} Bits/Bytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="mb2kb", pass_context=False)
    async def _mb2kb_data(self, userinput: float):
        """Megabits/Megabytes to Kilobits/Kilobytes, respectively"""

        convertednumber = userinput * 1024

        await self.bot.say("Your converted data amount is `{} Kilobits/Kilobytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="mb2gb", pass_context=False)
    async def _mb2gb_data(self, userinput: float):
        """Megabits/Megabytes to Gigabits/Gigabytes, respectively"""

        convertednumber = userinput / 1024

        await self.bot.say("Your converted data amount is `{} Gigabits/Gigabytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="mb2tb", pass_context=False)
    async def _mb2tb_data(self, userinput: float):
        """Megabits/Megabytes to Terabits/Terabytes, respectively"""

        convertednumber = userinput / 1048576

        await self.bot.say("Your converted data amount is `{} Terabits/Terabytes`".format(convertednumber))
#||||||||||||||||||||||||||||||||||GIGABITS||||||||||||||||||||||||||||||||||||

    @data.command(name="gb2b", pass_context=False)
    async def _gb2b_data(self, userinput: float):
        """Gigabits/Gigabytes to Bits/Bytes, respectively"""

        convertednumber = userinput * 1073741824

        await self.bot.say("Your converted data amount is `{} Bits/Bytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="gb2kb", pass_context=False)
    async def _gb2kb_data(self, userinput: float):
        """Gigabits/Gigabytes to Kilobits/Kilobytes, respectively"""

        convertednumber = userinput * 1048576

        await self.bot.say("Your converted data amount is `{} Kilobits/Kilobytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="gb2mb", pass_context=False)
    async def _gb2mb_data(self, userinput: float):
        """Gigabits/Gigabytes to Kilobits/Kilobytes, respectively"""

        convertednumber = userinput * 1024

        await self.bot.say("Your converted data amount is `{} Megabits/Megabytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="gb2tb", pass_context=False)
    async def _gb2tb_data(self, userinput: float):
        """Gigabits/Gigabytes to Terabits/Terabytes, respectively"""

        convertednumber = userinput / 1024

        await self.bot.say("Your converted data amount is `{} Terabits/Terabytes`".format(convertednumber))
#||||||||||||||||||||||||||||||||||TERABITS||||||||||||||||||||||||||||||||||||

    @data.command(name="tb2b", pass_context=False)
    async def _tb2b_data(self, userinput: float):
        """Terabits/Terabytes to Bits/Bytes, respectively"""

        convertednumber = userinput * 1099511627776

        await self.bot.say("Your converted data amount is `{} Bits/Bytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="tb2kb", pass_context=False)
    async def _tb2kb_data(self, userinput: float):
        """Terabits/Terabytes to Kilobits/Kilobytes, respectively"""

        convertednumber = userinput * 1073741824

        await self.bot.say("Your converted data amount is `{} Kilobits/Kilobytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="tb2mb", pass_context=False)
    async def _tb2mb_data(self, userinput: float):
        """Terabits/Terabytes to Megabits/Megabytes, respectively"""

        convertednumber = userinput * 1048576

        await self.bot.say("Your converted data amount is `{} Megabits/Megabytes`".format(convertednumber))
#------------------------------------------------------------------------------

    @data.command(name="tb2gb", pass_context=False)
    async def _tb2gb_data(self, userinput: float):
        """Terabits/Terabytes to Gigabits/Gigabytes, respectively"""

        convertednumber = userinput * 1024

        await self.bot.say("Your converted data amount is `{} Gigabits/Gigabytes`".format(convertednumber))
#------------------------------------------------------------------------------
#|||||||||||||||||||||||||||||||||||DEFINE|||||||||||||||||||||||||||||||||||||
#------------------------------------------------------------------------------

def setup(bot):
    n = UnitConverter(bot)
    bot.add_cog(n)
