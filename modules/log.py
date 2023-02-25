from multiprocessing.connection import Client
import discord
from discord.ext import commands

import datetime
import sys
import os
from os import mkdir, path

msg_file='./log/msg.log'

class log(commands.Cog):
    def __init__(self,client):
        self.client=client
    
    