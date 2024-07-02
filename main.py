# discord specific imports
from discord import Intents, Client, Message, app_commands, channel
from discord.ext import commands, tasks
from discord.ext.commands import Context

# general imports
from dotenv import load_dotenv
import os

from typing import Final

# Load token from .env file
load_dotenv()
TOKEN: Final[str] = os.getenv("TOKEN")
print(TOKEN)

# Initialise discord bot settings
intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


# confirmation that bot is online + sync commands when bot is run
@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    channel_test = bot.get_channel(1255558358790832299)
    # await channel_test.send("this is my exciting test")
    await bot.tree.sync()


# # replace this with the actual crew channel id when relevant
# crew_channel = bot.get_channel(1255558358790832299)


# @bot.hybrid_command(name="hello", description="Say hello to the bot")
# async def hello(ctx: commands.Context):
#     await ctx.reply(f"Hey!")


@bot.hybrid_command(name="attention", description="Alert game team you need help or adjudication")
async def attention(ctx: commands.Context):
    crew_channel = await bot.fetch_channel(1255558358790832299)
    msg = Message.content
    await ctx.reply(f"Your current channel is {ctx.channel}. The game team are checking and will get back to you soon")
    # msg = await ctx.channel.fetch_message()
    await crew_channel.send(f"you got a message from {ctx.channel}! The message is \n{msg}")

    # await message.channel.send("Please go to <#channelID>")
    # await channel.send(f"current chasnnel is: {message.crew_channel}, message is \n{message}")
    # message_channel = ctx.channel


@bot.hybrid_command(name="attention2", description="electric boogaloo")
async def attention2(ctx: commands.Context):
    crew_channel = await bot.fetch_channel(1255558358790832299)
    user_input = await bot.wait_for("message")
    await ctx.reply(f"Your current channel is {ctx.channel}. The game team are checking and will get back to you soon")
    msg = await ctx.channel.fetch_message()
    await crew_channel.send(f"zeroth test: message sent was \n'{user_input}'")
    await crew_channel.send(f"first test: message sent was \n'{user_input.content}'")
    await crew_channel.send(f"second test: message sent was \n'{msg}'")
    # await crew_channel.send(f"you got a message from {ctx.channel}! The message is \n{ctx.send(msg.embeds[0].description)}")

    # await message.channel.send("Please go to <#channelID>")
    # await channel.send(f"current channel is: {message.crew_channel}, message is \n{message}")
    # message_channel = ctx.channel

# main function
def main() -> None:
    bot.run(token=TOKEN)


# main
if __name__ == "__main__":
    main()
