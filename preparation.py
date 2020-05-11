import discord
import pprint
from discord.ext import commands
import requests


TOKEN = "NzA5MzUxMzI0NzEzNDg0MzE4.XrkpIg.g8IGzFFRUeS_F1rdfX0LEUD6O-s"
bot = commands.Bot(command_prefix='!')
key = '_**.**_'


def check(key_drop):
    if key != key_drop:
        print('код не подошёл')
        return False
    else:
        print('код подошёл')
        return True


@bot.command(name='rules')
async def rules(self, key):
    if check(key):
        text = ''
        with open('rules/rules_step.txt') as f:
            text = ' '.join(f.readlines())
        await self.send(text)
        await self.send('_ _')
        text = ''
        with open('rules/rules_card.txt') as f:
            text = ' '.join(f.readlines())
        await self.send(text)


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
