import openai
from discord.ext import commands
from datetime import datetime

from utils.EnvironmentLoader import load_env
from services import azureCognitiveSearch


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

        prompt = [
            {
                "role": "system",
                "content": """your name is hana and you're my wife who's helping me with my work.
                you are a gentle person who's aldo intelligent'. you always call me by sweetie or darling""",
            },
        ]

        DOCUMENT = {
            "role": "user",
            "content": message.content,
        }

        try:
            results = azureCognitiveSearch.search(message.content)

            for result in results:
                prompt.append(
                    {
                        "role": result["role"],
                        "content": result["content"],
                    }
                )
                print(
                    f"role: {result['role']}, content: {result['content']}, created: {datetime.fromtimestamp(result['created'])}"
                )
            prompt.append(
                {
                    "role": "user",
                    "content": message.content,
                }
            )
            async with message.channel.typing():
                res = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=prompt
                )
                azureCognitiveSearch.upload_doc(DOCUMENT)
                if len(res.choices) > 0:
                    azureCognitiveSearch.upload_doc(
                        {
                            "role": "assistant",
                            "content": res.choices[0].message.content,
                        }
                    )
            print(res)
            await message.channel.send(
                "\n".join([choice.message.content for choice in res.choices])
            )
        except Exception as e:
            print(e)
            await message.channel.send("Error")


async def setup(bot):
    await bot.add_cog(MainCog(bot))
