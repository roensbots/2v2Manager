# Versus by Roen Wainscoat

import discord
from discord.ext import commands
from discord.ext.commands import bot
import time

commands = commands.Bot(command_prefix="#", case_insensitive=True)
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.content.upper().startswith('#VERSUS REQUEST'):
        userName = message.author
        args = message.content.split(' ', 1)
        print(args)
        #requested = args[1]

        embed = discord.Embed(title="New 2v2 Request", description="", color=0x42f459)
        embed.add_field(name=userName, value="has requested a 2v2 battle.", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('#VERSUS HELP'):
        embed = discord.Embed(title="VersusManager Command Guide", description="", color=0x659df7)
        embed.add_field(name="Bot-specific Prefix", value="#versus", inline=False)
        embed.add_field(name="Help", value="$ help", inline=False)
        embed.add_field(name="Request Partner", value="$ request [discord name]", inline=False)
        embed.add_field(name="Cancel Request", value="$ cancel", inline=False)
        await client.send_message(message.channel, embed=embed)

client.run("")