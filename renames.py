import discord
from discord.ext import commands
import random_roles


TOKEN = "NzA0NzQ4NTg2NjgzOTkwMjk2.Xq7CvQ.6JNSN1e6NC40hmEf55AO-p6FJhI"
bot = commands.Bot(command_prefix='!')
key = '_**.**_'

def check(key_drop):
    if key != key_drop:
        print('код не подошёл')
        return False
    else:
        print('код подошёл')
        return True

@bot.command(name='rename')
async def renames(self, key):
    if check(key):
        count = 1
        for member in bot.guilds[0].members:  # bot.guilds[1] - Mafia party сервер, пока не знаю как определить гильдию отправителя
            try:
                if member.__str__() not in ['Оутсайдер#6307', 'Helper#0261', 'seijuko#1575', 'kohiry#9498']:
                    await member.edit(nick=str(count)) # or do whatever you wish with the member detail
                    count += 1
            except discord.errors.Forbidden:
                print('Нет прав на переименование, скипаю')

    # await self.send('#')  # таким образом буду автоматически вызывать нужные мне команды


@bot.command(name='renameRev')
async def renamesRev(self, key):
    if check(key):
        for member in bot.guilds[0].members:  # bot.guilds[0] - Mafia party сервер, пока не знаю как определить гильдию отправителя
            try:
                await member.edit(nick=None) # or do whatever you wish with the member detail
            except discord.errors.Forbidden:
                print('Нет прав на переименование, скипаю')


bot.run(TOKEN)
