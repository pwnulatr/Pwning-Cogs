# Sauce: rapidtables.com, checkyourmath.com & Wikipedia
# Coded by Pwnulatr with a ton of math help from Exbrandong
from discord.ext import commands
from __main__ import send_cmd_help

__author__ = "Pwnulatr"
__version__ = "0.2.1"


class UnitConverter:
    """Unit conversion tool"""

    def __init__(self, bot):
        self.bot = bot
# -----------------------------------------------------------------------------
# ||||||||||||||||||||||||||||||GROUP DEFINING|||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------------
# Defining the group command and if no subcommand is sent, send the help message

    @commands.group(pass_context=True)
    async def temperature(self, ctx):
        """Units of Temperature you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

# -----------------------------------------------------------------------------
    @commands.group(pass_context=True)
    async def speed(self, ctx):
        """Units of speed you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

# -----------------------------------------------------------------------------
    @commands.group(pass_context=True)
    async def length(self, ctx):
        """Units of distance you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

# -----------------------------------------------------------------------------
    @commands.group(pass_context=True)
    async def currency(self, ctx):
        """Units of currency you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

# -----------------------------------------------------------------------------
    @commands.group(pass_context=True)
    async def data(self, ctx):
        """Units of data you can convert (In binary form, ex. 1024 not 1000)"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

# -----------------------------------------------------------------------------
    @commands.group(pass_context=True)
    async def weight(self, ctx):
        """Units of weight you can convert"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

# -----------------------------------------------------------------------------
# |||||||||||||||||||||||||||||||TEMPERATURE|||||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------------
# And thus we begin the Copy-Paste abuse
    @temperature.command(name="f2c", pass_context=False)
    async def _f2c_temperature(self, userinput: float):
        """Fahrenheit to Celsius"""

        solved = (userinput - 32) / 1.8

        await self.bot.say(f"Your converted temperature is `{solved}°C`")

# -----------------------------------------------------------------------------
    @temperature.command(name="c2f", pass_context=False)
    async def _c2f_temperature(self, userinput: float):
        """Celsius to Fahrenheit"""

        solved = userinput * 1.8 + 32

        await self.bot.say(f"Your converted temperature is `{solved}°F`")

# -----------------------------------------------------------------------------
    @temperature.command(name="f2k", pass_context=False)
    async def _f2k_temperature(self, userinput: float):
        """Fahrenheit to Kelvin"""

        solved = (userinput + 459.67) * 5 / 9

        await self.bot.say(f"Your converted temperature is `{solved}°K`")

# -----------------------------------------------------------------------------
    @temperature.command(name="c2k", pass_context=False)
    async def _c2k_temperature(self, userinput: float):
        """Celsius to Kelvin"""

        solved = userinput + 273.15

        await self.bot.say(f"Your converted temperature is `{solved}°K`")

# -----------------------------------------------------------------------------
    @temperature.command(name="r2k", pass_context=False)
    async def _r2k_temperature(self, userinput: float):
        """Rankine to Kelvin"""

        solved = userinput * 5 / 9

        await self.bot.say(f"Your converted temperature is `{solved}°K`")

# -----------------------------------------------------------------------------
    @temperature.command(name="c2r", pass_context=False)
    async def _c2r_temperature(self, userinput: float):
        """Celsius to Rankine"""

        solved = (userinput + 273.15) * 9 / 5

        await self.bot.say(f"Your converted temperature is `{solved}°R`")

# -----------------------------------------------------------------------------
    @temperature.command(name="f2r", pass_context=False)
    async def _f2r_temperature(self, userinput: float):
        """Fahrenheit to Rankine"""

        solved = userinput + 459.67

        await self.bot.say(f"Your converted temperature is `{solved}°R`")

# -----------------------------------------------------------------------------
    @temperature.command(name="k2f", pass_context=False)
    async def _k2f_temperature(self, userinput: float):
        """Kelvin to Fahrenheit"""

        solved = userinput * 9 / 5 - 459.67

        await self.bot.say(f"Your converted temperature is `{solved}°F`")

