# Made by Phumrapee Soenvanichakul (jannnn1235)
# Github: https://github.com/Jannnn1235
import discord 
from discord.ext import commands
from datetime import datetime as date
import table

bot = commands.Bot(command_prefix='n.' )

@bot.event
async def on_ready():
    print('{0.user}'.format(bot), 'is ready2')
    print("==================")
    await bot.change_presence(activity=discord.Game(name="ตารางเรียน"))

@bot.event
async def on_message(message):
    await talk_bot(message) 

@bot.event
async def talk_bot(message):    
    day_today = str(date.today().strftime("%A"))
    time_start = date.today().strftime("%H:%M")  

    def findX():
        for i in range(11):
            if str(time_start) >= table.timestart['timestart'][i] and str(time_start) <= table.timestart['timestart'][i+1]:
                return i
            elif i == 10:
                return i

    if 'คาบ' in message.content:
        x = findX()
        if 'คาบนี้' in message.content:  
            if day_today in table.day and x < 10:
                await message.channel.send(f"{table.day[f'{day_today}'][x]} {table.timestart['timestart'][x]} - {table.timestart['timestart'][x+1]}")
            else:
                await message.channel.send("ไม่มีเรียนไอ้สัสเอ้ย อย่าติดตลก")

        if 'คาบต่อไป' in message.content or 'คาบหน้า' in message.content:
            if day_today in table.day and x < 9:
                await message.channel.send(table.day[f"{day_today}"][x+1])
            else:
                await message.channel.send("ไม่มีเรียนไอ้สัสเอ้ย อย่าติดตลก")
        
        if 'คาบเมื่อกี้' in message.content or 'คาบที่แล้ว' in message.content:  
            if day_today in table.day and x < 10:
                await message.channel.send(table.day[f"{day_today}"][x-1])
            else:
                await message.channel.send("ไม่มีเรียนไอ้สัสเอ้ย อย่าติดตลก")

    if 'ตารางเรียน' in message.content:   
        file = discord.File("image/ตารางเรียน.jpg")
        await message.channel.send(file = file)

    if message.content == 'n.help':
        embed=discord.Embed(title="ช่วยเหลือ" , color=blue)
        embed.add_field(name="คาบนี้", value="พิมพ์ในช่องแชท", inline=False)
        embed.add_field(name="คาบต่อไป", value="พิมพ์ในช่องแชท", inline=False)
        embed.add_field(name="ตารางเรียน", value="พิมพ์ในช่องแชท", inline=True)
        embed.set_thumbnail(url = bot.user.avatar_url)
        embed.set_footer(text=github)
        await message.channel.send(embed=embed)
        
bot.run("#HERE")
