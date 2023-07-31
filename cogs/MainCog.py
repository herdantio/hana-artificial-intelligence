# import discord
from discord.ext import commands
import os

from utils.EnvironmentLoader import load_env

env = load_env()

DISCORD_GENERAL_CHANNEL_ID = env["DISCORD_GENERAL_CHANNEL_ID"]


class MainCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.get_channel(DISCORD_GENERAL_CHANNEL_ID).send(
            f"{self.bot.user} has connected to Discord!"
        )

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        await message.channel.send(
            f"Message received from {message.author.name} with content: {message.content}"
        )


async def setup(bot):
    await bot.add_cog(MainCog(bot))
