import os
import sys
from dotenv import load_dotenv


def load_dev():
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    DISCORD_GENERAL_CHANNEL_ID = int(os.getenv("DISCORD_GENERAL_CHANNEL_ID"))
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    return {
        "DISCORD_TOKEN": DISCORD_TOKEN,
        "DISCORD_GENERAL_CHANNEL_ID": DISCORD_GENERAL_CHANNEL_ID,
        "OPENAI_KEY": OPENAI_KEY,
    }


def load_prod():
    DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
    DISCORD_GENERAL_CHANNEL_ID = int(os.environ["DISCORD_GENERAL_CHANNEL_ID"])
    OPENAI_KEY = os.environ["OPENAI_KEY"]
    return {
        "DISCORD_TOKEN": DISCORD_TOKEN,
        "DISCORD_GENERAL_CHANNEL_ID": DISCORD_GENERAL_CHANNEL_ID,
        "OPENAI_KEY": OPENAI_KEY,
    }


def load_env():
    try:
        if sys.argv[1] == "prod":
            print("Running in prod mode")
            return load_prod()
        else:
            print("Running in dev mode")
            return load_dev()
    except IndexError:
        print("Running in dev mode")
        return load_dev()
    except Exception as e:
        print(e)
        raise e