# -----------------------------------------------------------------------------
    @temperature.command(name="k2c", pass_context=False)
    async def _k2c_temperature(self, userinput: float):
        """Kelvin to Celsius"""

        solved = userinput - 273.15

        await self.bot.say(f"Your converted temperature is `{solved}°C`")

# -----------------------------------------------------------------------------
    @temperature.command(name="k2r", pass_context=False)
    async def _k2r_temperature(self, userinput: float):
        """Kelvin to Rankine"""

        solved = userinput * 9 / 5

        await self.bot.say(f"Your converted temperature is `{solved}°R`")

# -----------------------------------------------------------------------------
    @temperature.command(name="r2f", pass_context=False)
    async def _r2f_temperature(self, userinput: float):
        """Rankine to Fahrenheit"""

        solved = userinput - 459.67

        await self.bot.say(f"Your converted temperature is `{solved}°F`")

# -----------------------------------------------------------------------------
    @temperature.command(name="r2c", pass_context=False)
    async def _r2c_temperature(self, userinput: float):
        """Rankine to Celsius"""

        solved = (userinput - 491.67) * 5 / 9

        await self.bot.say(f"Your converted temperature is `{solved}°C`")

# -----------------------------------------------------------------------------
# |||||||||||||||||||||||||||||||||||SPEED|||||||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------------
    @speed.command(name="mph2kmh", pass_context=False)
    async def _mph2kmh_speed(self, userinput: float):
        """Miles Per Hour to Kilometers Per Hour"""

        solved = userinput * 1.609344

        await self.bot.say(f"Your converted speed is `{solved} KMH`")

# -----------------------------------------------------------------------------
    @speed.command(name="kmh2mph", pass_context=False)
    async def _kmh2mph_speed(self, userinput: float):
        """Kilometers Per Hour to Miles Per Hour"""

        solved = userinput / 1.609344

        await self.bot.say(f"Your converted speed is `{solved} MPH`")

# -----------------------------------------------------------------------------
    @speed.command(name="mps2kmh", pass_context=False)
    async def _mps2kmh_speed(self, userinput: float):
        """Meters Per Second to Kilometers Per Hour"""

        solved = userinput * 3.6

        await self.bot.say(f"Your converted speed is `{solved} KMH`")

# -----------------------------------------------------------------------------
    @speed.command(name="kmh2mps", pass_context=False)
    async def _kmh2mps_speed(self, userinput: float):
        """Kilometers Per Hour to Meters Per Second"""

        solved = userinput / 3.6

        await self.bot.say(f"Your converted speed is `{solved} M/S`")

# -----------------------------------------------------------------------------
    @speed.command(name="fps2mph", pass_context=False)
    async def _fps2mph_speed(self, userinput: float):
        """Feet Per Second to Miles Per Hour"""

        solved = userinput / 1.46666666666667

        await self.bot.say(f"Your converted speed is `{solved} MPH`")

# -----------------------------------------------------------------------------
    @speed.command(name="mph2fps", pass_context=False)
    async def _mph2fps_speed(self, userinput: float):
        """Miles Per Hour to Feet Per Second"""

        solved = userinput * 1.46666666666667

        await self.bot.say(f"Your converted speed is `{solved} FPS`")

# -----------------------------------------------------------------------------
    @speed.command(name="knots2mph", pass_context=False)
    async def _knots2mph_speed(self, userinput: float):
        """Knots to Miles Per Hour"""

        solved = userinput * 1.15078

        await self.bot.say(f"Your converted speed is `{solved} MPH`")

# -----------------------------------------------------------------------------
    @speed.command(name="mph2knots", pass_context=False)
    async def _mph2knots_speed(self, userinput: float):
        """Miles Per Hour to Knots"""

        solved = userinput / 1.15078

        await self.bot.say(f"Your converted speed is `{solved} Knots`")

# -----------------------------------------------------------------------------
    @speed.command(name="kmh2knots", pass_context=False)
    async def _kmh2knots_speed(self, userinput: float):
        """Kilometers Per Hour to Knots"""

        anothaconversion = userinput / 1.609344
        solved = anothaconversion / 1.15078

        await self.bot.say(f"Your converted speed is `{solved} Knots`")

