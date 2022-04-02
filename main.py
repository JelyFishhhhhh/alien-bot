import discord
from discord.ext import commands
import datetime
import sys
import os
from os import mkdir, path
import json
from json.decoder import JSONDecodeError

prefix='*'
client = commands.Bot(command_prefix=prefix,intents=discord.Intents.all())

import music,cmd
cogs=[music,cmd]

with open('bot.json', mode='r', encoding='utf8') as file:
    data=json.load(file)

for x in cogs:
    x.setup(client)

@client.event
async def on_ready():
    print(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S} >>> {client.user} is on the air.')

if __name__ == '__main__':
    client.run(data['TOKEN'])