import discord
import requests
import pprint
from discord.ext import commands


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


@bot.event
async def on_message(message):
    if message.content.startswith('-debug'):
        await message.channel.send('d')
    content = message.content.lower()
    # Посхалки
    if 'ты где' in content:
        await message.channel.send("Где-же андрюша-неровная спинуша?")
    if 'потерялась' in content:
        await message.channel.send("андрюша-неровная спинуша")
    if 'кто ты' in content:
        await message.channel.send('Я есть творение Koh(a). Буду помогать вам.')

    cat = ['кот', 'кошк']
    for i in cat:
        if i in message.content.lower():
            response = requests.get('https://api.thecatapi.com/v1/images/search')
            if response:
                json_response = response.json()
                await message.channel.send(f"{json_response[0]['url']}")
            break
    dog = ['соба', 'щено']
    for i in dog:
        if i in message.content.lower():
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            if response:
                json_response = response.json()
                await message.channel.send(f"{json_response['message']}")
            break

    await bot.process_commands(message)


bot.run(TOKEN)
