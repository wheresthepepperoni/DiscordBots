# MorbBot.py

import os
import discord
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MORB_DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())



@client.event
async def on_ready():
    print(
    f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    morb = ['It\'s Morbin\' time',
'Just admiring my Morb',
'#MORBIUSSWEEP']

    morbImage = 'image'

    if 'morb' in message.content.lower() or 'morbius' in message.content.lower():
        response = random.choice(morb)
        await message.channel.send(response)

client.run(TOKEN)
