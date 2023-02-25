from turtle import title
import discord
from discord.ext import commands
from discord.ext import tasks

import datetime
import youtube_dl
import ffmpeg
import asyncio

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

class music(commands.Cog):
    def __init__(self, client):
        self.client=client
        self.musicQueue=[]

    async def checkQue(self,ctx):
        if len(self.musicQueue) > 0:
            server = ctx.message.guild
            voice_channel = server.voice_client
            while voice_channel.is_playing():
                a=self.musicQueue[0]
            await self.playSong(ctx)
            while voice_channel.is_playing():
                a=self.musicQueue[0]
            print('end')
            self.musicQueue.pop()
        else:
            await ctx.send('No song in queue.')
    
    async def playSong(self,ctx):
        voice_channel = ctx.voice_client
        self.joinChannel
        with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
            info=ydl.extract_info(self.musicQueue[0], download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **ffmpeg_options)
            voice_channel.play(source)

    async def joinChannel(self,ctx):
        if not ctx.author.voice:
            await ctx.send(f'<@{ctx.author.id}>plz join a voice channel.')
        voiceChannel=ctx.author.voice.channel
        await voiceChannel.connect()

    @commands.command()
    async def join(self,ctx):
        await self.joinChannel(ctx)
    
    @commands.command()
    async def leave(self,ctx):
        ctx.voice_client.disconnect()
    
    @commands.command()
    async def play(self,ctx, *,msg):
        self.musicQueue.append(msg)
        await self.checkQue(ctx)
        
    @commands.command()
    async def pause(self,ctx):
        ctx.voice_client.pause()
        await self.send('pause')
    
    @commands.command()
    async def resume(self,ctx):
        ctx.voice_client.resume()
        await ctx.send('resume')
    
    @commands.command()
    async def stop(self,ctx):
        ctx.voice_client.stop()
        await ctx.send('stop')

def setup(client):
    client.add_cog(music(client))