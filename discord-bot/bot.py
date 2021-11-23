import os

import aiohttp
import discord
from dotenv import load_dotenv

from logger import get_logger

load_dotenv()
client = discord.Client()
rasa_url = "http://localhost:5005/webhooks/rest/webhook"
logger = get_logger("discord_bot")


@client.event
async def on_ready():
    logger.info('Discord bot started as {0.user}'.format(client))


@client.event
async def on_message(message):
    logger.debug(message.author.name + ": " + message.content)
    if message.author == client.user:
        return
    content = {
        "sender": message.author.name,
        "message": message.content
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(rasa_url, json=content) as resp:
                rasa_reply = await resp.json()
                rasa_reply = rasa_reply[0]['text']
                await message.channel.send(rasa_reply)
    except Exception as e:
        await message.channel.send("සමාවෙන්න, RASA සර්වර් එකේ ගැටලුවක් 🙁")
        logger.warning(str(e))


client.run(os.environ['DISCORD_TOKEN'])