# -----------------------------------------------------------------------------
# ||||||||||||||||||||||||||||||||||LENGTH|||||||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------------
# Thanks Exbrandong for help with some of the math
    @length.command(name="cm2f", pass_context=False)
    async def _cm2f_length(self, userinput: float):
        """Centimeters to Feet"""

        solved = userinput / 30.48
        inches = solved * 12

        if solved < 1:
            await self.bot.say(f"Your converted length is `{solved} feet` or "
                               f"`0 feet {inches} inches`")
        else:
            remain_inch = inches - (12 * int(solved))
            floor_solved = int(solved)

            await self.bot.say(f"Your converted length is `{solved} feet` or "
                               f"`{floor_solved} feet {remain_inch} inches`")

# -----------------------------------------------------------------------------
    @length.command(name="cm2in", pass_context=False)
    async def _cm2in_length(self, userinput: float):
        """Centimeters to Inches"""

        solved = userinput / 2.54

        if solved < 12:
            await self.bot.say(f"Your converted length is `{solved} inches`")
        else:
            feet = solved / 12
            inches = solved - (12 * int(feet))
            floor_feet = int(feet)
            await self.bot.say(f"Your converted length is `{solved} inches` or"
                               f" `{floor_feet} feet {inches} inches`")

# -----------------------------------------------------------------------------
    @length.command(name="f2cm", pass_context=False)
    async def _f2cm_length(self, userinput: float):
        """Feet to Centimeters"""

        solved = userinput * 30.48

        await self.bot.say(f"Your converted length is `{solved} centimeters`")

# -----------------------------------------------------------------------------
    @length.command(name="cm2mm", pass_context=False)
    async def _cm2mm_length(self, userinput: float):
        """Centimeters to Millimeters"""

        solved = userinput * 10

        await self.bot.say(f"Your converted length is `{solved} Millimeters`")

# -----------------------------------------------------------------------------
    @length.command(name="f2mm", pass_context=False)
    async def _f2mm_length(self, userinput: float):
        """Feet to Millimeters"""

        solved = userinput * 304.8

        await self.bot.say(f"Your converted length is `{solved} Millimeters`")

# -----------------------------------------------------------------------------
    @length.command(name="f2in", pass_context=False)
    async def _f2in_length(self, userinput: float):
        """Feet to Inches"""

        solved = userinput * 12

        await self.bot.say(f"Your converted length is `{solved} Inches`")

# -----------------------------------------------------------------------------
    @length.command(name="f2m", pass_context=False)
    async def _f2m_length(self, userinput: float):
        """Feet to Meters"""

        solved = userinput * 0.3048

        await self.bot.say(f"Your converted length is `{solved} Meters`")

# -----------------------------------------------------------------------------
    @length.command(name="in2mm", pass_context=False)
    async def _in2mm_length(self, userinput: float):
        """Inches to Millimeters"""

        solved = userinput * 25.4

        await self.bot.say(f"Your converted length is `{solved} Millimeters`")

# -----------------------------------------------------------------------------
    @length.command(name="mm2in", pass_context=False)
    async def _mm2in_length(self, userinput: float):
        """Millimeters to Inches"""

        solved = userinput / 25.4

        await self.bot.say(f"Your converted length is `{solved} Inches`")


# -----------------------------------------------------------------------------
# |||||||||||||||||||||||||||||||||CURRENCY||||||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------------
    @currency.command(name="msp2dollar", pass_context=False)
    async def _msp2dollar_currency(self, userinput: float):
        """Microsoft Points to US/CA Dollars"""

        mathstuff = userinput / 80
        solved = round(mathstuff, 2)

        await self.bot.say(f"Your converted currency is `${solved}`")

# -----------------------------------------------------------------------------
    @currency.command(name="dollar2msp", pass_context=False)
    async def _dollar2msp_currency(self, userinput: float):
        """US/CA Dollars to Microsoft Points"""

        solved = userinput * 80

        await self.bot.say(f"Your converted currency is `{solved} Points`")

