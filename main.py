import discord
from discord.ext import commands
import datetime
import sys
import os
from os import mkdir, path
import json
from json.decoder import JSONDecodeError

prefix='*'

client = discord.Client()

def mode(msg,info):
    msg=msg.lower()
    if msg=='ping':
        print(f'{info.author} is asking the bot\'s ping')
        return str(round(client.latency*1000))+' (ms)'
    
    elif msg=='restart':
        os.system('main.py')

    elif msg=='stop':
        sys.exit()

    else:
        return 'err0r'

with open('bot.json', mode='r', encoding='utf8') as file:
    data=json.load(file)

@client.event
async def on_ready():
    print(f'{client.user} is on the air.')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    try:
        print((message.content[0]==prefix)*'command')
    except IndexError:
        print(f'its a picture :|')
        return
    
    if message.content[0]==prefix:
        await message.channel.send(f'{mode(message.content[1:],message)}')
    elif (message.content.lower()) in ('hello', 'hi','嗨','哈囉','你好','泥好','嗨你好'):
        print(f'say hello to {message.author}')
        await message.channel.send(f'Hello <@{message.author.id}>')

if __name__ == '__main__':
    client.run(str(data['TOKEN']))