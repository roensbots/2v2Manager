# Versus by Roen Wainscoat

import globalvars

import discord
from discord.ext import commands
from discord.ext.commands import bot
import time

commands = commands.Bot(command_prefix="#", case_insensitive=True)
client = discord.Client()

print("reqhandler.py LOADED!")
 
@client.event
async def on_message(message):
    if message.content.upper().startswith('#VERSUS ACCEPT'):
        userID = message.content.id