# -----------------------------------------------------------------------------
    @currency.command(name="platinum2usd", aliases=["plat2usd"], pass_context=False)
    async def _platinum2usd_currency(self, userinput: float):
        """Platinum (WarFrame currency) to US Dollars"""

        mathstuff = userinput / 15
        solved = round(mathstuff, 2)

        await self.bot.say(f"Your converted currency is `${solved}`")

# -----------------------------------------------------------------------------
    @currency.command(name="usd2platinum", aliases=["usd2plat"], pass_context=False)
    async def _usd2platinum_currency(self, userinput: float):
        """US Dollars to Platinum (WarFrame currency)"""

        solved = userinput * 15

        await self.bot.say(f"Your converted currency is `{solved} Platinum`")

# -----------------------------------------------------------------------------
    @currency.command(name="platinum2cad", aliases=["plat2cad"], pass_context=False)
    async def _platinum2cad_currency(self, userinput: float):
        """Platinum (WarFrame currency) to CA Dollars"""

        mathstuff = userinput / 13.66120218579235
        solved = round(mathstuff, 2)

        await self.bot.say(f"Your converted currency is `${solved}`")

# -----------------------------------------------------------------------------
    @currency.command(name="cad2platinum", aliases=["cad2plat"], pass_context=False)
    async def _cad2platinum_currency(self, userinput: float):
        """CA Dollars to Platinum (WarFrame currency)"""

        mathstuff = userinput * 13.66120218579235
        solved = round(mathstuff)

        await self.bot.say(f"Your converted currency is `{solved} Platinum`")

# -----------------------------------------------------------------------------
# 1 Bit = 0.014 USD when dividing 7 by 500 because it costs $7 for 500 bits.
    @currency.command(name="twitchbits2usd", aliases=["bits2usd"], pass_context=False)
    async def _twitchbits_currency(self, userinput: int):
        """Twitch Bits to US Dollars"""

        mathstuff = userinput * 0.014
        solved = round(mathstuff, 2)

        await self.bot.say(f"Your converted currency is `${solved}`")

# -----------------------------------------------------------------------------
    @currency.command(name="usd2twitchbits", aliases=["usd2bits"], pass_context=False)
    async def _usd2twitchbits_currency(self, userinput: float):
        """US Dollars to Twitch Bits"""

        mathstuff = userinput / 0.014
        solved = round(mathstuff)

        await self.bot.say(f"Your converted currency is `{solved} bits`")

# -----------------------------------------------------------------------------
    @currency.command(name="r6credits2usd", aliases=["r62usd"], pass_context=False)
    async def _r6credits2usd_currency(self, userinput: float):
        """Rainbow Six Credits to US Dollars"""

        mathstuff = userinput / 120
        solved = round(mathstuff, 2)

        await self.bot.say(f"Your converted currency is `${solved}`")

# -----------------------------------------------------------------------------
    @currency.command(name="usd2r6credits", aliases=["usd2r6"], pass_context=False)
    async def _usd2twitchbits_currency(self, userinput: float):
        """US Dollars to Rainbow Six Credits"""

        mathstuff = userinput * 120
        solved = round(mathstuff)

        await self.bot.say(f"Your converted currency is `{solved} Rainbow Six Credits`")

# -----------------------------------------------------------------------------
    @currency.command(name="destinysilver2usd", aliases=["d2silver2usd"], pass_context=False)
    async def _destinysilver2usd_currency(self, userinput: float):
        """Destiny 2 Silver (Premium currency) to US Dollars"""

        mathstuff = userinput / 100
        solved = round(mathstuff, 2)

        await self.bot.say(f"Your converted currency is `${solved}`")

# -----------------------------------------------------------------------------
    @currency.command(name="usd2destinysilver", aliases=["usd2d2silver"], pass_context=False)
    async def _usd2destinysilver_currency(self, userinput: float):
        """US Dollars to Destiny 2 Silver (Premium currency)"""

        mathstuff = userinput * 100
        solved = round(mathstuff)

        await self.bot.say(f"Your converted currency is `{solved} Silver`")

