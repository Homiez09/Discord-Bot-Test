/* Made by Phumrapee Soenvanichakul (Jannnn1235) 
สร้างไฟล์ .env
TOKEN=<ใส่ TOKEN บอท>
PREFIX=<ใส่ prefix>
ownerid=<"ใส่ id ของเจ้าของเซิฟ">

คำสั่ง ผู้ใช้
info    [ดูเลขบัตร]
coin    [ดูจำนวนเงิน]      <ให้ user พิมพ์ <prefix>coin เพิ่อ add user เข้า database>
ping    [pong!  ไร้สาระ 5555]

คำสั่ง แอดมิน
givecoin <id> <amount>      [ให้เงิน]
removecoin <id> <amount>    [ลบเงิน]
clear <amount>              [ลบแชท]
*/

require('dotenv').config();
const Discord = require('discord.js');
const bot = new Discord.Client();

const prefix = process.env.PREFIX

const fs = require('fs');
bot.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`)

    bot.commands.set(command.name, command);
}

function jsonReader(filePath, cb){
    fs.readFile('./jsonfile/coins.json', 'utf-8', (err, fileData) => {
        if(err) {
            return cb && cb(err);
        }
        try {
            const object = JSON.parse(fileData);
            return cb && cb(null, object);
        } catch(err) {
            return cb && cb(err);
        }
    });
}

var version = '1.0.0';

bot.on('ready', () => {
    console.log('Bot is now online!');
    bot.user.setActivity('demo', {
        type: 'PLAYING'
    }).catch(console.error);
})

bot.on('guildMemberAdd', member => { /* แจ้งเตือนคนเข้าสู่เซิฟ ใน channel => welcome */
    const channel = member.guild.channels.cache.find(channel => channel.name === "welcome");
    if(!channel) return;

    channel.send(`Welcome to our server, ${member}`)
})

bot.on('message', message => {
    if(!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/);

    const  command = args.shift().toLowerCase();
    

    if(command === 'ping'){
        bot.commands.get('ping').execute(bot, message, args, Discord)
    }
    else if(command === 'info'){
        bot.commands.get('info').execute(bot, message, args, Discord)
    }
    else if(command === 'coin'){
        bot.commands.get('coin').execute(bot, message, args, Discord)
    }

    if(message.author.id === process.env.ownerid){
        if(command === 'clear'){
            bot.commands.get('clear').execute(bot, message, args, Discord)
        }
        else if(command === 'givecoin'){
            bot.commands.get('givecoin').execute(bot, message, args, Discord)
        }
        else if(command === 'removecoin'){
            bot.commands.get('removecoin').execute(bot, message, args, Discord)
        }
    }

})

bot.on('message', msg => {
    if(msg.content.length >= 1){
      
    }
}) 
bot.login(process.env.TOKEN);