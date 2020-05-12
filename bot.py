import discord
from discord.ext import commands
import random_roles
import asyncio
import random


TOKEN = "NzA5MzUxMzI0NzEzNDg0MzE4.Xrl9yQ.8KVfIAQCcEQSu8Q5vPTWG0LBb04"
bot = commands.Bot(command_prefix='!')
key = '_**.**_'
count_work = 0
count_work_2 = 0
count_work_3 = 0
people_talk = []

def check(key_drop):
    if key != key_drop:
        print('код не подошёл')
        return False
    else:
        print('код подошёл')
        return True


@bot.command(name='renameReverse')
async def renamesRev(self):
    '''Удаляет все никнейми участников сервера'''
    for member in self.guild.members:  # bot.guilds[0] - Mafia party сервер, пока не знаю как определить гильдию отправителя
        try:
            await member.edit(nick=None) # or do whatever you wish with the member detail
        except discord.errors.Forbidden:
            print('Нет прав на переименование, скипаю')


@bot.command(name='create-channel')  # !create-channel _**.**_
async def created_channel(self, key):
    '''Создаёт новые каналы, специально для игры в "Мафию"'''
    if check(key):
        global count_work, count_work_2
        count_work += 1  # следим за количевством включений команды
        count_work_2 = 0
        if count_work < 2 and 'Мафия' not in [i.name for i in self.guild.channels]:
            await self.send('Эта шняга сработает если сущевстует голосовой канал названный "Основной"')
            for i in self.guild.channels:
                if type(i) == discord.channel.VoiceChannel:
                    await i.clone(name='Основной-голосовой')
                    for j in range(1, 9):
                        await i.clone(name='Мирный-житель-' + str(j))
                    for j in range(1, 3):
                        await i.clone(name='Дополнительная-роль-' + str(j))
                    for j in ['Доктор', 'Мафия', 'Дон-Мафии', 'Комиссар']:
                        await i.clone(name=str(j))
                    await self.send('Создал необходимое количевство каналов для игры 16 человек max.')
                    break
        else:
            await self.send('Глупый, ты уже запускал его и каналы созданы.')


@bot.command(name='delete-channel')  # !create-channel _**.**_
async def delete_channel(self, key):
    '''удаляет все созданные каналы кроме "Основной"'''
    if check(key):
        global count_work, count_work_2
        count_work_2 += 1  # следим за количевством включений команды
        count_work = 0
        if count_work_2 < 2 and 'Мафия' in [i.name for i in self.guild.channels]:
            await self.send('Сейчас удалим все голосовые каналы кроме "Основной"')
            for i in self.guild.channels:
                if i.name != "Основной" and type(i) == discord.channel.VoiceChannel:
                    await i.delete()
        else:
            await self.send('Глупый, ты уже запускал его и каналы удалены.')


@bot.command(name='rules', decription='Правила игра в Мафию')
async def rules(self, key):
    '''Правила игра в Мафию'''
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
    global count_work_3
    if message.content.startswith('-debug'):
        await message.channel.send('d')
    content = message.content.lower()
    answer = ''
    if message.author == bot.user:
        return
    # Посхалки
    if '#' in content:
        await message.channel.send("Сработала скрытая команда")
    if ('норм' in content or 'отлично' in content or 'хорошо' in content) and message.author.__str__() in people_talk:
        answer += random.choice(['Ок.', 'нормалёк', 'неплохо'])
    if 'привет' in content or 'здарова' in content or 'дратути' in content or 'дарова' in content or 'здравствуй' in content:
        if message.author.__str__() not in people_talk:
            answer += random.choice(['Приветики!', 'Здравствуй)', 'Ага.']) + ' Как твои дела?'
            print(answer)
            people_talk.append(message.author.__str__())
        else:
            answer += random.choice(['Мальчик, у тебя проблемы с памятью? **Мы здоровались.**', 'Где-то я тебя **уже слышал** -. -', '**Повторяешься.**'])
    dog = ['соба', 'щено', 'пёс', 'пес']
    for i in dog:
        if i in message.content.lower():
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            if response:
                json_response = response.json()
                await message.channel.send(f"{json_response['message']}")
            break
    if answer != '':
        await message.channel.send(answer)
    await bot.process_commands(message)



@bot.command(name='move')
async def move(self):
    '''Включить файл bot_game_action, для использования'''
    pass


@bot.command(name='moveReverse')
async def moveReverse(self):
    '''Включить файл bot_game_action, для использования'''
    pass


@bot.command(name='rename')
async def renames(self):
    '''Включить файл bot_game_action, для использования'''
    pass


bot.run(TOKEN)
