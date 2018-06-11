# Versus by Roen Wainscoat

import globalvars

import discord
from discord.ext import commands
from discord.ext.commands import bot
import time

commands = commands.Bot(command_prefix="#", case_insensitive=True)
client = discord.Client()

print("reqcreator.py LOADED!")
 
@client.event
async def on_message(message):
    userName = message.author
    sendRequest = "true"
    if message.content.upper().startswith('#VERSUS REQUEST'):
        if message.content.upper().startswith('#VERSUS REQUEST --OPEN'):
            senderID = message.author.id
            embed = discord.Embed(title="New Open 2v2 Request", description="Type $ accept --open to accept!", color=0x42f459)
            await client.send_message(message.channel, embed=embed)
        else:
            args = message.content.split(' ')
            print(args)

            try:
                args[2]
            except IndexError:
                sendRequest = "false"

            if sendRequest == "true":
                embed = discord.Embed(title="New 2v2 Request", description="", color=0x42f459)
                embed.add_field(name=userName, value="has requested a 2v2 battle.", inline=False)
                await client.send_message(message.channel, embed=embed)
            else:
                embed = discord.Embed(title="Error!", description="", color=0xf44253)
                embed.add_field(name="You did not provide a name to send the request to.", value="To send an open request, use $ request --open", inline=False)
                await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('#VERSUS HELP'):
        embed = discord.Embed(title="VersusManager Command Guide", description="", color=0x659df7)
        embed.add_field(name="Bot-specific Prefix", value="#versus", inline=False)
        embed.add_field(name="Help", value="$ help", inline=False)
        embed.add_field(name="Request Partner", value="$ request [discord name]", inline=False)
        embed.add_field(name="Cancel Request", value="$ cancel", inline=False)
        await client.send_message(message.channel, embed=embed)