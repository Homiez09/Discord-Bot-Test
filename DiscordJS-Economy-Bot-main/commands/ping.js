module.exports = {
    name: 'ping',
    description: "This is a ping command",
    async execute(bot, message, args, Discord){
        message.channel.send('pong')
    }
}

/* https://github.com/Jannnn1235 */