import discord
import os
from dotenv import load_dotenv

load_dotenv()
GUILD = os.getenv("DISCORD_GUILD")


class MyClient(discord.Client):
    async def on_ready(self):
        for guild in self.guilds:
            if guild.name == GUILD:
                break

        print(
            f"{self.user} is connected to the following guild:\n"
            f"{guild.name}(id: {guild.id})"
        )

        members = "\n - ".join([member.name for member in guild.members])
        print(f"Guild Members:\n - {members}")
        print(f"\n There are {len(guild.members)} members in this guild")

    # async def on_message(self, message):
    #     print(f'Message from {message.author}: {message.content}')
