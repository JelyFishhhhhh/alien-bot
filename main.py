from email import message
import discord
from discord.ext import commands
import datetime
import sys
from os.path import isdir
from os import mkdir, path
import json

prefix='*'
client = commands.Bot(command_prefix=prefix,intents=discord.Intents.all())

from modules import cmd, log, music
cogs=[music,cmd,log]

with open('bot.json', mode='r', encoding='utf8') as file:
    data=json.load(file)

for x in cogs:
    x.setup(client)

@client.event
async def on_ready():
    print(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S} >>> {client.user} is on the air.')
    #channel = client.get_channel(int(data['statusChannel']))
    #await channel.send(f'<@{client.user.id}> is on the air !')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not isdir("log"):
        mkdir("log")
    
    log()

if __name__ == '__main__':
    client.run(data['TOKEN'])