# -----------------------------------------------------------------------------
# |||||||||||||||||||||||||||||||||||DATA||||||||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------------
    @data.command(name="bits2bytes", pass_context=False)
    async def _bits2bytes_data(self, userinput: float):
        """Bits to Bytes (will work with any data prefix if converting to same prefix)"""

        solved = userinput / 8

        await self.bot.say(f"Your converted data amount is `{solved} bytes`")

# -----------------------------------------------------------------------------
    @data.command(name="bytes2bits", pass_context=False)
    async def _bytes2bits_data(self, userinput: float):
        """Bytes to Bits (will work with any data prefix if converting to same prefix)"""

        solved = userinput * 8

        await self.bot.say(f"Your converted data amount is `{solved} bits`")

# -----------------------------------------------------------------------------
    @data.command(name="b2kb", pass_context=False)
    async def _b2kb_data(self, userinput: float):
        """Bits/Bytes to Kilobits/Kilobytes, respectively"""

        solved = userinput / 1024

        await self.bot.say(f"Your converted data amount is `{solved} Kilobits/Kilobytes`")

# -----------------------------------------------------------------------------
    @data.command(name="b2mb", pass_context=False)
    async def _b2mb_data(self, userinput: float):
        """Bits/Bytes to Megabits/Megabytes, respectively"""

        solved = userinput / 1048576

        await self.bot.say(f"Your converted data amount is `{solved} Megabits/Megabytes`")

# -----------------------------------------------------------------------------
    @data.command(name="b2gb", pass_context=False)
    async def _b2gb_data(self, userinput: float):
        """Bits/Bytes to Gigabits/Gigabytes, respectively"""

        solved = userinput / 1073741824

        await self.bot.say(f"Your converted data amount is `{solved} Gigabits/Gigabytes`")

# -----------------------------------------------------------------------------
    @data.command(name="b2tb", pass_context=False)
    async def _b2tb_data(self, userinput: float):
        """Bits/Bytes to Terabits/Terabytes, respectively"""

        solved = userinput / 1099511627776

        await self.bot.say(f"Your converted data amount is `{solved} Terabits/Terabytes`")

# |||||||||||||||||||||||||||||||||KILOBITS||||||||||||||||||||||||||||||||||||
    @data.command(name="kb2b", pass_context=False)
    async def _kb2b_data(self, userinput: float):
        """Kilobits/Kilobytes to Bits/Bytes, respectively"""

        solved = userinput * 1024

        await self.bot.say(f"Your converted data amount is `{solved} Bits/Bytes`")

# -----------------------------------------------------------------------------
    @data.command(name="kb2mb", pass_context=False)
    async def _kb2mb_data(self, userinput: float):
        """Kilobits/Kilobytes to Megabits/Megabytes, respectively"""

        solved = userinput / 1024

        await self.bot.say(f"Your converted data amount is `{solved} Megabits/Megabytes`")

# -----------------------------------------------------------------------------
    @data.command(name="kb2gb", pass_context=False)
    async def _kb2gb_data(self, userinput: float):
        """Kilobits/Kilobytes to Gigabits/Gigabytes, respectively"""

        solved = userinput / 1048576

        await self.bot.say(f"Your converted data amount is `{solved} Gigabits/Gigabytes`")

# -----------------------------------------------------------------------------
    @data.command(name="kb2tb", pass_context=False)
    async def _kb2tb_data(self, userinput: float):
        """Kilobits/Kilobytes to Gigabits/Gigabytes, respectively"""

        solved = userinput / 1073741824

        await self.bot.say(f"Your converted data amount is `{solved} Terabits/Terabytes`")

# |||||||||||||||||||||||||||||||||MEGABITS||||||||||||||||||||||||||||||||||||
    @data.command(name="mb2b", pass_context=False)
    async def _mb2b_data(self, userinput: float):
        """Megabits/Megabytes to Bits/Bytes, respectively"""

        solved = userinput * 1048576

        await self.bot.say(f"Your converted data amount is `{solved} Bits/Bytes`")

