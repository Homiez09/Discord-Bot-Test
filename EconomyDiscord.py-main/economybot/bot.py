import os
import discord
from discord.ext import commands
import config

intents = discord.Intents().all()
PREFIX = config.PREFIX["command"]
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f"{PREFIX}coin เพื่อเริ่ม"))

@commands.has_role(config.ROLE["command"])
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@commands.has_role(config.ROLE["command"])
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config.APIBOT["TOKEN"])