import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil
import config

bot = commands.Bot(command_prefix='t.')

@bot.event  
async def on_ready():
    print('ready')
    await bot.change_presence(activity=discord.Game(name="ร้องเพลง"))

@bot.command(pass_context =True, aliases=['jo','joi','jn'])
async def join(ctx):
    global voice   
    channel = ctx.message.author.voice.channel  
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print("The bot has connencted to channel")
    await ctx.send(f"Joined {channel}")


@bot.command(pass_context =True, aliases=['L','l'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel   
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left channel")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("กูไม่ได้อยู่ในห้องไอ้ควาย")

@bot.command(pass_context =True, aliases=['p','pl','pla'])
async def play(ctx, url: str):
    global voice
    channel = ctx.message.author.voice.channel  
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:  
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print('No more queued song(s)')
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
            if length != 0:
                print("song done, playing next queued")
                print(f"songs still in queue: {still_q}")
                song_there = os.path.isfile("song.mp3")
                if song_there:
                    os.remove("song.mp3")
                shutil.move(song_path, main_location)
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, 'song.mp3')

                voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 70
                
            else:
                queues.clear()
                return
        
        else:
            queues.clear()
            print("No songs were queued before the ending og the last song")

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed old song file")
    except PermissionError:
        print("Trying tp delete song file, but it's being played")
        await ctx.send("**เดอะทอยส์เจ็บคอกระทันหันไม่สามาร้องเพลงได้")
        return

    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:     
            print("Removed old Queue Folder")
        shutil.rmtree(Queue_folder)
    except:
        print("No old Queue Folder")



    await ctx.send("**กำลังวอมเสียงก่อนร้องเพลง")

    voice = get(bot.voice_clients, guild = ctx.guild)
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'True',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 70

    nname = name.rsplit("-", 2)
    await ctx.send(f"กำลังเล่น {nname[0]}")
    print("playing")

@bot.command(pass_context =True, aliases=['pa','pau'])
async def pause(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music paused")
        voice.pause()
        await ctx.send("**เดอะทอยส์หยุดพักจิบน้ำ")
    else:
        print("Music not playing failed pause")
        await ctx.send("**เดอะทอยส์ยังไม่ได้ร้องสักเพลง")

@bot.command(pass_context =True, aliases=['r','res'])
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print('Resumed music')
        voice.resume()
        await ctx.send("เลนเพลงต่อ")
    else: 
        print("Music not playing failed resume")
        await ctx.send("**เดอะทอยส์ยังไม่ได้ร้องสักเพลง")

@bot.command(pass_context =True, aliases=['st','sto'])
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_playing():
        print('Music stopped')
        voice.stop()
        await ctx.send("**เดอะทอยส์ร้องเพลงจบแล้ว")
    else: 
        print("No music playing failed to stop")
        await ctx.send("**เดอะทอยส์ยังไม่ได้ร้องสักเพลง")

queues = {}

@bot.command(pass_context =True, aliases=['q','qu'])
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath("Queue"))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num
    
    queue_path = os.path.abspath(os.path.realpath("Queue") + f"\song{q_num}.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'True',
        'outtmpl': queue_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now")
        ydl.download([url])

    await ctx.send(f'เพิ่มเพลง {str(q_num)} ไปในคิวแล้ว')

    print("เพิ่มเพลงแล้ว")


bot.run(config.TOKEN)