# -----------------------------------------------------------------------------
    @data.command(name="mb2kb", pass_context=False)
    async def _mb2kb_data(self, userinput: float):
        """Megabits/Megabytes to Kilobits/Kilobytes, respectively"""

        solved = userinput * 1024

        await self.bot.say(f"Your converted data amount is `{solved} Kilobits/Kilobytes`")

# -----------------------------------------------------------------------------
    @data.command(name="mb2gb", pass_context=False)
    async def _mb2gb_data(self, userinput: float):
        """Megabits/Megabytes to Gigabits/Gigabytes, respectively"""

        solved = userinput / 1024

        await self.bot.say(f"Your converted data amount is `{solved} Gigabits/Gigabytes`")

# -----------------------------------------------------------------------------
    @data.command(name="mb2tb", pass_context=False)
    async def _mb2tb_data(self, userinput: float):
        """Megabits/Megabytes to Terabits/Terabytes, respectively"""

        solved = userinput / 1048576

        await self.bot.say(f"Your converted data amount is `{solved} Terabits/Terabytes`")

# |||||||||||||||||||||||||||||||||GIGABITS||||||||||||||||||||||||||||||||||||
    @data.command(name="gb2b", pass_context=False)
    async def _gb2b_data(self, userinput: float):
        """Gigabits/Gigabytes to Bits/Bytes, respectively"""

        solved = userinput * 1073741824

        await self.bot.say(f"Your converted data amount is `{solved} Bits/Bytes`")

# -----------------------------------------------------------------------------
    @data.command(name="gb2kb", pass_context=False)
    async def _gb2kb_data(self, userinput: float):
        """Gigabits/Gigabytes to Kilobits/Kilobytes, respectively"""

        solved = userinput * 1048576

        await self.bot.say(f"Your converted data amount is `{solved} Kilobits/Kilobytes`")

# -----------------------------------------------------------------------------
    @data.command(name="gb2mb", pass_context=False)
    async def _gb2mb_data(self, userinput: float):
        """Gigabits/Gigabytes to Kilobits/Kilobytes, respectively"""

        solved = userinput * 1024

        await self.bot.say(f"Your converted data amount is `{solved} Megabits/Megabytes`")

# -----------------------------------------------------------------------------
    @data.command(name="gb2tb", pass_context=False)
    async def _gb2tb_data(self, userinput: float):
        """Gigabits/Gigabytes to Terabits/Terabytes, respectively"""

        solved = userinput / 1024

        await self.bot.say(f"Your converted data amount is `{solved} Terabits/Terabytes`")

# |||||||||||||||||||||||||||||||||TERABITS||||||||||||||||||||||||||||||||||||
    @data.command(name="tb2b", pass_context=False)
    async def _tb2b_data(self, userinput: float):
        """Terabits/Terabytes to Bits/Bytes, respectively"""

        solved = userinput * 1099511627776

        await self.bot.say(f"Your converted data amount is `{solved} Bits/Bytes`")

# -----------------------------------------------------------------------------
    @data.command(name="tb2kb", pass_context=False)
    async def _tb2kb_data(self, userinput: float):
        """Terabits/Terabytes to Kilobits/Kilobytes, respectively"""

        solved = userinput * 1073741824

        await self.bot.say(f"Your converted data amount is `{solved} Kilobits/Kilobytes`")

# -----------------------------------------------------------------------------
    @data.command(name="tb2mb", pass_context=False)
    async def _tb2mb_data(self, userinput: float):
        """Terabits/Terabytes to Megabits/Megabytes, respectively"""

        solved = userinput * 1048576

        await self.bot.say(f"Your converted data amount is `{solved} Megabits/Megabytes`")

# -----------------------------------------------------------------------------
    @data.command(name="tb2gb", pass_context=False)
    async def _tb2gb_data(self, userinput: float):
        """Terabits/Terabytes to Gigabits/Gigabytes, respectively"""

        solved = userinput * 1024

        await self.bot.say(f"Your converted data amount is `{solved} Gigabits/Gigabytes`")

# -----------------------------------------------------------------------------
# ||||||||||||||||||||||||||||||||||WEIGHT|||||||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------------
    @weight.command(name="g2oz", pass_context=False)
    async def _g2oz_weight(self, userinput: float):
        """Grams to Ounces"""

        solved = userinput / 28.34952

        await self.bot.say(f"Your converted weight is `{solved} oz`")

