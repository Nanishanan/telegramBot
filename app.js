const axios = require('axios');
const {Telegraf} = require('telegraf');
const fs = require('fs')
const bot = new Telegraf('5298752852:AAG_r3UJebeYSOO1FmhjHaju6usd5wfUzbQ');
const convertion_function = require('./controller/convert')

bot.command('start', (ctx) => {
    console.log(ctx.from)
    bot.telegram.sendMessage(ctx.chat.id, `Hi ${ctx.from.first_name} ! Welcome to my Bot. Please upload photo to turn it into swag pic`)
})

bot.on('message', async (ctx)=>{
    // console.log(ctx.message.photo[0].file_id)
    const files = ctx.update.message.photo
    const fileID = files[(files.length)-1].file_id

    await ctx.telegram.getFileLink(fileID)
        .then((url)=>{
            var url_href = url['href']
            console.log(url_href)
            axios({url: url_href, responseType: 'stream'})
                .then((response)=>{
                    return new Promise((resolve, reject)=>{
                        response.data.pipe(fs.createWriteStream(__dirname+'/public/images/'+(ctx.from.id)+'.jpg'))
                            .on('finish', ()=>{
                                bot.telegram.sendMessage(ctx.chat.id, `Converting...`)
                                console.log('Uploaded')
                                convert(ctx.from.id, url_href)
                            })
                            .on('error', (e)=>{
                                console.log("Error occured", e)
                            })
                    })
                })
        })
})

function convert(file, url_href){
    convertion_function(file, url_href)
}

bot.launch();