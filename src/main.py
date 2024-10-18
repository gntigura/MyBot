import discord
from discord.ext import commands
from weather import get_weather
from latex import render_latex_to_image
import random as r
from datetime import datetime
import asyncio
import os

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
async def bum(ctx, *, message: str):
    ## Doesn't work, searching a way for a bot-user interaction if possible ##
    """
    ##So the bot doesn't respond to himself ##
    if message.author.id == bot.user.id:
        return
    if True:
        await message.send("Who's the bum? You got 10 seconds to respond (be careful on what you respond)")

        def check(m):
            return  m.author == message.author
    
        try:
            response = bot.wait_for('message', check=check,timeout=1000.0)
        except asyncio.TimeoutError :
            return await message.send("{} must really be a bum if it took you more than 10 seconds to make a choice".format(message.author.name))
    """
    if message.upper() == "YANN":
        await ctx.send("The Boy isn't a bum, he is your savior!")
        await ctx.send("ShhhBot has the permissions to ban users, so be careful of not spamming this command ;)")
        return
    else:
        await ctx.send("{} IS A BUM!!".format(ctx.upper()))
        return



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

def main():
    
    #bot.run("Your_token")
    return

if __name__ == "__main__":
    main()