# -----------------------------------------------------------------------------
    @weight.command(name="g2lbs", pass_context=False)
    async def _g2lbs_weight(self, userinput: float):
        """Grams to Pounds"""

        solved = userinput / 453.59237

        await self.bot.say(f"Your converted weight is `{solved} lbs`")

# -----------------------------------------------------------------------------
    @weight.command(name="oz2g", pass_context=False)
    async def _oz2g_weight(self, userinput: float):
        """Ounces to Grams"""

        solved = userinput * 28.34952

        await self.bot.say(f"Your converted weight is `{solved} g`")

# -----------------------------------------------------------------------------
    @weight.command(name="oz2lbs", pass_context=False)
    async def _oz2lbs_weight(self, userinput: float):
        """Ounces to Pounds"""

        solved = userinput / 16

        await self.bot.say(f"Your converted weight is `{solved} lbs`")

# -----------------------------------------------------------------------------
    @weight.command(name="oz2kg", pass_context=False)
    async def _oz2kg_weight(self, userinput: float):
        """Ounces to Kilograms"""

        solved = userinput * 0.02834952

        await self.bot.say(f"Your converted weight is `{solved} kg`")

# -----------------------------------------------------------------------------
    @weight.command(name="lbs2g", pass_context=False)
    async def _lbs2g_weight(self, userinput: float):
        """Pounds to Grams"""

        solved = userinput * 453.59237

        await self.bot.say(f"Your converted weight is `{solved} g`")

# -----------------------------------------------------------------------------
    @weight.command(name="lbs2oz", pass_context=False)
    async def _lbs2oz_weight(self, userinput: float):
        """Pounds to Ounces"""

        solved = userinput * 16

        await self.bot.say(f"Your converted weight is `{solved} oz`")

# -----------------------------------------------------------------------------
    @weight.command(name="lbs2s", aliases=["lbs2stones"], pass_context=False)
    async def _lbs2s_weight(self, userinput: float):
        """Pounds to Stones"""

        solved = userinput / 14

        await self.bot.say(f"Your converted weight is `{solved} Stones`")

# -----------------------------------------------------------------------------
    @weight.command(name="lbs2t", aliases=["lbs2tons"], pass_context=False)
    async def _lbs2t_weight(self, userinput: float):
        """Pounds to Metric Tons"""

        solved = userinput * 0.00045359237

        await self.bot.say(f"Your converted weight is `{solved} Tons`")

# -----------------------------------------------------------------------------
    @weight.command(name="kg2oz", pass_context=False)
    async def _kg2oz_weight(self, userinput: float):
        """Kilograms to Ounces"""

        solved = userinput / 0.02834952

        await self.bot.say(f"Your converted weight is `{solved} oz`")

# -----------------------------------------------------------------------------
    @weight.command(name="kg2lbs", pass_context=False)
    async def _kg2lbs_weight(self, userinput: float):
        """Kilograms to Pounds"""

        solved = userinput / 0.45359237

        await self.bot.say(f"Your converted weight is `{solved} lbs`")

# -----------------------------------------------------------------------------
    @weight.command(name="s2lbs", aliases=["stones2lbs"], pass_context=False)
    async def _s2lbs_weight(self, userinput: float):
        """Stones to Pounds"""

        solved = userinput * 14

        await self.bot.say(f"Your converted weight is `{solved} lbs`")

# -----------------------------------------------------------------------------
    @weight.command(name="t2lbs", aliases=["tons2lbs"], pass_context=False)
    async def _t2lbs_weight(self, userinput: float):
        """Metric Tons to Pounds"""

        solved = userinput / 0.00045359237

        await self.bot.say(f"Your converted weight is `{solved} lbs`")


# -----------------------------------------------------------------------------
# ||||||||||||||||||||||||||||||||||DEFINE|||||||||||||||||||||||||||||||||||||
# -----------------------------------------------------------------------------
def setup(bot):
    n = UnitConverter(bot)
    bot.add_cog(n)
