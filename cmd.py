import discord
from discord.ext import commands

import datetime
import sys
import os
from os import mkdir, path

class cmd(commands.Cog):
    def __init__(self, client):
        self.client=client
    
    @commands.command()
    async def ping(self, ctx):
        print(f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S} >>> {ctx.author} is asking the bot\'s ping')
        await ctx.send(f'{str(round(self.client.latency*1000))} (ms)')

    @commands.command() 
    async def end(self,ctx):
        sys.exit()

def setup(client):
    client.add_cog(cmd(client))