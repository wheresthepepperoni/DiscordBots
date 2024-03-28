# SpoonBot.py

import os
import discord
import random
import logging
from discord import Intents
from discord.ext import commands 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('SPOON_DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="", intents=intents)


handler = logging.FileHandler(filename=r"C:\Users\Administrator\Documents\GitHub\DiscordBots\Discord\Prod\Logs\SpoonBotLog.txt", encoding='utf-8', mode='w')

@client.event
async def on_ready():
    print(
    f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    spoon = 'spoon'

    fork = ['ratio + not a spoon + kys',
            'spoon > fork',
            'fuck forks; all my homies HATE forks',
            'the next word out of your mouth better be spoon. Fuck you']

    knife = ['knives are ok. At least they\'re not forks',
             'whatever',
             'the next word out of your mouth better be spoon']

    broken = 'i broke'

    if 'spoon' in message.content.lower():
        randy = random.randint(1,2)
        if randy == 1:
            response = spoon
            await message.channel.send(response, file=discord.File(r"C:\users\administrator\documents\GitHub\DiscordBots\Discord\Prod\spoon.png"))
        elif randy == 2:
            await message.add_reaction('\U0001f944')
        else:
            response = broken
            await message.channel.send(response)
            
    if 'fork' in message.content.lower():
        randy = random.randint(1,2)
        if randy == 1:
            response = fork
            await message.channel.send(response, file=discord.File(r"C:\users\administrator\documents\GitHub\DiscordBots\Discord\Prod\fork.png"))
        elif randy == 2:
            response = random.choice(fork)
            await message.channel.send(response)
        else:
            response = broken
            await message.channel.send(response)

    if 'knife' in message.content.lower():
        response = random.choice(knife)
        await message.channel.send(response)

    if 'knives' in message.content.lower():
        response = random.choice(knife)
        await message.channel.send(response)

client.run(TOKEN, log_handler=handler)
