import discord
from discord.ext import commands
from weather import get_weather
from latex import render_latex_to_image
import random as r
from datetime import datetime
import asyncio
import os
from bumbot import BumBot

class ShhhBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        intents = kwargs.pop('intents', discord.Intents.default())
        command_prefix = kwargs.pop('command_prefix', "!")

        super().__init__(command_prefix=command_prefix, intents=intents, *args, **kwargs)


    async def on_ready(self):
        print(f"ShhhBot is ready to perfom as {self.user} (ID: {self.user.id})")

intents = discord.Intents.default()
intents.message_content = True
bot = ShhhBot(command_prefix="!", intents=intents) 
bumbot = BumBot(intents=intents)


@bot.event
async def on_ready():
    return (f"Logged in as {bot.user}")


@bot.command()
async def help_me(ctx):
    response = "ShhhBot has different commands \n !bum : to find who's the bum (doesn't work anymore, still need some fixing) \n !weather location : to give the weather of a location \n !latex message :  to compile a message into LaTex (might not work well, still in developpement) \n !random number : lets the bot choose a random number from range(0,number) (Developping this command to create a small guessing game) \n !Shhh : the bot will send a famous picture \n !hello: the bot will greet to the author of the message"
    await ctx.send("You thought I was here to help you? :joy_cat: :thumbsdown:")
    await asyncio.sleep(2.0)
    await ctx.send("I'm just kidding")
    await ctx.send(response)


@bot.command()
async def hello(ctx):
    await ctx.send("I ain't no bum Bot sayin hello :joy_cat: :thumbsdown:")


@bot.command()
async def weather(ctx, *, country):
    weather_data, error = get_weather(country)
    if error:
        await ctx.send("Error fetching the data weather: {}".format(error))
        return
    response = (f"Weather in {country}:\n"
                f"Temperature: {weather_data['temperature']}°C\n"
                f"Condition: {weather_data['description']}\n")
    
    await ctx.send(response)


@bot.command()
async def latex(ctx, *, latex_code: str):
    try:
        image = render_latex_to_image(latex_code)

        buf = discord.File(image, filename="latex.png")
        await ctx.send(file=buf)
        return
    except Exception as e:
        await ctx.send("{} while producing the latex".format(e))


@bot.command()
async def random(ctx, *, number: int):
    try:
        if (int(number) == 0):
            await ctx.send("I can't choose a random number in a range of 0")
            return
        newn = r.randint(0, int(number))
        await ctx.send("I choose number {}".format(newn))
        return
    except Exception:
        await ctx.send("{} is not a number".format(number))
        return
    

@bot.command()
async def Shhh(ctx):
    paths = os.path.join('/Users', 'yann', 'Desktop', 'MyBot', 'MyBot', 'src', 'IMG_6700.JPG')
    if os.path.exists(paths):
        await ctx.send(file=discord.File(paths))
        return
    await ctx.send("The famous picture is lost :joy_cat: :thumbsdown:")

@bot.command()
@bot.has_permissions(ban_members=True)
async def tired(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"Shhh bro fr!!!")

        await asyncio.sleep(10.0)

        await ctx.guild.unban(member)
        await ctx.send("I really hope you're good because I won't hesitate to use this command again")
    
    except discord.Forbidden:
        await ctx.send("Only The Boy can do this!")
    
    except discord.HTTPException:
        await ctx.send("An error occurred while banning/unbanning the user.")

async def run_bot():
    await asyncio.gather(bot.start("your_token", reconnect=False), bumbot.start("your_second_token", reconnect=False))

if __name__ == "__main__":
    asyncio.run(run_bot())