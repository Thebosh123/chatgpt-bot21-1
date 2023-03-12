from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API ID", 19132497))
API_HASH = getenv("API_HASH", "55a02a263088db38e00db9287ce5d4e3")
BOT_TOKEN = getenv("BOT_TOKEN", "6019411469:AAFSN9ANdv9FBTz9lxYbEvevPleqiSu1LvA")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
