# Versus by Roen Wainscoat

import discord
from discord.ext import commands
from discord.ext.commands import bot
import time

commands = commands.Bot(command_prefix="#", case_insensitive=True)
client = discord.Client()

requestOriginID = "undefined"
reqOpen = 0

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

def addRequest():
    print("Adding a request...")
    global reqOpen
    reqOpen += 1
    print("Done.")

def remRequest():
    print("Removing one filled request...")
    global reqOpen
    reqOpen -= 1
    print("Done.")

@client.event
async def on_message(message):
    if message.content.upper().startswith('#VERSUS HELP'):
        embed = discord.Embed(title="VersusManager Command Guide", description="", color=0x659df7)
        embed.add_field(name="Bot-specific Prefix", value="#versus", inline=False)
        embed.add_field(name="Help", value="$ help", inline=False)
        embed.add_field(name="Request Partner", value="$ request [discord name]", inline=False)
        embed.add_field(name="Cancel Request", value="$ cancel", inline=False)
        await client.send_message(message.channel, embed=embed)
        userName = message.author
    sendRequest = "true"
    if message.content.upper().startswith('#VERSUS REQUEST'):
        if message.content.upper().startswith('#VERSUS REQUEST --OPEN'):
            requestOriginID = message.author.id
            embed = discord.Embed(title="New Open 2v2 Request", description="Type $ accept --open to accept!", color=0x42f459)
            await client.send_message(message.channel, embed=embed)
            addRequest()
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
    if message.content.upper().startswith('#VERSUS ACCEPT'):
        userID = message.author.id
        userName = message.author
        if 8 > 0:
            if requestOriginID != userID:
                embed = discord.Embed(title="Request Accepted!", description="", color=0x659df7)
                embed.add_field(name=userName, value="has accepted the request.", inline=False)
                await client.send_message(message.channel, embed=embed)
            else:
                embed = discord.Embed(title="Error!", description="", color=0xf44253)
                embed.add_field(name="You cannot accept your own request.", value="$ cancel --open to cancel.", inline=False)
                await client.send_message(message.channel, embed=embed)
        else:
                embed = discord.Embed(title="Error!", description="", color=0x659df7)
                embed.add_field(name="Sorry, but there are no open requests now.", value="Please type $ request to open a request.", inline=False)
                await client.send_message(message.channel, embed=embed)

client.run("")