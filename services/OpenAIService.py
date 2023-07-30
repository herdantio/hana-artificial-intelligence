# import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
# GUILD = os.getenv("DISCORD_GUILD")


class OpenAIService(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} has connected to Discord!")

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message)
        if message.author == self.user:
            return

        await message.channel.send(
            f"Message received from {message.author.name} with content: {message.content}"
        )


async def setup(bot):
    await bot.add_cog(OpenAIService(bot))
