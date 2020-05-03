import discord
import requests
import pprint
from discord.ext import commands
import random
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

@bot.command(name='helpU')
async def help(self, key):
    if check(key):
        print(self.message)
        await self.send('Я есть творение Koh(a). Буду помогать вам.')


@bot.command(name='rules')
async def rules(self, key):
    if check(key):
        text = ''
        with open('rules.txt') as f:
            text = ' '.join(f.readlines())
        await self.send(text)


@bot.command(name='rename')
async def renames(self, key):
    if check(key):
        count = 1
        for member in bot.guilds[0].members:  # bot.guilds[1] - Mafia party сервер, пока не знаю как определить гильдию отправителя
            try:
                await member.edit(nick=str(count)) # or do whatever you wish with the member detail
                count += 1
            except discord.errors.Forbidden:
                print('Нет прав на переименование, скипаю')

    # await self.send('#')  # таким образом буду автоматически вызывать нужные мне команды

@bot.event
async def on_message(message):
    if message.content.startswith('-debug'):
        await message.channel.send('d')
    content = message.content.lower()
    # Посхалки
    if '#' in content:
        await message.channel.send("Сработала скртая команда")
    if 'ты где' in content or 'где ты' in content:
        await message.channel.send("Где-же андрюша-неровная спинуша?")
    if 'потерялась' in content:
        await message.channel.send("андрюша-неровная спинуша")
    if 'кто ты' in content or 'ты кто' in content:
        await message.channel.send('Я есть творение Koh(a). Буду помогать вам.')
    dog = ['соба', 'щено', 'пёс', 'пес']
    for i in dog:
        if i in message.content.lower():
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            if response:
                json_response = response.json()
                await message.channel.send(f"{json_response['message']}")
            break
    await bot.process_commands(message)


bot.run(TOKEN)
