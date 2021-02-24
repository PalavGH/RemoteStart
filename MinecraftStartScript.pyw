import discord
import subprocess

bot = discord.Client()

# Does not print to Discord channel, only the terminal. Since this is a pyw file, however, it will not be shown on your screen.
@bot.event
async def on_ready():
    print("Bot started.")

# The command can be changed to anything you want. Recognize's messages from all channels the bot has access to. 
@bot.event
async def on_message(message):
    if message.content == "!start":
        subprocess.call([r'PATH TO THE BATCH FILE THAT STARTS YOUR SERVER.'])

bot.run("INSERT DISCORD API KEY HERE. KEEP THE QUOTES.")