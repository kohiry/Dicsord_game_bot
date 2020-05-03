import discord
import requests
import pprint
from discord.ext import commands
import random
import random_roles


TOKEN = "TOKEN"
bot = commands.Bot(command_prefix='!')


@bot.command(name='help_u')
async def help(self):
    await self.send('Я есть творение Koh(a). Буду помогать вам.')


@bot.command(name='rules')
async def rules(self):
    text = ''
    with open('rules.txt') as f:
        text = ' '.join(f.readlines())
    await self.send(text)


@bot.command(name='rename')
async def renames(self):
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
