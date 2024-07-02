# discord specific imports
from discord import Intents, Client, Message, app_commands
from discord.ext import commands, tasks
from discord.ext.commands import Context

# general imports
from dotenv import load_dotenv
import os

from typing import Final

# Load token from .env file
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
print(TOKEN)

# Initialise discord bot settings
intents: Intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


# main function
def main() -> None:
    bot.run(token=TOKEN)


# main
if __name__ == "__main__":
    main()
