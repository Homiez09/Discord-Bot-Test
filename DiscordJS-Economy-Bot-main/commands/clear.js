module.exports = {
    name: 'clear',
    description: "ลบข้อความ",
    async execute(bot, message, args, Discord){
        if(!args[0]) return message.reply('Error please define second arg')
        message.channel.bulkDelete(Number(args[0]) + 1);
        console.log(`You have deleted all ${Number(args[0])} messages.`)
    }
}

/* https://github.com/Jannnn1235 */