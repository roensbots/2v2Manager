# 2v2Manager by Roen Wainscoat

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
    if message.content.upper().startswith('#2V2 REQUEST'):
        userName = message.author
        args = message.content.split(' ', 1)
        print(args)
        #requested = args[1]

        embed = discord.Embed(title="New 2v2 Request", description="", color=0x42f459)
        embed.add_field(name=userName, value="has requested a 2v2 battle.", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('#2V2 HELP'):
        embed = discord.Embed(title="2v2Manager Command Guide", description="", color=0x42f459)
        embed.add_field(name="Bot-specific Prefix", value="#2v2", inline=False)
        embed.add_field(name="Help", value="$ help", inline=False)
        embed.add_field(name="Request Partner", value="$ request [discord name]", inline=False)
        embed.add_field(name="Cancel Request", value="$ cancel", inline=False)
        await client.send_message(message.channel, embed=embed)

client.run("")