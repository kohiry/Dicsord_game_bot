import discord
from discord.ext import commands
import random_roles
import asyncio


TOKEN = "NzA5MzUxMzI0NzEzNDg0MzE4.XrkpIg.g8IGzFFRUeS_F1rdfX0LEUD6O-s"
bot = commands.Bot(command_prefix='!')


@bot.command(name='create-channel')  # !create-channel _**.**_
async def create_channel(self):
    print(self.guild)
    for i in self.guild.channels:
        print(i, type(i), type(discord.channel.VoiceChannel))
        if i.name == "Основной" and type(discord.VoiceChannel) == type(i):
            print('Нашёл еп')
    #if check(key):
        #await discord.VoiceChannel.clone('1', name='1')


bot.run(TOKEN)
