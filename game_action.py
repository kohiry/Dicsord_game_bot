import discord
from discord.ext import commands
import random_roles
import asyncio
import inspect


TOKEN = "NzA5MzUxMzI0NzEzNDg0MzE4.Xrl9yQ.8KVfIAQCcEQSu8Q5vPTWG0LBb04"
bot = commands.Bot(command_prefix='!')
key = '_**.**_'
count_work = 0
count_work_2 = 0


roles = random_roles.main(int(input('Введи количевство игроков')))

print(inspect.getfullargspec(bot.command()))

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
        for i in self.guild.channels:
            if type(i) == discord.channel.VoiceChannel:
                list_roles[i.name] = i
        # начало моего алгоритма для распределения ролей
        stop = False
        for i in self.guild.members:  #игроки
            for j in roles.keys():  # названия ролей из random_roles
                if j in list_roles.keys() and i.nick in roles[j]:  #сравнение названия роли и ключа из list_roles и сравнение ника с списоком номеров ролей
                    print(type(i), list_roles[j])
                    await i.move_to(list_roles[j])


@bot.command(name='moveReverse')
async def moveReverse(self):
    # образование списка с кналами войс чата
    stop = True
    for i in self.guild.channels:
        if i.name == "Основной-голосовой":
            for member in bot.guilds[0].members:
                await member.move_to(i)
            break


@bot.command(name='rename')
async def renames(self):
    count = 1
    stop = True
    for i in self.guild.channels:
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
    for member in self.guild.members:  # bot.guilds[0] - Mafia party сервер, пока не знаю как определить гильдию отправителя
        try:
            await member.edit(nick=None) # or do whatever you wish with the member detail
        except discord.errors.Forbidden:
            print('Нет прав на переименование, скипаю')



@bot.command(name='create-channel')  # !create-channel _**.**_
async def created_channel(self, key):
    if check(key):
        global count_work, count_work_2
        count_work += 1  # следим за количевством включений команды
        count_work_2 = 0
        if count_work < 2 and 'Мафия' not in [i.name for i in self.guild.channels]:
            await self.send('Эта шняга сработает если сущевстует голосовой канал названный "Основной"')
            for i in self.guild.channels:
                if type(i) == discord.channel.VoiceChannel:
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
