import os
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
    search_song = str(message.content)
    if search_song.startswith('<play'):
        search_song = search_song[6:]
        searches = yt.search(q=search_song, max_results=1)
        values_coll = searches[0].values()
        value_iter = iter(values_coll)
        song_id = next(value_iter)

        opts = [(link + song_id)]
        youtube_dl.main(opts)
        files = [x for x in os.listdir('C:\\Songs') if x.endswith(".mp4")]
        newest = max(files, key=os.path.getctime)
        # channel = message.channel
        voice_channel = message.author.voice.channel
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(newest))


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


bot.run("NTYwOTc3NDI3MDY1NjAyMDQ4.XJ1g8Q.ic-ZaMvprz1bVCgtc9mlidbcOgg")
