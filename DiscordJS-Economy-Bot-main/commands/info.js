module.exports = {
    name: 'info',
    description: "This is a embed",
    async execute(bot, message, args, Discord){
        const embed = new Discord.MessageEmbed()
            .setTitle('บัตรประจำตัวประชาชน')
            .addField('ชื่อผู้ใช้' , message.author.username)
            .addField('เลขบัตรประจำตัว' , message.author.id)
            .addField('ที่อยู่ปัจจุบัน', message.guild.name)
            .setColor(0xF1C40F)
            .setThumbnail(message.author.avatarURL({ dynamic:true }))
            .setFooter('github : https://github.com/Jannnn1235')
            message.channel.send(embed);
    }
}

/* https://github.com/Jannnn1235 */