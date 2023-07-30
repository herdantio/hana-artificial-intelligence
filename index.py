import os
import discord

from MyClient import MyClient

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = MyClient(intents=intents)

# python try catch
try:
    client.run(TOKEN)
except Exception as e:
    print(e)
