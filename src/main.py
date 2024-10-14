import discord
from discord.ext import commands
from weather import get_weather
from latex import render_latex_to_image
import random as r
from datetime import datetime
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents) 

@bot.event
async def on_ready():
    return (f"Logged in as {bot.user}")

@bot.command()
async def help_me(ctx):
    response = "ShhhBot has different commands \n !bum : to find who's the bum \n !weather location : to give the weather of a location \n !latex message :  to compile a message into LaTex (might not work well, still in developpement) \n !random number : lets the bot choose a random number from range(0,number) (Developping this command to create a small guessing game) \n !Shhh : the bot will send a famous picture"
    await ctx.send(response)

@bot.command()
@commands.has_permissions(ban_members= True)
async def bum(ctx, message: str, second: int):


    #So the bot doesn't respond to himself
    if ctx.author.id == bot.user.id:
        return

    await ctx.send("Who's the bum (enter Yann, Samy or Felix)? You got 10 seconds to respond (be careful on what you respond)")
    def check(m):
        members = ['Yann', 'Samy', 'Felix']
        return  m.author == ctx.author and m.content in members
    
    try:
        response = bot.wait_for('message', check=check,timeout=10.0)
    except asyncio.TimeoutError :
        return await ctx.send("{} must really be a bum if it took you more than 10 seconds to make a choice".format(ctx.author.name))
    if str(response).upper() == "YANN":
        await ctx.send("The Boy isn't a bum, he is your savior!")
        await ctx.send("ShhhBot has the permissions to ban users, so be careful of not spamming this command ;)")
        return
    await ctx.send("{} IS A BUM!!".format(str(response).upper()))
    return



@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!\n Today we are the {datetime.now()}!")

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
async def latex(ctx, *, latex_code):
    try:
        image = render_latex_to_image(latex_code)

        file = discord.File(image, filename="latex.png")
        await ctx.send(file)
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
    with open("IMG_6700.JPG", 'rb') as f:
        image = discord.File(f)
        await ctx.send(image)
        return

def main():
    #No need to run the code, this is not the right token
    
    #bot.run("MTI5NTA0MjY1NTIwMTM5ODc4NA.GaTwS_.3-zdDKhkgBoJ6rI-do87vbtS0jzMUqbZQ8")
    return

if __name__ == "__main__":
    main()