import discord
import asyncio

class BumBot(discord.Client):
    async def on_ready(self):
        print(f"BumBot is ready to perform as {self.user} (ID: {self.user.id})")

    async def on_message(self, message):
        if message.author == self.author:
            return
        
        if message.content.startswith("!bum"):
            await message.channel.send("Who's the bum? You got 10 seconds to respond (be careful on what you respond)")

            def check(m):
                return  m.author == message.author
            
            try:
                response = await self.wait_for('message', check=check, timeout=10.0)
            except asyncio.TimeoutError:
                await message.channel.send("{} must really be a bum if it took you more than 10 seconds to make a choice".format(message.author.name))
                return
            
            if str(response).upper() == "YANN":
                await message.channel.send("The Boy isn't a bum, he is your savior!")
                await message.channel.send("ShhhBot has the permissions to ban users, so be careful of not spamming this command ;)")
            else:
                await message.channel.send(f"{str(response).upper()} IS A BUM! :thumbsdown")

    async def on_message_delete(self, message):
        msg = f"{message.author} has deleted the following message: {message.content}"
        await message.channel.send("You thought you could just delete a message and it would go unnoticed? :joy_cat: :thumbsdown:")
        await message.channel.send(msg)