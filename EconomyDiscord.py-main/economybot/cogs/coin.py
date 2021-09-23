import json
from discord.ext import commands
import discord

class coin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('coin is activate')

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('cogs/coin.json', 'r+') as f:
            coin = json.load(f)
        if len(message.content) >= 10 and str(message.author.id) in coin:
            coin[str(message.author.id)]["coin"] += 1
        with open('cogs/coin.json', 'w') as f:
            json.dump(coin, f)
  

    @commands.command()
    async def coin(ctx, message):
        with open('cogs/coin.json', 'r+') as f:
            coin = json.load(f)
        if not str(message.author.id) in coin:
            coin[str(message.author.id)] = {}  
            coin[str(message.author.id)]["coin"] = 0   
            with open('cogs/coin.json', 'w') as f:
                json.dump(coin, f)
            embeduser = discord.Embed(description=f"เพิ่ม {message.author.mention} เข้า database เรียบร้อยแล้ว", color=0x84c5e6)
            await message.channel.send(embed=embeduser)        
        coinuser = coin[str(message.author.id)]["coin"]
        embed = discord.Embed(title = f"{message.author}", description=f"มียอดคงเหลือ {coinuser} $coin", color=0x84c5e6)
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/77825705?v=4")
        embed.set_footer(text="github : https://github.com/Jannnn1235")
        await message.send(embed=embed)

def setup(client):
    client.add_cog(coin(client))