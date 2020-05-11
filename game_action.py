import discord
from discord.ext import commands
import random_roles
import asyncio


TOKEN = "NzA5MzUxMzI0NzEzNDg0MzE4.XrkpIg.g8IGzFFRUeS_F1rdfX0LEUD6O-s"
bot = commands.Bot(command_prefix='!')
key = '_**.**_'

roles = random_roles.main(int(input()))

def check(key_drop):
    if key != key_drop:
        print('код не подошёл')
        return False
    else:
        print('код подошёл')
        return True

@bot.command(name='move')
async def move(self, key):
    if check(key):
        # образование списка с кналами войс чата
        list_roles = {}
        for i in self.guilds.channels:
            if type(i) == discord.channel.VoiceChannel:
                list_roles[i.name] = i
        # начало моего алгоритма для распределения ролей
        stop = False
        for i in self.guilds.members:  #игроки
            for j in roles.keys():  # названия ролей из random_roles
                if j in list_roles.keys() and i.nick in roles[j]:  #сравнение названия роли и ключа из list_roles и сравнение ника с списоком номеров ролей
                    print(type(i), list_roles[j])
                    await i.move_to(list_roles[j])

@bot.command(name='create-channel')  # !create-channel _**.**_
async def create_channel(self, key):
    print(self.guild)
    #if check(key):
        #await discord.VoiceChannel.clone('1', name='1')


@bot.command(name='moveReverse')
async def moveReverse(self):
    # образование списка с кналами войс чата
    stop = True
    for i in self.guilds.channels:
        if i.name == "Основной-голосовой":
            for member in bot.guilds[0].members:
                await member.move_to(i)
            break


@bot.command(name='rename')
async def renames(self):
    count = 1
    stop = True
    for i in self.guilds.channels:
        if i.name == "Основной-голосовой":
            for member in i.members:
                print(member)
                try:
                    if member.__str__() not in ['Оутсайдер#6307', 'Helper#0261', 'kohiry#9498']:
                        await member.edit(nick=str(count)) # or do whatever you wish with the member detail
                        count += 1
                except discord.errors.Forbidden:
                    print('Нет прав на переименование, скипаю')
                    continue
            break


@bot.command(name='renameReverse')
async def renamesRev(self):
    for member in self.guilds.members:  # bot.guilds[0] - Mafia party сервер, пока не знаю как определить гильдию отправителя
        try:
            await member.edit(nick=None) # or do whatever you wish with the member detail
        except discord.errors.Forbidden:
            print('Нет прав на переименование, скипаю')


bot.run(TOKEN)