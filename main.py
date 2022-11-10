import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the youtube bot")


#!hello -- You can name any file this name


@client.event
async def on_member_join(member):
    channel = client.get_channel('')
    await channel.send("Hello")
    #await member.send("Test")


client.run(os.environ['token'])

#keep_alive()
#client.run(os.environ['token'])
