import os
import asyncio
import sys

import nest_asyncio
import discord
from discord.ext import commands


from utils.EnvironmentLoader import load_env

env = load_env()
TOKEN = env["DISCORD_TOKEN"]

intents = discord.Intents.all()


bot = commands.Bot(command_prefix="!", intents=intents)


async def main():
    await bot.load_extension("cogs.MainCog")
    bot.run(TOKEN)


if __name__ == "__main__":
    try:
        nest_asyncio.apply()
        asyncio.run(main())
    except Exception as e:
        print(e)
