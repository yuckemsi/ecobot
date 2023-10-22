import discord
from discord.ext import commands
import os
from settings import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"Вы зашли как: {bot.user}")
                   
@bot.command()
async def info(ctx):
    await ctx.send("Привет, я бот разработанный для просвещения в экологии, вот что я могу:\n !info - комманды, которые ест ьв боте.\n !types - виды сортируемого мусора\n !things - вещи, которые можно сделать из мусора\n !how - узнать, как можно начать сортировку в домашник условиях\n !dev - связь с разработчиком")

@bot.command()
async def types(ctx):
    with open('images/types.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send("Виды сортируемого мусора делятся на несколько, это:\n ✅ пластик\n✅ стекло\n ✅ металл\n ✅ батарейки\n ✅ органика\n ✅ бумага\n ")

    await ctx.send("Сортировка мусора предполагает прохождение следующих этапов:\n• Удаление камней, острых и значительных по объему предметов, способных повредить конвейер или иное оборудование.\n• Отделение крупного сора от более мелкого.\n• Отделение стекла, бумаги, пластика и т. д.\n• Сбор в отдельные тюки или контейнеры для отправки на переработку или утилизацию")

@bot.command()
async def things(ctx):
    with open('images/things.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send("↑ Из переработанного мусора можно сделать огромное множество вещей, они представленны на картинке выше ↑")

@bot.command()
async def how(ctx):
    with open('images/things.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

    await ctx.send("Начать сортировку дома можно со следующих пунктов:\n • Заведите экологичные привычки\n • Собирайте батарейки\n • Заведите место для сортировки\n • Уделите особое внимание пластику\n • Найдите пункт приема вторсырья")

    await ctx.send("✅ Все, вы готовы начать свою экологичную жизнь и сделать вклад в природу!")

bot.run(settings["TOKEN"])
