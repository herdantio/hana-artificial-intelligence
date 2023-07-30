import os
import asyncio
import nest_asyncio
import discord
from discord.ext import commands


from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()


bot = commands.Bot(command_prefix="", intents=intents)


async def main():
    await bot.load_extension("services.OpenAIService")
    bot.run(TOKEN)


if __name__ == "__main__":
    try:
        nest_asyncio.apply()
        asyncio.run(main())
    except Exception as e:
        print(e)
