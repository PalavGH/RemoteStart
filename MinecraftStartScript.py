import os
import subprocess

import discord
import youtube_dl
from youtube_api import YouTubeDataAPI

intents = discord.Intents().all()
activity = discord.Activity(name='Children', type=discord.ActivityType.watching)
bot = discord.Client(intents=intents, activity=activity)
yt = YouTubeDataAPI("AIzaSyCk0ndEUOUYPB1gxdcsNTOVmSKzdzo0gCU")
link = "https://www.youtube.com/watch?v="
os.chdir('C:/Songs')
searchSong = ""


@bot.event
async def on_ready():
    print("The final bot has started.")


@bot.event
async def on_message(message):
    if message.content == "!start":
        subprocess.call([r'PATH TO THE BATCH FILE THAT STARTS YOUR SERVER.'])


@bot.event
async def on_message(message):
    if message.content == "?pp":
        await message.channel.send("PP Test")


@bot.event
async def on_member_update(before, after):
    if before.status != after.status and (str(after.status) == "idle" or str(after.status) == "offline") and str(
            before.status) != "offline":
        if after.voice is not None:
            embed = discord.Embed(title=f"KICKED FOR BEING " + str(after.status))
            embed.add_field(name='MR VC FARMER', value=before.mention)
            embed.add_field(name='LES GOOOO', value="https://www.youtube.com/watch?v=w1PRiHEHJd8")
            channel = bot.get_channel(788477061962268693)
            await channel.send(embed=embed)
            await after.edit(voice_channel=None)


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None and str(member.status) == "offline":
        embed = discord.Embed(title=f"KICKED FOR BEING " + str(member.status))
        embed.add_field(name='MR VC FARMER', value=member.mention)
        embed.add_field(name='LES GOOOO', value="https://www.youtube.com/watch?v=w1PRiHEHJd8")
        channel = bot.get_channel(788477061962268693)
        await channel.send(embed=embed)
        await member.edit(voice_channel=None)


bot.run("NTYwOTc3NDI3MDY1NjAyMDQ4.XJ1g8Q.hbG-G7sAl9m3CWonHwezDyVolTk")
