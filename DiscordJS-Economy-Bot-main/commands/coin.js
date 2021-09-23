module.exports = {
    name: 'coin',
    description: "The Coin is everything",
    async execute(bot, message, args, Discord){
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

        jsonReader('../jsonfile/coins.json', (err, data) => {
            if(err){
                jsonReader('./jsonfile/coins.json', (err, data) => {
                    if(err){ 
                        console.log(err);
                    } else {
                        var userCreate = JSON.parse(fs.readFileSync('./jsonfile/coins.json')); 
                        userCreate[message.author.id] = {
                            coin: 0   
                        }
                        fs.writeFileSync('./jsonfile/coins.json', JSON.stringify(userCreate, null, 2));
                        message.channel.send(`Added <@${message.author.id}> into database.`)    
                    }
                });
            } else {
                const embed = new Discord.MessageEmbed()
                .addField(`<${message.author.username}>`,`มียอดคงเหลือ ${data[message.author.id].coin} $COIN`)
                .setColor(0xF1C40F)
                .setThumbnail(message.author.avatarURL({ dynamic:true }))
                .setFooter('github : https://github.com/Jannnn1235')
                message.channel.send(embed);
                fs.writeFile('./jsonfile/coins.json', JSON.stringify(data, null, 2), err =>{
                });
            }
        });
    }
}

/* https://github.com/Jannnn1235 */
