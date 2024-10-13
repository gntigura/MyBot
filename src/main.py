import discord
from discord.ext import commands
from weather import get_weather
from latex import render_latex_to_image
import random as r
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents) 

@bot.event
async def on_ready():
    return (f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.member.displayName}!\n Today we are the {datetime.now()}!")

@bot.command()
async def weather(ctx, country):
    weather_data, error = get_weather(country)
    if error:
        await ctx.send("Error fetching the data weather: {}".format(error))
        return
    response = (f"Weather in {country}:\n"
                f"Temperature: {weather_data['temperature']}°C\n"
                f"Condition: {weather_data['description']}\n")
    
    await ctx.send(response)

@bot.command()
async def latex(ctx, *, latex_code):
    try:
        image = render_latex_to_image(latex_code)

        file = discord.File(image, filename="latex.png")
        await ctx.send(file)
        return
    except Exception as e:
        await ctx.send("{} while producing the latex".format(e))

@bot.command()
async def random(ctx, *, number):
    try:
        nbr = int(number)
        if (number == 0):
            await ctx.send("I can't choose a random number in a range of 0")
            return
        newn = r.choice(nbr)
        await ctx.send("I choose number {}".format(newn))
        return
    except Exception:
        await ctx.send("This is not a number {}".format(number))
        return

#bot.run("MTI5NTA0MjY1NTIwMTM5ODc4NA.Gs4neo.cD2rStjf3tVSnxkbWzNxdhW7jStzC6eHyy57cI")