module.exports = {
    name: 'removecoin',
    description: "The Coin is everything",
    async execute(bot, message, args, Discord){
        if(!args[0] && !args[1]) return message.reply('กรุณาป้อนข้อมูลให้ถูกต้อง')
        const fs = require('fs');
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

        jsonReader('./jsonfile/coins.json', (err, data) => {
            if(err){ 
                console.log(args[0], args[1])
                const embed = new Discord.MessageEmbed()
                .addField('ไม่มีผู้ใช้นี้อยู่ในระบบ')
                .setColor(0xF1C40F)
                .setFooter('github : https://github.com/Jannnn1235')
                message.channel.send(embed);
            } else {
                console.log(data[args[0]].coin);
                data[args[0]].coin -= Number(args[1])
  
                fs.writeFile('./jsonfile/coins.json', JSON.stringify(data, null, 2), err =>{
                });
                const embed = new Discord.MessageEmbed()
                .addField('System',`คุณลบ COIN ของ<@${args[0]}> จำนวน ${args[1]}$COIN`)
                .setColor(0xF1C40F)
                .setFooter('github : https://github.com/Jannnn1235')
                message.channel.send(embed);
            }
        });
        


    }
}

/* https://github.com/Jannnn1235 */