# 2v2Manager by Roen Wainscoat

import discord
from discord.ext import commands
from discord.ext.commands import bot
import time

client = discord.Client()
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.content.startswith('!ping'):
        userID = message.author.id
        await client.send_message(message.channel, '<@%s> pong' % (userID))


client.run("")