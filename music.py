import discord
from discord.ext import commands

import datetime
import youtube_dl
import ffmpeg

class music(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f'<@{ctx.author.id}>plz join a voice channel.')
        voiceChannel=ctx.author.voice.channel
        if ctx.voice_client is None:
            await voiceChannel.connect()
        else:
            await ctx.voice_client.move_to(voiceChannel)
    
    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()
    
    @commands.command()
    async def play(self,ctx,msg):
        #ctx.voice_client.stop()
        FFMPEG_OPTIONS={'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format' : 'bestaudio'}
        vc=ctx.voice_client
        print(msg)
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info=ydl.extract_info(msg, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
    
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await self.send('pause')
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send('resume')
    
    @commands.command()
    async def stop(self,ctx):
        await ctx.voice_client.stop()
        await ctx.send('stop')

def setup(client):
    client.add_cog(music(client))