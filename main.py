# discord specific imports
from discord import Intents, Client, Message, app_commands, channel, InteractionType, Interaction
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


# works but is limited - slowly building working stuff into this
@bot.hybrid_command(name="get_help", description="Request for help, adjudication, or clarification")
async def get_help(ctx: commands.Context, message: str):
    crew_channel = await bot.fetch_channel(1255558358790832299)
    at_user = ctx.author.mention
    crew = ctx.guild.get_role(1255558358790832294)  # replace with actual crew role ID in live server
    at_crew = crew.mention
    await ctx.reply(
                        f"Your response has been sent to the game team, {at_user}. "
                        f"The game team are checking and will get back to you soon. "
                        f"\nThe message you sent: \n> _{message}_"
                  )
    await crew_channel.send(
        f"{at_crew} you got a request from username '**{ctx.author.name}**', "
        f"server nickname at time of sending '**{ctx.author.nick}**'. "
        f"\nMessage sent from: {ctx.channel.jump_url}"
        f"\nMessage sent: \n> _{message}_"
    )

    # await message.channel.send("Please go to <#channelID>")
    # await channel.send(f"current channel is: {message.crew_channel}, message is \n{message}")
    # message_channel = ctx.channel


# @bot.hybrid_command(name="attention2", description="electric boogaloo")
# # @app_commands.describe(
# #     choices="hello, tell me what you want",
# # )
# async def attention2(
#         ctx: commands.Context,
#         # choices: app_commands.Choice[str]
# ):
#     # Update specific channel ID when you know the real server ID channel
#     crew_channel = await bot.fetch_channel(1255558358790832299)
#     user_input = await bot.wait_for("message")
#     await ctx.reply(f"Your current channel is {ctx.channel}. The game team are checking and will get back to you soon")
#     msg = await ctx.channel.fetch_message()
#     await crew_channel.send(f"zeroth test: message sent was \n'{user_input}'")
#     await crew_channel.send(f"first test: message sent was \n'{user_input.content}'")
#     await crew_channel.send(f"second test: message sent was \n'{msg}'")
#     # await crew_channel.send(f"you got a message from {ctx.channel}! The message is \n{ctx.send(msg.embeds[0].description)}")
#
#     # await message.channel.send("Please go to <#channelID>")
#     # await channel.send(f"current channel is: {message.crew_channel}, message is \n{message}")
#     # message_channel = ctx.channel
#
#
# # the command i'm doing my messy testing on. Message crashes. ctx.author.nick returns None,
# # Message.author.nick returns exception
# # message.author.nick returns None as well iirc but might return exception - no time to rerun at this second
# @bot.hybrid_command(name="attention3", description="i'm outta control")
# async def attention3(ctx: commands.Context, message: Message):
#     crew_channel = await bot.fetch_channel(1255558358790832299)
#     # msg = Message.content
#     at_user = ctx.author.mention
#     user_channel = ctx.channel
#     # testing = await ctx.fetch_message(message.id)
#     # testing = Message.author.nick
#     # testing = ctx.author.nick
#     testing = await ctx.fetch_message(bot.user.id)
#     guild = await bot.fetch_guild(1255558358790832291)  # need to replace with new guild_id of live server
#     # nickname = await guild.fetch_member(message.author.id)
#     # msg_link = Message.channel.mention
#     await ctx.reply(
#         f"current channel is {user_channel}, user{at_user} with messageid {'message.id'} {testing}. The game team are checking and will get back to you soon")
#     # msg = await ctx.channel.fetch_message()
#     await crew_channel.send(
#         f"you got a message from {user_channel}! The message is from {'wherever'}, message: \n{'msg'}")


# main function
def main() -> None:
    bot.run(token=TOKEN)


# main
if __name__ == "__main__":
    main()
