import discord
from discord.ext import commands
import random_roles
import asyncio


TOKEN = "NzA5MzUxMzI0NzEzNDg0MzE4.Xrl9yQ.8KVfIAQCcEQSu8Q5vPTWG0LBb04"
bot = commands.Bot(command_prefix='!')
count_work = 0
count_work_2 = 0


@bot.command(name='create-channel')  # !create-channel _**.**_
async def create_channel(self):
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
                break
    else:
        await self.send('Глупый, ты уже запускал его и каналы созданы.')


@bot.command(name='delete-channel')  # !create-channel _**.**_
async def delete_channel(self):
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


bot.run(TOKEN)
